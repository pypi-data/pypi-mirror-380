"""WebTransport Application Framework."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from types import TracebackType
from typing import Any, Self, TypeVar

from pywebtransport.config import ServerConfig
from pywebtransport.connection import WebTransportConnection
from pywebtransport.events import Event
from pywebtransport.server.middleware import MiddlewareManager
from pywebtransport.server.router import RequestRouter
from pywebtransport.server.server import WebTransportServer
from pywebtransport.session import WebTransportSession
from pywebtransport.types import EventType, MiddlewareProtocol, SessionHandler
from pywebtransport.utils import get_logger

__all__ = ["ServerApp"]

logger = get_logger(name="server.app")

F = TypeVar("F", bound=Callable[..., Any])


class ServerApp:
    """A high-level WebTransport application with routing and middleware."""

    def __init__(self, *, config: ServerConfig | None = None) -> None:
        """Initialize the server application."""
        self._server = WebTransportServer(config=config)
        self._router = RequestRouter()
        self._middleware_manager = MiddlewareManager()
        self._stateful_middleware: list[Any] = []
        self._startup_handlers: list[Callable[[], Any]] = []
        self._shutdown_handlers: list[Callable[[], Any]] = []
        self._server.on(event_type=EventType.SESSION_REQUEST, handler=self._handle_session_request)

    @property
    def server(self) -> WebTransportServer:
        """Get the underlying WebTransportServer instance."""
        return self._server

    async def __aenter__(self) -> Self:
        """Enter the async context and run startup procedures."""
        await self._server.__aenter__()
        await self.startup()
        logger.info("ServerApp started.")
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit the async context and run shutdown procedures."""
        await self.shutdown()
        await self._server.close()
        logger.info("ServerApp stopped.")

    def run(self, *, host: str | None = None, port: int | None = None, **kwargs: Any) -> None:
        """Run the server application in a new asyncio event loop."""
        final_host = host if host is not None else self.server.config.bind_host
        final_port = port if port is not None else self.server.config.bind_port

        async def main() -> None:
            async with self:
                await self.serve(host=final_host, port=final_port, **kwargs)

        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            logger.info("Server stopped by user.")

    async def serve(self, *, host: str | None = None, port: int | None = None, **kwargs: Any) -> None:
        """Start the server and serve forever."""
        final_host = host if host is not None else self.server.config.bind_host
        final_port = port if port is not None else self.server.config.bind_port
        await self._server.listen(host=final_host, port=final_port)
        await self._server.serve_forever()

    async def shutdown(self) -> None:
        """Run all registered shutdown handlers and exit stateful middleware."""
        for handler in self._shutdown_handlers:
            if asyncio.iscoroutinefunction(handler):
                await handler()
            else:
                handler()
        for middleware in reversed(self._stateful_middleware):
            if hasattr(middleware, "__aexit__"):
                await middleware.__aexit__(exc_type=None, exc_val=None, exc_tb=None)

    async def startup(self) -> None:
        """Run all registered startup handlers and enter stateful middleware."""
        for middleware in self._stateful_middleware:
            if hasattr(middleware, "__aenter__"):
                await middleware.__aenter__()
        for handler in self._startup_handlers:
            if asyncio.iscoroutinefunction(handler):
                await handler()
            else:
                handler()

    def add_middleware(self, *, middleware: MiddlewareProtocol) -> None:
        """Add a middleware to the processing chain."""
        self._middleware_manager.add_middleware(middleware=middleware)
        if hasattr(middleware, "__aenter__") and hasattr(middleware, "__aexit__"):
            self._stateful_middleware.append(middleware)

    def middleware(self, middleware_func: MiddlewareProtocol) -> MiddlewareProtocol:
        """Register a middleware function."""
        self.add_middleware(middleware=middleware_func)
        return middleware_func

    def on_shutdown(self, handler: F) -> F:
        """Register a handler to run on application shutdown."""
        self._shutdown_handlers.append(handler)
        return handler

    def on_startup(self, handler: F) -> F:
        """Register a handler to run on application startup."""
        self._startup_handlers.append(handler)
        return handler

    def pattern_route(self, *, pattern: str) -> Callable[[SessionHandler], SessionHandler]:
        """Register a session handler for a URL pattern."""

        def decorator(handler: SessionHandler) -> SessionHandler:
            self._router.add_pattern_route(pattern=pattern, handler=handler)
            return handler

        return decorator

    def route(self, *, path: str) -> Callable[[SessionHandler], SessionHandler]:
        """Register a session handler for a specific path."""

        def decorator(handler: SessionHandler) -> SessionHandler:
            self._router.add_route(path=path, handler=handler)
            return handler

        return decorator

    async def _handle_session_request(self, event: Event) -> None:
        """Handle an incoming session request event from the server."""
        if not isinstance(event.data, dict):
            logger.warning("Session request event data is not a dictionary")
            return

        connection = event.data.get("connection")
        if not isinstance(connection, WebTransportConnection) or not connection.protocol_handler:
            logger.warning("Invalid connection object in session request")
            return

        session_id = event.data.get("session_id")
        stream_id = event.data.get("stream_id")
        if not session_id or stream_id is None:
            if not session_id:
                logger.warning("Missing session_id in session request")
            else:
                logger.warning("Missing stream_id in session request")
            return

        if not connection.is_connected:
            logger.warning("Connection %s is not in connected state", connection.connection_id)
            return

        logger.info("Processing session request: session_id=%s, stream_id=%s", session_id, stream_id)
        try:
            session_info = connection.protocol_handler.get_session_info(session_id=session_id)
            if not session_info:
                logger.error("Session info not found for session %s", session_id)
                return

            config = connection.config
            if not isinstance(config, ServerConfig):
                logger.error("Connection %s has a non-server config, which is unexpected.", connection.connection_id)
                connection.protocol_handler.close_webtransport_session(
                    session_id=session_id,
                    code=1,
                    reason="Internal server configuration error",
                )
                return

            session = WebTransportSession(
                connection=connection,
                session_id=session_id,
                max_streams=config.max_streams_per_connection,
                max_incoming_streams=config.max_incoming_streams,
                stream_cleanup_interval=config.stream_cleanup_interval,
            )
            await session.initialize()
            session._path = session_info.path
            session._headers = session_info.headers
            session._control_stream_id = stream_id

            if self.server.session_manager:
                await self.server.session_manager.add_session(session=session)

            logger.info("Processing session request for path '%s'", session.path)
            if not await self._middleware_manager.process_request(session=session):
                logger.warning(
                    "Session request for path '%s' rejected by middleware.",
                    session.path,
                )
                connection.protocol_handler.close_webtransport_session(
                    session_id=session_id, code=403, reason="Rejected by middleware"
                )
                return

            handler = self._router.route_request(session=session)
            if not handler:
                logger.warning("No route found for path: %s", session.path)
                connection.protocol_handler.close_webtransport_session(
                    session_id=session_id, code=404, reason="Route not found"
                )
                return

            logger.info("Routing session request for path '%s' to handler '%s'", session.path, handler.__name__)
            connection.protocol_handler.accept_webtransport_session(stream_id=stream_id, session_id=session_id)
            logger.info("Handler task created for session %s", session_id)

            async def run_handler(*, h: SessionHandler, s: WebTransportSession) -> None:
                try:
                    logger.debug("Handler starting for session %s", s.session_id)
                    await h(s)
                    logger.debug("Handler completed for session %s", s.session_id)
                except Exception as handler_error:
                    logger.error("Handler error for session %s: %s", s.session_id, handler_error, exc_info=True)
                finally:
                    if not s.is_closed:
                        logger.debug("Closing session %s", s.session_id)
                        await s.close()

            asyncio.create_task(run_handler(h=handler, s=session))

        except Exception as e:
            logger.error("Error handling session request for session %s: %s", session_id, e, exc_info=True)
            try:
                if connection.protocol_handler:
                    connection.protocol_handler.close_webtransport_session(
                        session_id=session_id,
                        code=1,
                        reason="Internal server error",
                    )
            except Exception:
                pass
