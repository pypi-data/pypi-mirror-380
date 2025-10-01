import asyncio
import contextvars
import threading
from collections.abc import Coroutine
from typing import Any, TypeVar

T = TypeVar("T")


def run_sync(coro: Coroutine[Any, Any, T]) -> T:
    """Run a coroutine synchronously.

    This function uses asyncio to run a coroutine in a synchronous context.
    It attempts the following strategies in order:
    1. If no event loop is running, creates a new one and runs the coroutine
    2. If a loop is running, attempts to run the coroutine on that loop
    3. As a last resort, creates a new thread with its own event loop to run the coroutine

    Context variables are properly propagated between threads in all cases.

    Example:
    ```python
    async def f(x: int) -> int:
        return x + 1

    result = run_sync(f(1))
    ```

    Args:
        coro: The coroutine to run synchronously

    Returns:
        The result of the coroutine
    """
    ctx = contextvars.copy_context()
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    try:
        return ctx.run(loop.run_until_complete, coro)
    except RuntimeError as e:
        if "event loop" in str(e):
            return run_sync_in_thread(coro)
        raise e


def run_sync_in_thread(coro: Coroutine[Any, Any, T]) -> T:
    """Run a coroutine synchronously in a new thread.

    This function creates a new thread with its own event loop to run the coroutine.
    Context variables are properly propagated between threads.
    This is useful when you need to run async code in a context where you can't use
    the current event loop (e.g., inside an async frame).

    Example:
    ```python
    async def f(x: int) -> int:
        return x + 1

    result = run_sync_in_thread(f(1))
    ```

    Args:
        coro: The coroutine to run synchronously

    Returns:
        The result of the coroutine
    """
    result: T | None = None
    error: BaseException | None = None
    done = threading.Event()
    ctx = contextvars.copy_context()

    def thread_target() -> None:
        nonlocal result, error
        loop = asyncio.new_event_loop()
        try:
            asyncio.set_event_loop(loop)
            result = ctx.run(loop.run_until_complete, coro)
        except BaseException as e:
            error = e
        finally:
            loop.close()
            asyncio.set_event_loop(None)
            done.set()

    thread = threading.Thread(target=thread_target)
    thread.start()
    done.wait()

    if error is not None:
        raise error

    return result
