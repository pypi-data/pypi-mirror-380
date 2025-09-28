# sync_client.py
from __future__ import annotations

from typing import Any, Callable, Iterator, Optional, Awaitable
from .async_client import AsyncManiac
from .loop_runner import LoopRunner


class Maniac:
    def __init__(self, **opts: Any) -> None:
        self._runner = LoopRunner()
        self._client = AsyncManiac(**opts)

        self._chat = _SyncChat(self._runner, self._client)
        self._completions = _SyncRegisterOnly(self._runner, self._client)
        self._models = _SyncModels(self._runner, self._client)
        self._containers = _SyncContainers(self._runner, self._client)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

    def close(self) -> None:
        try:
            self._runner.run(self._client.aclose())
        finally:
            self._runner.stop()

    @property
    def chat(self) -> "_SyncChat":
        return self._chat

    @property
    def completions(self) -> "_SyncRegisterOnly":
        return self._completions

    @property
    def models(self) -> "_SyncModels":
        return self._models

    @property
    def containers(self) -> "_SyncContainers":
        return self._containers


class _SyncChat:
    def __init__(self, runner: LoopRunner, client: AsyncManiac) -> None:
        self.completions = _SyncCompletions(runner, client)


class _SyncCompletions:
    def __init__(self, runner: LoopRunner, client: AsyncManiac) -> None:
        self._r = runner
        self._c = client

    def create(self, **params: Any) -> Any:
        return self._r.run(self._c.chat.completions.create(params))

    def create_with_stream(self, **params: Any) -> Iterator[Any]:
        import queue

        q: "queue.Queue[object]" = queue.Queue()
        SENTINEL = object()

        async def pump():
            try:
                async for chunk in self._c.chat.completions.create_with_stream(params):
                    q.put(chunk)
            finally:
                q.put(SENTINEL)

        self._r.run(pump())
        while True:
            item = q.get()
            if item is SENTINEL:
                break
            yield item

    def stream(
        self,
        *,
        callback: Optional[Callable[[Any], Awaitable[None] | None]] = None,
        **params: Any,
    ) -> Iterator[Any] | None:
        if callback is None:
            return self.create_with_stream(**params)

        async def _run_with_callback():
            async for chunk in self._c.chat.completions.create_with_stream(params):
                maybe = callback(chunk)
                if maybe is not None and hasattr(maybe, "__await__"):
                    await maybe

        self._r.run(_run_with_callback())
        return None

    def register(self, **input: Any) -> Any:
        return self._r.run(self._c.completions.register(input))


class _SyncRegisterOnly:
    def __init__(self, runner: LoopRunner, client: AsyncManiac) -> None:
        self._r = runner
        self._c = client

    def register(self, **input: Any) -> Any:
        return self._r.run(self._c.completions.register(input))


class _SyncModels:
    def __init__(self, runner: LoopRunner, client: AsyncManiac) -> None:
        self._r = runner
        self._c = client

    def list(self) -> Any:
        return self._r.run(self._c.models.list())

    def retrieve(self, id: str) -> Any:
        return self._r.run(self._c.models.retrieve(id))


class _SyncContainers:
    def __init__(self, runner: LoopRunner, client: AsyncManiac) -> None:
        self._r = runner
        self._c = client

    def create(self, **params: Any) -> Any:
        return self._r.run(self._c.containers.create(params))

    def get(self, **params: Any) -> Any:
        return self._r.run(self._c.containers.get(params))
