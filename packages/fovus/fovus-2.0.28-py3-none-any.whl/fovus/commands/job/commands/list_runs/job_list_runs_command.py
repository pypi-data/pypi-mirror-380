import json

import click
from typing_extensions import Union

from fovus.adapter.fovus_api_adapter import FovusApiAdapter
from fovus.util.util import Util


@click.command("list-runs")
@click.option("--job-id", type=str, help="The ID of the job to monitor or fetch runs from.")
@click.option("--limit", type=int, help="Maximum number of records to retrieve in this request.")
@click.option("--next_start_key", type=str, help="The key to start from for pagination of results.")
@click.option("--run-names", type=str, help="Comma-separated list of run names to filter the results.")
@click.option("--run-ids", type=str, help="Comma-separated list of run IDs to filter the results.")
def job_list_runs_command(job_id: Union[str, None], **list_runs_options):
    """
    List runs of a job.

    --job-id is required.

    This command retrieves the runs associated with a specific job ID.
    """
    print("Authenticating...")
    fovus_api_adapter = FovusApiAdapter()

    run_names = list_runs_options.get("run_names")
    run_ids = list_runs_options.get("run_ids")
    runs = fovus_api_adapter.get_list_runs(
        Util.remove_none_values_recursive(
            {
                "jobId": job_id,
                "limit": list_runs_options.get("limit", 50),
                "nextStartKey": list_runs_options.get("next_start_key", None),
                "workspaceId": fovus_api_adapter.workspace_id,
                "filterOptions": {
                    "runNames": run_names.split(",") if run_names else None,
                    "runIds": run_ids.split(",") if run_ids else None,
                },
            }
        )
    )

    print(json.dumps(runs.get("runList", []), indent=2))
