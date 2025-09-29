from dataclasses import dataclass

from fred.settings import logger_manager
from fred.utils.dateops import datetime_utcnow
from fred.worker.runner.rest.routers.interface import RouterInterface

logger = logger_manager.get_logger(name=__name__)


class RunnerRouterMethods:

    def handler_exists(self, classname: str, classpath: str) -> dict:
        from fred.worker.runner.handler import RunnerHandler
        from fred.worker.interface import HandlerInterface

        result_payload = {
            "handler_classname": classname,
            "handler_classpath": classpath,
            "exists": False,
            "is_runner_handler": False,
            "metadata": {}
        }

        try:
            handler = HandlerInterface.find_handler(
                import_pattern=classpath,
                handler_classname=classname,
            )
            result_payload["is_runner_handler"] = isinstance(handler, RunnerHandler)
            result_payload["exists"] = True
            return result_payload
        except Exception as e:
            result_payload["metadata"]["error"] = str(e)
            return result_payload

    def qlen(self, queue_slug: str) -> dict:

        snapshot_at = datetime_utcnow().isoformat()
        req_queue = self.runner_backend.queue(f"req:{queue_slug}")
        res_queue = self.runner_backend.queue(f"res:{queue_slug}")
        backend_name = self.runner_backend._cat.name
        return {
            "snapshot_at": snapshot_at,
            "queue_slug": queue_slug,
            "queue_backend": backend_name,
            "req": req_queue.size(),
            "res": res_queue.size(),
        }

    def runner_start(self, payload: dict) -> dict:
        from fred.worker.runner.model.catalog import RunnerModelCatalog
        from fred.worker.runner.plugins.catalog import PluginCatalog
        # Determine which plugin to use; default to LOCAL if not specified
        plugin_name: str = payload.pop("plugin", "LOCAL")
        wait_for_exec: bool = payload.pop("wait_for_exec", False)
        # Create the RunnerSpec from the provided payload
        # TODO: Instead on depending on parsing a dict... Can we implement a base-model to facilitate fast-api validation?
        runner_spec = RunnerModelCatalog.RUNNER_SPEC.value.from_payload(payload=payload)
        # Instantiate the plugin and execute the runner
        plugin = PluginCatalog[plugin_name.upper()]()
        return {
            "runner_id": plugin.execute(runner_spec, wait_for_exec=wait_for_exec, **payload).runner_id,
            "queue_slug": runner_spec.queue_slug,
        }
    
    def runner_execute(self, payload: dict) -> dict:
        from fred.worker.runner.model.catalog import RunnerModelCatalog

        request_id = payload.pop("request_id", None)
        queue_slug = payload.pop("queue_slug", None) or (
            logger.error("No 'queue_slug' value provided; defaulting to 'demo'.")
            or "demo"
        )

        item = RunnerModelCatalog.ITEM.value.uuid(payload=payload, uuid_hash=False)
        request = item.as_request(use_hash=False, request_id=request_id)
        request.dispatch(
            request_queue=self.runner_backend.queue(f"req:{queue_slug}")
        )
        return {
            "item_id": item.item_id,
            "request_id": request.request_id,
            "queue_slug": queue_slug,
            "dispatched_at": datetime_utcnow().isoformat(),
        }


@dataclass(frozen=True, slots=False)
class RunnerRouter(RouterInterface.with_backend(), RunnerRouterMethods):

    def __post_init__(self):
        self.router.add_api_route(
            "/handler_exists",
            self.handler_exists,
            methods=["GET"],
            tags=["Runner"],
            summary="Check if a handler class exists and is a RunnerHandler.",
            response_description="Details about the handler class.",
        )
        self.router.add_api_route(
            "/qlen/{queue_slug}",
            self.qlen,
            methods=["GET"],
            tags=["Runner"],
            summary="Get the length of the request and response queues for a given queue slug.",
            response_description="The lengths of the request and response queues.",
        )
        self.router.add_api_route(
            "/start",
            self.runner_start,
            methods=["POST"],
            tags=["Runner"],
            summary="Start a runner using the specified plugin.",
            response_description="The ID of the started runner.",
        )
        self.router.add_api_route(
            "/execute",
            self.runner_execute,
            methods=["POST"],
            tags=["Runner"],
            summary="Execute a task by dispatching a request to the specified queue.",
            response_description="Details about the dispatched request.",
        )
