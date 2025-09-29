import typing

from celery.local import Proxy

F = typing.TypeVar("F", bound=typing.Callable[..., typing.Any])

def shared_task(func: F) -> Proxy[F]: ...
