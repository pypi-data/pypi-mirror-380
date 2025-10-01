from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from typing import Callable, Generator, Iterable, Iterator, TypeVar

from jinja2 import Template
from tenacity import retry, stop_after_attempt, wait_random_exponential

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def item_formatter(template: str) -> Template:
    return Template(
        template,
        variable_start_string="{",
        variable_end_string="}",
        autoescape=False,
        keep_trailing_newline=True,
        finalize=lambda x: x or "",
    )


def retryable(function: T1) -> T1:
    retryobj = retry(
        wait=wait_random_exponential(min=1, max=30),
        stop=stop_after_attempt(10),
        reraise=True,
    )
    return retryobj(function)  # type: ignore


@contextmanager
def concurrentcontext(
    function: Callable[[T1], T2],
    generator: Iterable[T1],
    *,
    workers: int | None = None,
) -> Generator[Iterator[T2], None, None]:
    """With context, run a function on a batch of arguments concurrently."""

    with ThreadPoolExecutor(max_workers=workers) as executor:
        yield executor.map(function, generator)


def concurrent(
    function: Callable[[T1], T2],
    generator: Iterable[T1],
    *,
    workers: int | None = None,
) -> list[T2]:
    """Run a functions on a batch of arguments in concurrently."""

    with concurrentcontext(function, generator, workers=workers) as results:
        return list(results)
