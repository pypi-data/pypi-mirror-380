from __future__ import annotations

import asyncio
import logging
import os
import sys
import typing as t
from typing import cast

import bentoml
import httpx
from _bentoml_sdk import ServiceConfig

if t.TYPE_CHECKING:
    T = t.TypeVar("T")


logger = logging.getLogger("bentoml.service")

__all__ = ["service"]


class Router:
    service: bentoml.Service[Router]

    def __command__(self) -> list[str]:
        policy = os.getenv("ROUTER_POLICY", "cache_aware")
        return [
            sys.executable,
            "-m",
            "sglang_router.launch_router",
            "--port",
            "8000",
            "--policy",
            policy,
        ]

    async def __is_ready__(self) -> bool:
        client = cast(httpx.AsyncClient, self.service.context.state["client"])
        # Each time when readyz probe is called, we query all workers and add them to the router.
        # Duplicate workers will be ignored and stale workers will be dropped by the router automatically.
        llm_service = self.service.dependencies["llm"].on
        assert llm_service is not None, "LLM service dependency is not set"
        try:
            hosts = await llm_service.get_hosts()
        except Exception as e:
            logger.error(f"Failed to get hosts from {llm_service.name}: {e}")
            return False
        await asyncio.gather(
            *[
                client.post("/add_worker", params={"url": f"http://{host}"}, timeout=5)
                for host in hosts
            ],
            return_exceptions=True,
        )
        # Then, query the readiness endpoint of the router itself
        try:
            response = await client.get("/readiness", timeout=5.0)
        except (httpx.ConnectError, httpx.RequestError):
            return False
        return response.is_success

    async def __metrics__(self, content: str) -> str:
        client = cast(httpx.AsyncClient, self.service.context.state["client"])
        try:
            response = await client.get("http://localhost:29000", timeout=5.0)
            response.raise_for_status()
        except (httpx.ConnectError, httpx.RequestError) as e:
            logger.error(f"Failed to get metrics: {e}")
            return content
        else:
            return content + "\n" + response.text


@t.overload
def service(inner: type[Router], /) -> bentoml.Service[Router]: ...


@t.overload
def service(
    *,
    name: str | None = None,
    image: bentoml.images.Image | None = None,
    envs: list[dict[str, str]] | None = None,
    labels: dict[str, str] | None = None,
    cmd: list[str] | None = None,
    service_class: type[bentoml.Service[T]] = bentoml.Service,
    **kwargs: t.Unpack[ServiceConfig],
) -> t.Callable[[type], bentoml.Service[Router]]: ...


def service(
    inner: type[T] | None = None,
    /,
    *,
    name: str | None = None,
    image: bentoml.images.Image | None = None,
    description: str | None = None,
    envs: list[dict[str, str]] | None = None,
    labels: dict[str, str] | None = None,
    cmd: list[str] | None = None,
    service_class: type[bentoml.Service[T]] = bentoml.Service,
    **kwargs: t.Unpack[ServiceConfig],
) -> t.Any:
    def decorator(inner: type) -> bentoml.Service[Router]:
        llm_service = bentoml.service(
            name=name, cmd=cmd, service_class=service_class, **kwargs
        )(inner)
        router_service = bentoml.Service(
            "Router",
            inner=Router,
            image=image,
            description=description,
            envs=[
                *(envs or []),
                {
                    "name": "ROUTER_POLICY",
                    "value": os.getenv("ROUTER_POLICY", "cache_aware"),
                },
            ],
            labels=labels or {},
            config={
                "logging": {"access": {"enabled": False}},
                "endpoints": {"livez": "/liveness"},
            },
        )
        router_service.dependencies["llm"] = bentoml.depends(llm_service)
        # Inject the service object into the Router instance
        router_service.inner.service = router_service
        return router_service

    return decorator(inner) if inner is not None else decorator
