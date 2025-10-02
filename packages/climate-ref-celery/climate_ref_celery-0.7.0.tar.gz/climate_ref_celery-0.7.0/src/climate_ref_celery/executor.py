"""
Executor for running diagnostics asynchronously using Celery
"""

import time
from typing import Any

import celery.exceptions
import celery.result
from loguru import logger
from tqdm import tqdm

from climate_ref.config import Config
from climate_ref.models import Execution
from climate_ref_celery.app import app
from climate_ref_celery.tasks import generate_task_name
from climate_ref_core.diagnostics import ExecutionDefinition, ExecutionResult
from climate_ref_core.executor import Executor


class CeleryExecutor(Executor):
    """
    Run a diagnostic asynchronously

    Celery is an asynchronous task queue/job queue based on distributed message passing.
    Celery uses a message broker to distribute tasks across a cluster of worker nodes.
    The worker nodes are responsible for executing the tasks.
    The message broker used in this case is [Redis](https://github.com/redis/redis).
    The worker node may be running on the same machine as the client or on a different machine,
    either natively or via a docker container.

    We cannot resume tasks that are in progress if the process terminates.
    That should be possible tracking some additional state in the database.
    """

    name = "celery"

    def __init__(self, *, config: Config, **kwargs: Any) -> None:
        self.config = config
        super().__init__(**kwargs)  # type: ignore
        self._results: list[celery.result.AsyncResult[ExecutionResult]] = []

    def run(
        self,
        definition: ExecutionDefinition,
        execution: Execution | None = None,
    ) -> None:
        """
        Run a diagnostic calculation

        This will queue the diagnostic to be run by a Celery worker.
        The executions will be stored in the database when the task completes if `execution`
        is specified.
        No result will be returned from this function.
        Instead, you can periodically check the status of the task in the database.

        Tasks may not execute immediately if the correct workers are not available.
        The task will be queued and executed when a worker becomes available.

        Parameters
        ----------
        definition
            A description of the information needed for this execution of the diagnostic
            This includes relative paths to the data files,
            which will be converted to absolute paths when being executed
        execution
            Result of the diagnostic execution
            This is a database object that contains the executions of the execution.
            If provided, it will be updated with the executions of the execution.
            This may happen asynchronously, so the executions may not be immediately available.
        """
        from climate_ref_celery.worker_tasks import handle_result  # noqa: PLC0415

        diagnostic = definition.diagnostic

        name = generate_task_name(diagnostic.provider, diagnostic)

        async_result = app.send_task(
            name,
            args=[definition, self.config.log_level],
            queue=diagnostic.provider.slug,
            link=handle_result.s(execution_id=execution.id).set(queue="celery") if execution else None,
        )
        logger.debug(f"Celery task {async_result.id} submitted")
        self._results.append(async_result)

    def join(self, timeout: float) -> None:
        """
        Wait for all executions to finish

        This will block until all executions have finished running,
        and display a progress bar while waiting.

        Any tasks still running after the timeout will continue to run in the background.

        Parameters
        ----------
        timeout
            Maximum time to wait in seconds before raising a TimeoutError

        Raises
        ------
        TimeoutError
            If all executions aren't completed within the specified timeout
        """
        start_time = time.time()
        refresh_time = 0.5  # Time to wait between checking for completed tasks in seconds

        results = self._results
        t = tqdm(total=len(results), desc="Waiting for executions to complete", unit="execution")

        try:
            while results:
                # Wait for a short time before checking for completed executions
                time.sleep(refresh_time)

                elapsed_time = time.time() - start_time

                if elapsed_time > timeout:
                    raise TimeoutError("Not all tasks completed within the specified timeout")

                # Iterate over a copy of the list and remove finished tasks
                for result in results[:]:
                    if result.ready():
                        t.update(n=1)
                        results.remove(result)
        finally:
            t.close()
