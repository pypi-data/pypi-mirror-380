"""WebTransport connection manager implementation."""

from __future__ import annotations

import asyncio
import weakref
from collections import defaultdict
from types import TracebackType
from typing import Any, Self

from pywebtransport.connection.connection import WebTransportConnection
from pywebtransport.constants import (
    DEFAULT_CONNECTION_CLEANUP_INTERVAL,
    DEFAULT_CONNECTION_IDLE_CHECK_INTERVAL,
    DEFAULT_CONNECTION_IDLE_TIMEOUT,
    DEFAULT_SERVER_MAX_CONNECTIONS,
)
from pywebtransport.exceptions import ConnectionError
from pywebtransport.types import ConnectionId, EventType
from pywebtransport.utils import get_logger, get_timestamp

__all__ = ["ConnectionManager"]

logger = get_logger(name="connection.manager")


class ConnectionManager:
    """Manages multiple WebTransport connections with concurrency safety."""

    def __init__(
        self,
        *,
        max_connections: int = DEFAULT_SERVER_MAX_CONNECTIONS,
        connection_cleanup_interval: float = DEFAULT_CONNECTION_CLEANUP_INTERVAL,
        connection_idle_check_interval: float = DEFAULT_CONNECTION_IDLE_CHECK_INTERVAL,
        connection_idle_timeout: float = DEFAULT_CONNECTION_IDLE_TIMEOUT,
    ) -> None:
        """Initialize the connection manager."""
        self._max_connections = max_connections
        self._cleanup_interval = connection_cleanup_interval
        self._idle_check_interval = connection_idle_check_interval
        self._idle_timeout = connection_idle_timeout
        self._lock: asyncio.Lock | None = None
        self._connections: dict[ConnectionId, WebTransportConnection] = {}
        self._stats = {
            "total_created": 0,
            "total_closed": 0,
            "current_count": 0,
            "max_concurrent": 0,
        }
        self._cleanup_task: asyncio.Task[None] | None = None
        self._idle_check_task: asyncio.Task[None] | None = None
        self._is_shutting_down = False

    @classmethod
    def create(
        cls,
        *,
        max_connections: int = DEFAULT_SERVER_MAX_CONNECTIONS,
        connection_cleanup_interval: float = DEFAULT_CONNECTION_CLEANUP_INTERVAL,
        connection_idle_check_interval: float = DEFAULT_CONNECTION_IDLE_CHECK_INTERVAL,
        connection_idle_timeout: float = DEFAULT_CONNECTION_IDLE_TIMEOUT,
    ) -> Self:
        """Factory method to create a new connection manager instance."""
        return cls(
            max_connections=max_connections,
            connection_cleanup_interval=connection_cleanup_interval,
            connection_idle_check_interval=connection_idle_check_interval,
            connection_idle_timeout=connection_idle_timeout,
        )

    async def __aenter__(self) -> Self:
        """Enter async context, initializing resources and starting background tasks."""
        self._lock = asyncio.Lock()
        self._start_background_tasks()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit async context, shutting down the manager."""
        await self.shutdown()

    async def shutdown(self) -> None:
        """Shut down the manager and all associated tasks and connections."""
        if self._is_shutting_down:
            return

        self._is_shutting_down = True

        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass

        if self._idle_check_task:
            self._idle_check_task.cancel()
            try:
                await self._idle_check_task
            except asyncio.CancelledError:
                pass

        await self.close_all_connections()
        logger.info("Connection manager shutdown complete")

    async def add_connection(self, *, connection: WebTransportConnection) -> ConnectionId:
        """Add a new connection to the manager."""
        if self._lock is None:
            raise ConnectionError(
                message=(
                    "ConnectionManager has not been activated. It must be used as an "
                    "asynchronous context manager (`async with ...`)."
                )
            )

        async with self._lock:
            if len(self._connections) >= self._max_connections:
                raise ConnectionError(message=f"Maximum connections ({self._max_connections}) exceeded")

            connection_id = connection.connection_id
            self._connections[connection_id] = connection
            manager_ref = weakref.ref(self)

            async def on_close(event: Any) -> None:
                manager = manager_ref()
                if manager and isinstance(event.data, dict):
                    await manager.remove_connection(connection_id=event.data["connection_id"])

            connection.once(event_type=EventType.CONNECTION_CLOSED, handler=on_close)

            self._stats["total_created"] += 1
            self._update_stats_unsafe()
            logger.debug("Added connection %s (total: %d)", connection_id, len(self._connections))
            return connection_id

    async def close_all_connections(self) -> None:
        """Close all currently managed connections."""
        if self._lock is None:
            raise ConnectionError(
                message=(
                    "ConnectionManager has not been activated. It must be used as an "
                    "asynchronous context manager (`async with ...`)."
                )
            )

        connections_to_close: list[WebTransportConnection] = []
        async with self._lock:
            if not self._connections:
                return
            connections_to_close = list(self._connections.values())
            logger.info("Closing %d connections", len(connections_to_close))
            self._connections.clear()

        try:
            async with asyncio.TaskGroup() as tg:
                for conn in connections_to_close:
                    tg.create_task(conn.close())
        except* Exception as eg:
            logger.error("Errors occurred while closing connections: %s", eg.exceptions, exc_info=eg)

        async with self._lock:
            self._stats["total_closed"] += len(connections_to_close)
            self._update_stats_unsafe()

        logger.info("All connections closed")

    async def get_connection(self, *, connection_id: ConnectionId) -> WebTransportConnection | None:
        """Retrieve a connection by its ID."""
        if self._lock is None:
            raise ConnectionError(
                message=(
                    "ConnectionManager has not been activated. It must be used as an "
                    "asynchronous context manager (`async with ...`)."
                )
            )

        async with self._lock:
            return self._connections.get(connection_id)

    async def remove_connection(self, *, connection_id: ConnectionId) -> WebTransportConnection | None:
        """Remove a connection from the manager by its ID."""
        if self._lock is None:
            raise ConnectionError(
                message=(
                    "ConnectionManager has not been activated. It must be used as an "
                    "asynchronous context manager (`async with ...`)."
                )
            )

        async with self._lock:
            connection = self._connections.pop(connection_id, None)
            if connection:
                self._stats["total_closed"] += 1
                self._update_stats_unsafe()
                logger.debug("Removed connection %s (total: %d)", connection_id, len(self._connections))
            return connection

    async def cleanup_closed_connections(self) -> int:
        """Find and remove any connections that are marked as closed."""
        if self._lock is None:
            raise ConnectionError(
                message=(
                    "ConnectionManager has not been activated. It must be used as an "
                    "asynchronous context manager (`async with ...`)."
                )
            )

        closed_connection_ids = []
        async with self._lock:
            for conn_id, conn in list(self._connections.items()):
                if conn.is_closed:
                    closed_connection_ids.append(conn_id)

            for conn_id in closed_connection_ids:
                del self._connections[conn_id]

            if closed_connection_ids:
                self._stats["total_closed"] += len(closed_connection_ids)
                self._update_stats_unsafe()
                logger.debug("Cleaned up %d closed connections.", len(closed_connection_ids))

        return len(closed_connection_ids)

    async def get_all_connections(self) -> list[WebTransportConnection]:
        """Retrieve a list of all current connections."""
        if self._lock is None:
            raise ConnectionError(
                message=(
                    "ConnectionManager has not been activated. It must be used as an "
                    "asynchronous context manager (`async with ...`)."
                )
            )

        async with self._lock:
            return list(self._connections.values())

    def get_connection_count(self) -> int:
        """Get the current number of active connections."""
        return len(self._connections)

    async def get_stats(self) -> dict[str, Any]:
        """Get detailed statistics about the managed connections."""
        if self._lock is None:
            raise ConnectionError(
                message=(
                    "ConnectionManager has not been activated. It must be used as an "
                    "asynchronous context manager (`async with ...`)."
                )
            )

        async with self._lock:
            states: dict[str, int] = defaultdict(int)
            for conn in self._connections.values():
                states[conn.state] += 1
            return {
                **self._stats,
                "active": len(self._connections),
                "states": dict(states),
                "max_connections": self._max_connections,
            }

    def _on_cleanup_done(self, task: asyncio.Task[None]) -> None:
        """Callback to ensure cleanup is triggered when the cleanup task finishes."""
        if self._is_shutting_down:
            return

        if not task.cancelled():
            if exc := task.exception():
                logger.error("Connection cleanup task finished unexpectedly: %s.", exc, exc_info=exc)

        asyncio.create_task(self.shutdown())

    def _on_idle_check_done(self, task: asyncio.Task[None]) -> None:
        """Callback to ensure cleanup is triggered when the idle check task finishes."""
        if self._is_shutting_down:
            return

        if not task.cancelled():
            if exc := task.exception():
                logger.error("Connection idle check task finished unexpectedly: %s.", exc, exc_info=exc)

        asyncio.create_task(self.shutdown())

    async def _periodic_cleanup(self) -> None:
        """Periodically run the cleanup process to remove closed connections."""
        try:
            while True:
                try:
                    await self.cleanup_closed_connections()
                except Exception as e:
                    logger.error("Connection cleanup cycle failed: %s", e, exc_info=e)

                await asyncio.sleep(self._cleanup_interval)
        except (Exception, asyncio.CancelledError):
            pass

    async def _periodic_idle_check(self) -> None:
        """Periodically check for and close idle connections."""
        if self._lock is None:
            logger.warning("Idle check task running on uninitialized ConnectionManager; stopping.")
            return

        try:
            while True:
                try:
                    idle_connections_to_close = []
                    now = get_timestamp()

                    async with self._lock:
                        all_connections = list(self._connections.values())

                    for conn in all_connections:
                        if conn.is_closing or conn.is_closed:
                            continue

                        if self._idle_timeout > 0 and conn.last_activity_time > 0:
                            idle_duration = now - conn.last_activity_time
                            if idle_duration > self._idle_timeout:
                                idle_connections_to_close.append(conn)

                    if idle_connections_to_close:
                        logger.info("Closing %d idle connections.", len(idle_connections_to_close))
                        try:
                            async with asyncio.TaskGroup() as tg:
                                for conn in idle_connections_to_close:
                                    tg.create_task(conn.close(reason="Idle timeout"))
                        except* Exception as eg:
                            logger.error(
                                "Errors occurred while closing idle connections: %s", eg.exceptions, exc_info=eg
                            )

                except Exception as e:
                    logger.error("Idle connection check cycle failed: %s", e, exc_info=e)

                await asyncio.sleep(self._idle_check_interval)
        except (Exception, asyncio.CancelledError):
            pass

    def _start_background_tasks(self) -> None:
        """Start all periodic background tasks."""
        if self._cleanup_task is None or self._cleanup_task.done():
            self._cleanup_task = asyncio.create_task(self._periodic_cleanup())
            self._cleanup_task.add_done_callback(self._on_cleanup_done)

        if self._idle_check_task is None or self._idle_check_task.done():
            self._idle_check_task = asyncio.create_task(self._periodic_idle_check())
            self._idle_check_task.add_done_callback(self._on_idle_check_done)

    def _update_stats_unsafe(self) -> None:
        """Update internal statistics (must be called within a lock)."""
        current_count = len(self._connections)
        self._stats["current_count"] = current_count
        self._stats["max_concurrent"] = max(self._stats["max_concurrent"], current_count)
