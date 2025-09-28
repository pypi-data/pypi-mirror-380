from __future__ import annotations

import asyncio
import io
import uuid
from typing import Callable, Dict, Optional

import socketio
from loguru import logger

from ..constants import (
    EVENT_FT_ERROR,
    EVENT_FT_TRANSCRIBE_FILE,
    EVENT_FT_TRANSCRIBE_FILE_UPLOAD_SUCCESS,
    EVENT_FT_TRANSCRIBE_RESULT,
    ASRModelEnum,
    LanguageEnum,
)
from ..protocol import encode_string, encode_uint8, encode_uuid
from ..types import (
    ErrorResponse,
    FileUploadedResponse,
    FtTranscribeResponse,
)

FtTranscribeHandler = Callable[[FtTranscribeResponse], None]
FileUploadedHandler = Callable[[FileUploadedResponse], None]
ErrorHandler = Callable[[ErrorResponse], None]


class _TranscriptionContext:
    def __init__(
        self,
        on_response: Optional[FtTranscribeHandler],
        on_file_upload: Optional[FileUploadedHandler],
        on_error: Optional[ErrorHandler],
    ):
        self.on_response = on_response
        self.on_file_upload = on_file_upload
        self.on_error = on_error
        self.final_result: Optional[FtTranscribeResponse] = None

        # Signals completion on final result or error
        loop = asyncio.get_event_loop()
        self.done_future: asyncio.Future[None] = loop.create_future()


