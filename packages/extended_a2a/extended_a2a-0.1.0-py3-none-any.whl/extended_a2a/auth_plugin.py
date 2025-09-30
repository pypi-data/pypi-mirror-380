"""
Custom call context builder that extracts authentication headers
"""

import logging
import os
from collections.abc import AsyncGenerator
from typing import Any

from a2a.server.apps import CallContextBuilder
from a2a.server.apps.jsonrpc import StarletteUserProxy
from a2a.server.context import ServerCallContext
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.types import (
    JSONRPCError,
    Message,
    MessageSendParams,
    Task,
    TaskArtifactUpdateEvent,
    TaskIdParams,
    TaskStatusUpdateEvent,
)
from a2a.utils.errors import ServerError
from dotenv import load_dotenv
from starlette.requests import Request

load_dotenv()

logger = logging.getLogger("auth_context")


class AuthCallContextBuilder(CallContextBuilder):
    """Custom context builder that extracts authentication headers"""

    def build(self, request: Request) -> ServerCallContext:
        """
        Build ServerCallContext with authentication headers extracted from the request
        """
        try:
            # Extract headers from the request
            request_headers = {}
            for header_name, header_value in request.headers.items():
                request_headers[header_name.lower()] = header_value

            # Log headers for debugging (remove in production)
            logger.debug(f"Extracted headers: {list(request_headers.keys())}")

            # Handle user proxy safely (don't require AuthenticationMiddleware)
            try:
                user = StarletteUserProxy(
                    request.user if hasattr(request, "user") else None
                )
            except Exception as user_error:
                logger.debug(
                    f"Could not create user proxy (this is normal without AuthenticationMiddleware): {user_error}"
                )
                # Create a basic user proxy
                user = StarletteUserProxy(None)

            # Create context with headers stored in state
            context = ServerCallContext(
                user=user,
                state={"request_headers": request_headers},
                activated_extensions=set(),
                requested_extensions=set(),
            )

            logger.debug(
                f"✅ Successfully built context with {len(request_headers)} headers"
            )
            return context

        except Exception as e:
            logger.error(f"Error building context: {e}")
            # Return a basic context with whatever headers we managed to extract
            try:
                request_headers = {}
                for header_name, header_value in request.headers.items():
                    request_headers[header_name.lower()] = header_value

                return ServerCallContext(
                    user=StarletteUserProxy(None),
                    state={"request_headers": request_headers},
                    activated_extensions=set(),
                    requested_extensions=set(),
                )
            except Exception:
                # Last resort - empty context
                return ServerCallContext(
                    user=StarletteUserProxy(None),
                    state={},
                    activated_extensions=set(),
                    requested_extensions=set(),
                )


class AuthenticatedRequestHandler(DefaultRequestHandler):
    """Request handler with authentication enforcement"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configure valid credentials (in production, use secure storage)
        self.valid_bearer_token = os.getenv("A2A_BEARER_TOKEN")
        self.valid_api_key = os.getenv("A2A_API_KEY")

        assert self.valid_bearer_token or self.valid_api_key, (
            "At least one of A2A_BEARER_TOKEN or A2A_API_KEY must be set in environment"
        )

    def _validate_authentication(self, context: ServerCallContext | None) -> bool:
        """
        Validate authentication from request context
        Returns True if authenticated, False otherwise
        """
        if not context:
            logger.warning("No context available")
            return False

        # Check if authentication info is stored in context state
        # The Starlette app should populate this during request processing
        auth_headers = context.state.get("request_headers", {})

        if not auth_headers:
            logger.warning("No authentication headers found in context")
            return False

        # Check Bearer token authentication
        auth_header = auth_headers.get("authorization", "")
        if auth_header.lower().startswith("bearer "):
            token = auth_header[7:]  # Remove "Bearer " prefix
            if token == self.valid_bearer_token:
                logger.info("Authenticated with bearer token")
                return True
            else:
                logger.warning("Invalid bearer token provided")

        # Check API key authentication
        api_key = auth_headers.get("x-api-key", "")
        if api_key and api_key == self.valid_api_key:
            logger.info("Authenticated with API key")
            return True

        logger.warning("Authentication failed - no valid credentials found")
        return False

    def _raise_auth_error(self) -> None:
        """Raise authentication error using proper ServerError mechanism"""
        auth_error = JSONRPCError(
            code=-32001,  # Custom error code for authentication
            message="Authentication required",
            data={"error": "Please provide valid Bearer token or API key"},
        )
        raise ServerError(auth_error)

    async def on_message_send(
        self, params: MessageSendParams, context: ServerCallContext | None = None
    ) -> Task | Message:
        """Handle message send with authentication check"""
        if not self._validate_authentication(context):
            logger.error("Authentication failed for message/send")
            self._raise_auth_error()

        logger.info("Authentication successful, processing message/send")
        return await super().on_message_send(params, context)

    async def on_message_send_stream(
        self, params: MessageSendParams, context: ServerCallContext | None = None
    ) -> AsyncGenerator[
        Message | Task | TaskStatusUpdateEvent | TaskArtifactUpdateEvent, None
    ]:
        """Handle message stream with authentication check"""
        if not self._validate_authentication(context):
            logger.error("Authentication failed for message/stream")
            self._raise_auth_error()

        logger.info("Authentication successful, processing message/stream")
        async for event in super().on_message_send_stream(params, context):
            yield event

    async def on_get_task(
        self, params: TaskIdParams, context: ServerCallContext | None = None
    ) -> Task | None:
        """Handle get task with authentication check"""
        if not self._validate_authentication(context):
            logger.error("Authentication failed for tasks/get")
            self._raise_auth_error()

        return await super().on_get_task(params, context)

    async def on_cancel_task(
        self, params: TaskIdParams, context: ServerCallContext | None = None
    ) -> Task | None:
        """Handle cancel task with authentication check"""
        if not self._validate_authentication(context):
            logger.error("Authentication failed for tasks/cancel")
            self._raise_auth_error()

        return await super().on_cancel_task(params, context)

    async def on_list_tasks(
        self, params: Any, context: ServerCallContext | None = None
    ) -> list[Task]:
        """Handle list tasks with authentication check"""
        if not self._validate_authentication(context):
            logger.error("Authentication failed for tasks/list")
            self._raise_auth_error()

        return await super().on_list_tasks(params, context)