class FastTranscriptionClient:
    def __init__(
        self,
        api_url: str,
        api_path: str,
        api_key: str,
        on_connect: Optional[Callable[[], None]] = None,
        on_file_upload: Optional[Callable[[FileUploadedResponse | None], None]] = None,
        on_error: Optional[Callable[[ErrorResponse | None], None]] = None,
        verbose: bool = False,
    ):
        if not api_url or not api_path or not api_key:
            raise ValueError("api_url, api_path, and api_key are required")

        self._api_url = api_url
        self._api_path = api_path
        self._api_key = api_key
        self._sio: Optional[socketio.AsyncClient] = None

        # Dedicated event loop for sync usage to avoid cross-loop hangs
        self._sync_loop: Optional[asyncio.AbstractEventLoop] = None

        # Logging verbosity for the underlying Socket.IO client
        self._verbose = verbose

        self.connected_handler: Optional[Callable[[], None]] = on_connect
        self.error_handler: Optional[Callable[[ErrorResponse | None], None]] = on_error
        self.file_uploaded_handler: Optional[
            Callable[[FileUploadedResponse | None], None]
        ] = on_file_upload

        # Internal per-transcription contexts keyed by UUID
        self._transcribe_contexts: Dict[uuid.UUID, _TranscriptionContext] = {}

    def _ensure_client(self) -> socketio.AsyncClient:
        if self._sio is None:
            self._sio = socketio.AsyncClient(
                engineio_logger=self._verbose, logger=self._verbose
            )
            self._sio.on("connect", self._on_connect)
            self._sio.on(
                EVENT_FT_TRANSCRIBE_FILE_UPLOAD_SUCCESS, self._on_file_uploaded
            )
            self._sio.on(EVENT_FT_ERROR, self._on_error)
            self._sio.on(EVENT_FT_TRANSCRIBE_RESULT, self._on_transcription_result)
        return self._sio

    async def _on_connect(self):
        if self.connected_handler:
            self.connected_handler()

    async def _on_file_uploaded(self, data):
        if self.file_uploaded_handler:
            try:
                model = FileUploadedResponse.model_validate(data)
            except Exception:
                model = None
            self.file_uploaded_handler(model)

        try:
            model = FileUploadedResponse.model_validate(data)
            if model and model.id:
                ctx = self._transcribe_contexts.get(model.id.UUID)
                if not ctx:
                    return
                if ctx.on_file_upload:
                    ctx.on_file_upload(model)
        except Exception:
            pass

    async def _on_error(self, data):
        try:
            model = ErrorResponse.model_validate(data)
        except Exception:
            model = None

        if self.error_handler:
            self.error_handler(model)

        if model and model.id:
            ctx = self._transcribe_contexts.pop(model.id.UUID, None)
            if not ctx:
                return

            if ctx.on_error:
                ctx.on_error(model)
                if not ctx.done_future.done():
                    ctx.done_future.set_result(None)

    async def _on_transcription_result(self, data):
        try:
            model = FtTranscribeResponse.model_validate(data)
            ctx = self._transcribe_contexts.get(model.id.UUID)
            if not ctx:
                return

            if ctx.on_response:
                ctx.on_response(model)
            if model.is_final:
                ctx.final_result = model
                self._transcribe_contexts.pop(model.id.UUID, None)
                if not ctx.done_future.done():
                    ctx.done_future.set_result(None)
        except Exception:
            logger.exception("Failed to process transcription result")

    async def connect(self) -> None:
        sio = self._ensure_client()
        if sio.connected:
            return

        await sio.connect(
            self._api_url,
            headers={
                "x-api-key": self._api_key,
                "Origin": "https://pypi.org/project/sautech/",
            },
            socketio_path=self._api_path,
            transports=["websocket"],
        )
        logger.info("Connected to FastTranscriptionClient")

    async def close(self) -> None:
        if self._sio:
            try:
                if self._sio.connected:
                    await self._sio.disconnect()
            except asyncio.CancelledError:
                pass
            except Exception:
                logger.exception("Error while disconnecting FastTranscriptionClient")
            finally:
                # Clean up underlying aiohttp session
                try:
                    if (
                        (eio_client := getattr(self._sio, "eio", None))
                        and (http_session := getattr(eio_client, "http", None))
                        and not getattr(http_session, "closed", True)
                    ):
                        await http_session.close()
                except Exception:
                    pass
                self._sio = None
        logger.info("Disconnected from FastTranscriptionClient")

    def close_sync(self) -> None:
        if self._sync_loop is not None:
            try:
                self._sync_loop.run_until_complete(self.close())
            finally:
                try:
                    self._sync_loop.close()
                except Exception:
                    pass
                self._sync_loop = None
        else:
            asyncio.run(self.close())

    def _get_sync_loop(self) -> asyncio.AbstractEventLoop:
        if self._sync_loop is None:
            self._sync_loop = asyncio.new_event_loop()
        return self._sync_loop

    def _run_sync(self, coro):
        loop = self._get_sync_loop()
        return loop.run_until_complete(coro)

    async def __aenter__(self) -> "FastTranscriptionClient":
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    def __enter__(self) -> "FastTranscriptionClient":
        self._run_sync(self.connect())
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close_sync()

    async def transcribe(
        self,
        audio_source: bytes | io.BufferedReader,
        language: LanguageEnum,
        asr_model: ASRModelEnum,
        on_response: Optional[FtTranscribeHandler] = None,
        on_file_upload: Optional[FileUploadedHandler] = None,
        on_error: Optional[ErrorHandler] = None,
    ) -> Optional[FtTranscribeResponse]:
        await self.connect()

        uid = uuid.uuid4()
        ctx = _TranscriptionContext(
            on_response=on_response,
            on_file_upload=on_file_upload,
            on_error=on_error,
        )
        self._transcribe_contexts[uid] = ctx

        header = (
            encode_uuid(uid)
            + encode_uint8(int(language))
            + encode_string(str(asr_model))
            + encode_string("")  # diarization model key
            + encode_string("")  # itn model key
            + encode_string("")  # redact model key
        )

        read_method = getattr(audio_source, "read", None)
        audio_bytes = read_method() if callable(read_method) else bytes(audio_source)
        payload = header + audio_bytes

        assert self._sio is not None
        await self._sio.emit(EVENT_FT_TRANSCRIBE_FILE, payload)

        try:
            await ctx.done_future
            return ctx.final_result
        finally:
            self._transcribe_contexts.pop(uid, None)

    def transcribe_sync(
        self,
        audio_source: bytes | io.BufferedReader,
        language: LanguageEnum,
        asr_model: ASRModelEnum,
        on_response: Optional[FtTranscribeHandler] = None,
        on_file_upload: Optional[FileUploadedHandler] = None,
        on_error: Optional[ErrorHandler] = None,
    ) -> Optional[FtTranscribeResponse]:
        return self._run_sync(
            self.transcribe(
                audio_source,
                language,
                asr_model,
                on_response=on_response,
                on_file_upload=on_file_upload,
                on_error=on_error,
            )
        )
