"""Provides lowest level, user-facing interface to server."""

from __future__ import annotations

import json
import os
import tempfile
import time
from typing import Callable, Literal, Optional, Union

from requests import HTTPError
from rich.progress import BarColumn, Progress, TaskProgressColumn, TextColumn, TimeElapsedColumn

from tidy3d.components.medium import AbstractCustomMedium
from tidy3d.components.mode.mode_solver import ModeSolver
from tidy3d.components.mode.simulation import ModeSimulation
from tidy3d.components.types.workflow import WorkflowDataType, WorkflowType
from tidy3d.exceptions import WebError
from tidy3d.log import get_logging_console, log
from tidy3d.plugins.smatrix.component_modelers.terminal import TerminalComponentModeler
from tidy3d.web.core.account import Account
from tidy3d.web.core.constants import (
    CM_DATA_HDF5_GZ,
    MODE_DATA_HDF5_GZ,
    MODE_FILE_HDF5_GZ,
    MODELER_FILE_HDF5_GZ,
    SIM_FILE_HDF5,
    SIM_FILE_HDF5_GZ,
    SIMULATION_DATA_HDF5_GZ,
    TaskId,
)
from tidy3d.web.core.environment import Env
from tidy3d.web.core.exceptions import WebNotFoundError
from tidy3d.web.core.http_util import get_version as _get_protocol_version
from tidy3d.web.core.http_util import http
from tidy3d.web.core.task_core import BatchTask, Folder, SimulationTask
from tidy3d.web.core.task_info import ChargeType, TaskInfo
from tidy3d.web.core.types import PayType

from .connect_util import REFRESH_TIME, get_grid_points_str, get_time_steps_str, wait_for_connection
from .tidy3d_stub import Tidy3dStub, Tidy3dStubData

# time between checking run status
RUN_REFRESH_TIME = 1.0

# file names when uploading to S3
SIM_FILE_JSON = "simulation.json"

# not all solvers are supported yet in GUI
GUI_SUPPORTED_TASK_TYPES = ["FDTD", "MODE_SOLVER", "HEAT", "RF"]

# if a solver is in beta stage, cost is subject to change
BETA_TASK_TYPES = ["HEAT", "EME", "HEAT_CHARGE", "VOLUME_MESH"]

# map task_type to solver name for display
SOLVER_NAME = {
    "FDTD": "FDTD",
    "MODE_SOLVER": "Mode",
    "MODE": "Mode",
    "EME": "EME",
    "HEAT": "Heat",
    "HEAT_CHARGE": "HeatCharge",
    "VOLUME_MESH": "VolumeMesher",
}

TERMINAL_ERRORS = {
    "validate_fail",
    "error",
    "diverged",
    "blocked",
    "aborting",
    "aborted",
}

RUN_STATUSES = [
    "draft",
    "preprocess",
    "validating",
    "validate",
    "running",
    "postprocess",
    "success",
]


def _get_url(task_id: str) -> str:
    """Get the URL for a task on our server."""
    return f"{Env.current.website_endpoint}/workbench?taskId={task_id}"


def _get_folder_url(folder_id: str) -> str:
    """Get the URL for a task folder on our server."""
    return f"{Env.current.website_endpoint}/folders/{folder_id}"


def _get_url_rf(resource_id: str) -> str:
    """Get the RF GUI URL for a modeler/batch group."""
    return f"{Env.current.website_endpoint}/rf?taskId={resource_id}"


def _is_modeler_batch(resource_id: str) -> bool:
    """Detect whether the given id corresponds to a modeler batch resource."""
    return BatchTask.is_batch(resource_id, batch_type="RF_SWEEP")


def _batch_detail(resource_id: str):
    return BatchTask(resource_id).detail(batch_type="RF_SWEEP")


def _task_dict_to_url_bullet_list(data_dict: dict) -> str:
    """
    Converts a dictionary into a string formatted as a bullet point list.

    Args:
      data_dict: The dictionary to convert.

    Returns:
      A string with each key-url/value pair as a bullet point.
    """
    # Use a list comprehension to format each key-value pair
    # and then join them together with newline characters.
    return "\n".join([f"- {key}: '{value}'" for key, value in data_dict.items()])


@wait_for_connection
def run(
    simulation: WorkflowType,
    task_name: Optional[str] = None,
    folder_name: str = "default",
    path: str = "simulation_data.hdf5",
    callback_url: Optional[str] = None,
    verbose: bool = True,
    progress_callback_upload: Optional[Callable[[float], None]] = None,
    progress_callback_download: Optional[Callable[[float], None]] = None,
    solver_version: Optional[str] = None,
    worker_group: Optional[str] = None,
    simulation_type: str = "tidy3d",
    parent_tasks: Optional[list[str]] = None,
    reduce_simulation: Literal["auto", True, False] = "auto",
    pay_type: Union[PayType, str] = PayType.AUTO,
    priority: Optional[int] = None,
) -> WorkflowDataType:
    """
    Submits a :class:`.Simulation` to server, starts running, monitors progress, downloads,
    and loads results as a :class:`.WorkflowDataType` object.

    Parameters
    ----------
    simulation : Union[:class:`.Simulation`, :class:`.HeatSimulation`, :class:`.EMESimulation`]
        Simulation to upload to server.
    task_name : Optional[str] = None
        Name of task. If not provided, a default name will be generated.
    folder_name : str = "default"
        Name of folder to store task on web UI.
    path : str = "simulation_data.hdf5"
        Path to download results file (.hdf5), including filename.
    callback_url : str = None
        Http PUT url to receive simulation finish event. The body content is a json file with
        fields ``{'id', 'status', 'name', 'workUnit', 'solverVersion'}``.
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.
    simulation_type : str = "tidy3d"
        Type of simulation being uploaded.
    progress_callback_upload : Callable[[float], None] = None
        Optional callback function called when uploading file with ``bytes_in_chunk`` as argument.
    progress_callback_download : Callable[[float], None] = None
        Optional callback function called when downloading file with ``bytes_in_chunk`` as argument.
    solver_version: str = None
        target solver version.
    worker_group: str = None
        worker group
    reduce_simulation : Literal["auto", True, False] = "auto"
        Whether to reduce structures in the simulation to the simulation domain only. Note: currently only implemented for the mode solver.
    pay_type: Union[PayType, str] = PayType.AUTO
        Which method to pay the simulation.
    priority: int = None
        Priority of the simulation in the Virtual GPU (vGPU) queue (1 = lowest, 10 = highest).
        It affects only simulations from vGPU licenses and does not impact simulations using FlexCredits.
    Returns
    -------
    Union[:class:`.SimulationData`, :class:`.HeatSimulationData`, :class:`.EMESimulationData`]
        Object containing solver results for the supplied simulation.

    Notes
    -----

        Submitting a simulation to our cloud server is very easily done by a simple web API call.

        .. code-block:: python

            sim_data = tidy3d.web.api.webapi.run(simulation, task_name='my_task', path='out/data.hdf5')

        The :meth:`tidy3d.web.api.webapi.run()` method shows the simulation progress by default.  When uploading a
        simulation to the server without running it, you can use the :meth:`tidy3d.web.api.webapi.monitor`,
        :meth:`tidy3d.web.api.container.Job.monitor`, or :meth:`tidy3d.web.api.container.Batch.monitor` methods to
        display the progress of your simulation(s).

    Examples
    --------

        To access the original :class:`.Simulation` object that created the simulation data you can use:

        .. code-block:: python

            # Run the simulation.
            sim_data = web.run(simulation, task_name='task_name', path='out/sim.hdf5')

            # Get a copy of the original simulation object.
            sim_copy = sim_data.simulation

    See Also
    --------

    :meth:`tidy3d.web.api.webapi.monitor`
        Print the real time task progress until completion.

    :meth:`tidy3d.web.api.container.Job.monitor`
        Monitor progress of running :class:`Job`.

    :meth:`tidy3d.web.api.container.Batch.monitor`
        Monitor progress of each of the running tasks.
    """
    task_id = upload(
        simulation=simulation,
        task_name=task_name,
        folder_name=folder_name,
        callback_url=callback_url,
        verbose=verbose,
        progress_callback=progress_callback_upload,
        simulation_type=simulation_type,
        parent_tasks=parent_tasks,
        solver_version=solver_version,
        reduce_simulation=reduce_simulation,
    )
    start(
        task_id,
        verbose=verbose,
        solver_version=solver_version,
        worker_group=worker_group,
        pay_type=pay_type,
        priority=priority,
    )
    monitor(task_id, verbose=verbose)
    data = load(
        task_id=task_id, path=path, verbose=verbose, progress_callback=progress_callback_download
    )
    if isinstance(simulation, ModeSolver):
        simulation._patch_data(data=data)
    return data


@wait_for_connection
def upload(
    simulation: WorkflowType,
    task_name: Optional[str] = None,
    folder_name: str = "default",
    callback_url: Optional[str] = None,
    verbose: bool = True,
    progress_callback: Optional[Callable[[float], None]] = None,
    simulation_type: str = "tidy3d",
    parent_tasks: Optional[list[str]] = None,
    source_required: bool = True,
    solver_version: Optional[str] = None,
    reduce_simulation: Literal["auto", True, False] = "auto",
) -> TaskId:
    """
    Upload simulation to server, but do not start running :class:`.Simulation`.

    Parameters
    ----------
    simulation : Union[:class:`.Simulation`, :class:`.HeatSimulation`, :class:`.EMESimulation`]
        Simulation to upload to server.
    task_name : Optional[str]
        Name of task. If not provided, a default name will be generated.
    folder_name : str
        Name of folder to store task on web UI
    callback_url : str = None
        Http PUT url to receive simulation finish event. The body content is a json file with
        fields ``{'id', 'status', 'name', 'workUnit', 'solverVersion'}``.
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.
    progress_callback : Callable[[float], None] = None
        Optional callback function called when uploading file with ``bytes_in_chunk`` as argument.
    simulation_type : str = "tidy3d"
        Type of simulation being uploaded.
    parent_tasks : List[str]
        List of related task ids.
    source_required: bool = True
        If ``True``, simulations without sources will raise an error before being uploaded.
    solver_version: str = None
        target solver version.
    reduce_simulation: Literal["auto", True, False] = "auto"
        Whether to reduce structures in the simulation to the simulation domain only. Note: currently only implemented for the mode solver.

    Returns
    -------
    str
        Unique identifier of task on server.


    Notes
    -----

        Once you've created a ``job`` object using :class:`tidy3d.web.api.container.Job`, you can upload it to our servers with:

        .. code-block:: python

            web.upload(simulation, task_name="task_name", verbose=verbose)

        It will not run until you explicitly tell it to do so with :meth:`tidy3d.web.api.webapi.start`.

    """
    console = get_logging_console() if verbose else None

    if isinstance(simulation, (ModeSolver, ModeSimulation)):
        simulation = get_reduced_simulation(simulation, reduce_simulation)

    stub = Tidy3dStub(simulation=simulation)
    stub.validate_pre_upload(source_required=source_required)
    log.debug("Creating task.")

    if task_name is None:
        task_name = stub.get_default_task_name()

    task_type = stub.get_type()
    # Component modeler compatibility: map to RF task type
    port_name_list = None
    if task_type in ("COMPONENT_MODELER", "TERMINAL_COMPONENT_MODELER"):
        task_type = "RF"
        port_name_list = tuple(simulation.sim_dict.keys())

    task = SimulationTask.create(
        task_type,
        task_name,
        folder_name,
        callback_url,
        simulation_type,
        parent_tasks,
        "Gz",
        port_name_list=port_name_list,
    )

    if task_type == "RF":
        # Prefer the group id if present in the creation response; avoid extra GET.
        group_id = getattr(task, "groupId", None) or getattr(task, "group_id", None)
        if not group_id:
            try:
                detail_task = SimulationTask.get(task.task_id, verbose=False)
                group_id = getattr(detail_task, "groupId", None) or getattr(
                    detail_task, "group_id", None
                )
            except Exception:
                group_id = None
        # Prefer returning batch/group id for downstream batch endpoints
        batch_id = getattr(task, "batchId", None) or getattr(task, "batch_id", None)
        resource_id = batch_id or task.task_id
    else:
        group_id = None
        resource_id = task.task_id

    if verbose:
        console.log(
            f"Created task '{task_name}' with resource_id '{resource_id}' and task_type '{task_type}'."
        )
        if task_type in BETA_TASK_TYPES:
            solver_name = SOLVER_NAME[task_type]
            console.log(
                f"Tidy3D's {solver_name} solver is currently in the beta stage. "
                f"Cost of {solver_name} simulations is subject to change in the future."
            )
        if task_type in GUI_SUPPORTED_TASK_TYPES:
            if (task_type == "RF") and (isinstance(simulation, TerminalComponentModeler)):
                url = _get_url_rf(group_id or resource_id)
                folder_url = _get_folder_url(task.folder_id)
                console.log(f"View task using web UI at [link={url}]'{url}'[/link].")
                console.log(f"Task folder: [link={folder_url}]'{task.folder_name}'[/link].")
            else:
                url = _get_url(resource_id)
                folder_url = _get_folder_url(task.folder_id)
                console.log(f"View task using web UI at [link={url}]'{url}'[/link].")
                console.log(f"Task folder: [link={folder_url}]'{task.folder_name}'[/link].")

    remote_sim_file = SIM_FILE_HDF5_GZ
    if task_type == "MODE_SOLVER":
        remote_sim_file = MODE_FILE_HDF5_GZ
    elif task_type == "RF":
        remote_sim_file = MODELER_FILE_HDF5_GZ

    task.upload_simulation(
        stub=stub,
        verbose=verbose,
        progress_callback=progress_callback,
        remote_sim_file=remote_sim_file,
    )

    if task_type == "RF":
        split_path = "tidy3d/projects/component-modeler-split"
        payload = {
            "batchType": "RF_SWEEP",
            "batchId": resource_id,
            "fileName": "modeler.hdf5.gz",
            "protocolVersion": _get_protocol_version(),
        }
        resp = http.post(split_path, payload)
        if verbose:
            console = get_logging_console()
            console.log(
                f"Child simulation subtasks are being uploaded to \n{_task_dict_to_url_bullet_list(resp)}"
            )
        # split (modeler-specific)
        batch = BatchTask(resource_id)
        # Kick off server-side validation for the RF batch.
        batch.check(solver_version=solver_version, batch_type="RF_SWEEP")
        if verbose:
            # Validation phase
            console.log("Validating component modeler and subtask simulations...")

    estimate_cost(task_id=resource_id, solver_version=solver_version, verbose=verbose)

    task.validate_post_upload(parent_tasks=parent_tasks)

    # log the url for the task in the web UI
    log.debug(f"{Env.current.website_endpoint}/folders/{task.folder_id}/tasks/{resource_id}")
    return resource_id


def get_reduced_simulation(simulation, reduce_simulation):
    """
    Adjust the given simulation object based on the reduce_simulation parameter. Currently only
    implemented for the mode solver.

    Parameters
    ----------
    simulation : Simulation
        The simulation object to be potentially reduced.
    reduce_simulation : Literal["auto", True, False]
        Determines whether to reduce the simulation. If "auto", the function will decide based on
        the presence of custom mediums in the simulation.

    Returns
    -------
    Simulation
        The potentially reduced simulation object.
    """

    """
    TODO: This only works for the mode solver, which is also why `simulation.simulation.scene` is
    used below. After refactor to use the new ModeSimulation, it should be possible to put the call
    to this function outside of the MODE_SOLVER check in the upload function. We could implement
    dummy `reduced_simulation_copy` methods for the other solvers or also implement reductions
    there. Note that if we do the latter we may want to also modify the warning below to only
    happen if there are custom media *and* they extend beyond the simulation domain.
    """
    if reduce_simulation == "auto":
        if isinstance(simulation, ModeSimulation):
            sim_mediums = simulation.scene.mediums
        else:
            sim_mediums = simulation.simulation.scene.mediums
        contains_custom = any(isinstance(med, AbstractCustomMedium) for med in sim_mediums)
        reduce_simulation = contains_custom

        if reduce_simulation:
            log.warning(
                f"The {type(simulation)} object contains custom mediums. It will be "
                "automatically restricted to the solver domain to reduce data for uploading. "
                "To force uploading the original object use 'reduce_simulation=False'."
                " Setting 'reduce_simulation=True' will force simulation reduction in all cases and"
                " silence this warning."
            )
    if reduce_simulation:
        return simulation.reduced_simulation_copy
    return simulation


@wait_for_connection
def get_info(task_id: TaskId, verbose: bool = True) -> TaskInfo:
    """Return information about a task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.
    Returns
    -------
    :class:`TaskInfo`
        Object containing information about status, size, credits of task.
    """
    task = SimulationTask.get(task_id, verbose)
    if not task:
        raise ValueError("Task not found.")
    return TaskInfo(**{"taskId": task.task_id, "taskType": task.task_type, **task.dict()})


@wait_for_connection
def start(
    task_id: TaskId,
    verbose: bool = True,
    solver_version: Optional[str] = None,
    worker_group: Optional[str] = None,
    pay_type: Union[PayType, str] = PayType.AUTO,
    priority: Optional[int] = None,
) -> None:
    """Start running the simulation associated with task.

    Parameters
    ----------

    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    verbose : bool = True
        If ``True``, will print log messages, otherwise, will run silently.
    solver_version: str = None
        target solver version.
    worker_group: str = None
        worker group
    pay_type: Union[PayType, str] = PayType.AUTO
        Which method to pay the simulation
    priority: int = None
        Priority of the simulation in the Virtual GPU (vGPU) queue (1 = lowest, 10 = highest).
        It affects only simulations from vGPU licenses and does not impact simulations using FlexCredits.
    Note
    ----
    To monitor progress, can call :meth:`monitor` after starting simulation.
    """

    console = get_logging_console() if verbose else None

    # Component modeler batch path: hide split/check/submit
    if _is_modeler_batch(task_id):
        # split (modeler-specific)
        batch = BatchTask(task_id)
        detail = batch.wait_for_validate(batch_type="RF_SWEEP")
        status = detail.totalStatus
        status_str = status.value
        if status_str in ("validate_success", "validate_warn"):
            if verbose:
                console.log("Component modeler batch validation has been successful.")
        if status_str not in ("validate_success", "validate_warn"):
            raise WebError(f"Batch task {task_id} is blocked: {status_str}")
        # Submit batch to start runs after validation
        batch.submit(
            solver_version=solver_version, batch_type="RF_SWEEP", worker_group=worker_group
        )
        return

    if priority is not None and (priority < 1 or priority > 10):
        raise ValueError("Priority must be between '1' and '10' if specified.")
    task = SimulationTask.get(task_id)
    if not task:
        raise ValueError("Task not found.")
    task.submit(
        solver_version=solver_version,
        worker_group=worker_group,
        pay_type=pay_type,
        priority=priority,
    )


@wait_for_connection
def get_run_info(task_id: TaskId) -> tuple[Optional[float], Optional[float]]:
    """Gets the % done and field_decay for a running task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.

    Returns
    -------
    perc_done : float
        Percentage of run done (in terms of max number of time steps).
        Is ``None`` if run info not available.
    field_decay : float
        Average field intensity normalized to max value (1.0).
        Is ``None`` if run info not available.
    """
    task = SimulationTask(taskId=task_id)
    return task.get_running_info()


def get_status(task_id) -> str:
    """Get the status of a task. Raises an error if status is "error".

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    """
    task_info = get_info(task_id)
    status = task_info.status
    if status == "visualize":
        return "success"
    if status == "error":
        try:
            # Try to obtain the error message
            task = SimulationTask(taskId=task_id)
            with tempfile.NamedTemporaryFile(suffix=".json") as tmp_file:
                task.get_error_json(to_file=tmp_file.name)
                with open(tmp_file.name) as f:
                    error_content = json.load(f)
                    error_msg = error_content["msg"]
        except Exception:
            # If the error message could not be obtained, raise a generic error message
            error_msg = "Error message could not be obtained, please contact customer support."

        raise WebError(f"Error running task {task_id}! {error_msg}")
    return status


def monitor(task_id: TaskId, verbose: bool = True, worker_group: Optional[str] = None) -> None:
    """
    Print the real time task progress until completion.

    Notes
    -----

        To monitor the simulation's progress and wait for its completion, use:

        .. code-block:: python

            tidy3d.web.api.webapi.monitor(job.task_id, verbose=verbose).

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.

    Note
    ----
    To load results when finished, may call :meth:`load`.
    """

    # Batch/modeler monitoring path
    if _is_modeler_batch(task_id):
        _monitor_modeler_batch(task_id, verbose=verbose, worker_group=worker_group)
        return

    console = get_logging_console() if verbose else None

    task_info = get_info(task_id)

    task_name = task_info.taskName

    task_type = task_info.taskType

    break_statuses = ("success", "error", "diverged", "deleted", "draft", "abort", "aborted")

    def get_estimated_cost() -> float:
        """Get estimated cost, if None, is not ready."""
        task_info = get_info(task_id)
        block_info = task_info.taskBlockInfo
        if block_info and block_info.chargeType == ChargeType.FREE:
            est_flex_unit = 0
            grid_points = block_info.maxGridPoints
            time_steps = block_info.maxTimeSteps
            grid_points_str = get_grid_points_str(grid_points)
            time_steps_str = get_time_steps_str(time_steps)
            console.log(
                f"You are running this simulation for FREE. Your current plan allows"
                f" up to {block_info.maxFreeCount} free non-concurrent simulations per"
                f" day (under {grid_points_str} grid points and {time_steps_str}"
                f" time steps)"
            )
        else:
            est_flex_unit = task_info.estFlexUnit
        return est_flex_unit

    def monitor_preprocess() -> None:
        """Periodically check the status."""
        status = get_status(task_id)
        while status not in break_statuses and status != "running":
            new_status = get_status(task_id)
            if new_status != status:
                status = new_status
                if verbose and status != "running":
                    console.log(f"status = {status}")
            time.sleep(REFRESH_TIME)

    status = get_status(task_id)

    if verbose:
        console.log(f"status = {status}")

    # already done
    if status in break_statuses:
        return

    # preprocessing
    if verbose:
        console.log(
            "To cancel the simulation, use 'web.abort(task_id)' or 'web.delete(task_id)' "
            "or abort/delete the task in the web "
            "UI. Terminating the Python script will not stop the job running on the cloud."
        )
        with console.status(f"[bold green]Waiting for '{task_name}'...", spinner="runner"):
            monitor_preprocess()
    else:
        monitor_preprocess()

    # if the estimated cost is ready, print it
    if verbose:
        get_estimated_cost()
        console.log("starting up solver")

    # while running but before the percentage done is available, keep waiting
    while get_run_info(task_id)[0] is None and get_status(task_id) == "running":
        time.sleep(REFRESH_TIME)

    # while running but percentage done is available
    if verbose:
        # verbose case, update progressbar
        console.log("running solver")
        if task_type == "FDTD":
            with Progress(console=console) as progress:
                pbar_pd = progress.add_task("% done", total=100)
                perc_done, _ = get_run_info(task_id)

                while (
                    perc_done is not None and perc_done < 100 and get_status(task_id) == "running"
                ):
                    perc_done, field_decay = get_run_info(task_id)
                    new_description = f"solver progress (field decay = {field_decay:.2e})"
                    progress.update(pbar_pd, completed=perc_done, description=new_description)
                    time.sleep(RUN_REFRESH_TIME)

                perc_done, field_decay = get_run_info(task_id)
                if perc_done is not None and perc_done < 100 and field_decay > 0:
                    console.log(f"early shutoff detected at {perc_done:1.0f}%, exiting.")

                new_description = f"solver progress (field decay = {field_decay:.2e})"
                progress.update(pbar_pd, completed=100, refresh=True, description=new_description)
        elif task_type == "EME":
            with Progress(console=console) as progress:
                pbar_pd = progress.add_task("% done", total=100)
                perc_done, _ = get_run_info(task_id)

                while (
                    perc_done is not None and perc_done < 100 and get_status(task_id) == "running"
                ):
                    perc_done, _ = get_run_info(task_id)
                    new_description = "solver progress"
                    progress.update(pbar_pd, completed=perc_done, description=new_description)
                    time.sleep(RUN_REFRESH_TIME)

                perc_done, _ = get_run_info(task_id)
                new_description = "solver progress"
                progress.update(pbar_pd, completed=100, refresh=True, description=new_description)
        else:
            while get_status(task_id) == "running":
                perc_done, _ = get_run_info(task_id)
                time.sleep(RUN_REFRESH_TIME)

    else:
        # non-verbose case, just keep checking until status is not running or perc_done >= 100
        perc_done, _ = get_run_info(task_id)
        while perc_done is not None and perc_done < 100 and get_status(task_id) == "running":
            perc_done, field_decay = get_run_info(task_id)
            time.sleep(RUN_REFRESH_TIME)

    # post processing
    if verbose:
        status = get_status(task_id)
        if status != "running":
            console.log(f"status = {status}")

        with console.status(f"[bold green]Finishing '{task_name}'...", spinner="runner"):
            while status not in break_statuses:
                new_status = get_status(task_id)
                if new_status != status:
                    status = new_status
                    console.log(f"status = {status}")
                time.sleep(REFRESH_TIME)

        if task_type in GUI_SUPPORTED_TASK_TYPES:
            url = _get_url(task_id)
            console.log(f"View simulation result at [blue underline][link={url}]'{url}'[/link].")
    else:
        while get_status(task_id) not in break_statuses:
            time.sleep(REFRESH_TIME)


@wait_for_connection
def abort(task_id: TaskId):
    """Abort server-side data associated with task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.

    Returns
    -------
    TaskInfo
        Object containing information about status, size, credits of task.
    """
    console = get_logging_console()
    try:
        task = SimulationTask.get(task_id, verbose=False)
        if task:
            task.abort()
            url = _get_url(task.task_id)
            console.log(
                f"Task is aborting. View task using web UI at [link={url}]'{url}'[/link] to check the result."
            )
            return TaskInfo(**{"taskId": task.task_id, **task.dict()})
    except WebNotFoundError:
        pass  # Task not found, might be a batch task

    is_batch = BatchTask.is_batch(task_id, batch_type="RF_SWEEP")
    if is_batch:
        url = _get_url_rf(task_id)
        console.log(
            f"Batch task abortion is not yet supported, contact customer support."
            f" View task using web UI at [link={url}]'{url}'[/link]."
        )
        return

    console.log("Task ID cannot be found to be aborted.")
    return


@wait_for_connection
def download(
    task_id: TaskId,
    path: str = "simulation_data.hdf5",
    verbose: bool = True,
    progress_callback: Optional[Callable[[float], None]] = None,
) -> None:
    """Download results of task to file.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    path : str = "simulation_data.hdf5"
        Download path to .hdf5 data file (including filename).
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.
    progress_callback : Callable[[float], None] = None
        Optional callback function called when downloading file with ``bytes_in_chunk`` as argument.

    """
    # Component modeler batch download path
    if _is_modeler_batch(task_id):
        # Use a more descriptive default filename for component modeler downloads.
        # If the caller left the default as 'simulation_data.hdf5', prefer 'cm_data.hdf5'.
        if os.path.basename(path) == "simulation_data.hdf5":
            base_dir = os.path.dirname(path) or "."
            path = os.path.join(base_dir, "cm_data.hdf5")

        def _download_cm() -> bool:
            try:
                BatchTask(task_id).get_data_hdf5(
                    remote_data_file_gz=CM_DATA_HDF5_GZ,
                    to_file=path,
                    verbose=verbose,
                    progress_callback=progress_callback,
                )
                return True
            except Exception:
                return False

        if not _download_cm():
            BatchTask(task_id).postprocess(batch_type="RF_SWEEP")
            # wait for postprocess to finish
            while True:
                resp = BatchTask(task_id).detail(batch_type="RF_SWEEP")
                total = resp.totalTask or 0
                post_succ = resp.postprocessSuccess or 0
                status = resp.totalStatus
                status_str = status.value
                if status_str in {"error", "diverged", "blocked", "aborted", "aborting"}:
                    raise WebError(
                        f"Batch task {task_id} failed during postprocess: {status_str}"
                    ) from None
                if total > 0 and post_succ >= total:
                    break
                time.sleep(REFRESH_TIME)
            if not _download_cm():
                raise WebError("Failed to download 'cm_data' after postprocess completion.")
        return

    # Regular single-task download
    task_info = get_info(task_id)
    task_type = task_info.taskType

    remote_data_file = SIMULATION_DATA_HDF5_GZ
    if task_type == "MODE_SOLVER":
        remote_data_file = MODE_DATA_HDF5_GZ

    task = SimulationTask(taskId=task_id)
    task.get_sim_data_hdf5(
        path,
        verbose=verbose,
        progress_callback=progress_callback,
        remote_data_file=remote_data_file,
    )


@wait_for_connection
def download_json(task_id: TaskId, path: str = SIM_FILE_JSON, verbose: bool = True) -> None:
    """Download the ``.json`` file associated with the :class:`.Simulation` of a given task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    path : str = "simulation.json"
        Download path to .json file of simulation (including filename).
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.

    """

    task = SimulationTask(taskId=task_id)
    task.get_simulation_json(path, verbose=verbose)


@wait_for_connection
def delete_old(days_old: int, folder_name: str = "default") -> int:
    """Remove folder contents older than ``days_old``."""
    folder = Folder.get(folder_name, create=True)
    return folder.delete_old(days_old)


@wait_for_connection
def load_simulation(
    task_id: TaskId, path: str = SIM_FILE_JSON, verbose: bool = True
) -> WorkflowType:
    """Download the ``.json`` file of a task and load the associated simulation.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    path : str = "simulation.json"
        Download path to .json file of simulation (including filename).
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.

    Returns
    -------
    Union[:class:`.Simulation`, :class:`.HeatSimulation`, :class:`.EMESimulation`]
        Simulation loaded from downloaded json file.
    """

    task = SimulationTask.get(task_id)
    task.get_simulation_json(path, verbose=verbose)
    return Tidy3dStub.from_file(path)


@wait_for_connection
def download_log(
    task_id: TaskId,
    path: str = "tidy3d.log",
    verbose: bool = True,
    progress_callback: Optional[Callable[[float], None]] = None,
) -> None:
    """Download the tidy3d log file associated with a task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    path : str = "tidy3d.log"
        Download path to log file (including filename).
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.
    progress_callback : Callable[[float], None] = None
        Optional callback function called when downloading file with ``bytes_in_chunk`` as argument.

    Note
    ----
    To load downloaded results into data, call :meth:`load` with option ``replace_existing=False``.
    """
    task = SimulationTask(taskId=task_id)
    task.get_log(path, verbose=verbose, progress_callback=progress_callback)


@wait_for_connection
def load(
    task_id: TaskId,
    path: str = "simulation_data.hdf5",
    replace_existing: bool = True,
    verbose: bool = True,
    progress_callback: Optional[Callable[[float], None]] = None,
    lazy: bool = False,
) -> WorkflowDataType:
    """
    Download and Load simulation results into :class:`.SimulationData` object.

    Notes
    -----

        After the simulation is complete, you can load the results into a :class:`.SimulationData` object by its
        ``task_id`` using:

        .. code-block:: python

            sim_data = web.load(task_id, path="outt/sim.hdf5", verbose=verbose)

        The :meth:`tidy3d.web.api.webapi.load` method is very convenient to load and postprocess results from simulations
        created using Tidy3D GUI.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    path : str
        Download path to .hdf5 data file (including filename).
    replace_existing : bool = True
        Downloads the data even if path exists (overwriting the existing).
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.
    progress_callback : Callable[[float], None] = None
        Optional callback function called when downloading file with ``bytes_in_chunk`` as argument.
    lazy : bool = False
        Whether to load the actual data (``lazy=False``) or return a proxy that loads
        the data when accessed (``lazy=True``).

    Returns
    -------
    Union[:class:`.SimulationData`, :class:`.HeatSimulationData`, :class:`.EMESimulationData`]
        Object containing simulation data.
    """
    # For component modeler batches, default to a clearer filename if the default was used.
    if _is_modeler_batch(task_id) and os.path.basename(path) == "simulation_data.hdf5":
        base_dir = os.path.dirname(path) or "."
        path = os.path.join(base_dir, "cm_data.hdf5")

    if not os.path.exists(path) or replace_existing:
        download(task_id=task_id, path=path, verbose=verbose, progress_callback=progress_callback)

    if verbose:
        console = get_logging_console()
        if _is_modeler_batch(task_id):
            console.log(f"loading component modeler data from {path}")
        else:
            console.log(f"loading simulation from {path}")

    stub_data = Tidy3dStubData.postprocess(path, lazy=lazy)
    return stub_data


def _monitor_modeler_batch(
    batch_id: str,
    verbose: bool = True,
    max_detail_tasks: int = 20,
    worker_group: Optional[str] = None,
) -> None:
    """Monitor modeler batch progress with aggregate and per-task views."""
    console = get_logging_console() if verbose else None

    def _status_to_stage(status: str) -> tuple[str, int]:
        s = (status or "").lower()
        # Map a broader set of statuses to monotonic stages for progress bars
        if s in ("draft", "created"):
            return ("draft", 0)
        if s in ("queue", "queued"):
            return ("queued", 1)
        if s in ("preprocess",):
            return ("preprocess", 1)
        if s in ("validating",):
            return ("validating", 2)
        if s in ("validate_success", "validate_warn"):
            return ("validate", 3)
        if s in ("running",):
            return ("running", 4)
        if s in ("postprocess",):
            return ("postprocess", 5)
        if s in ("run_success", "success"):
            return ("success", 6)
        # Unknown statuses map to earliest stage to avoid showing 100% prematurely
        return (s or "unknown", 0)

    detail = _batch_detail(batch_id)
    name = detail.name or "modeler_batch"
    group_id = detail.groupId

    header = f"Subtasks status - {name}"
    if group_id:
        header += f"\nGroup ID: '{group_id}'"
    if console is not None:
        console.log(header)

    # Non-verbose path: poll without progress bars then return
    if not verbose:
        # Run phase
        while True:
            d = _batch_detail(batch_id)
            s = d.totalStatus.value
            total = d.totalTask or 0
            r = d.runSuccess or 0
            if s in TERMINAL_ERRORS:
                raise WebError(f"Batch {batch_id} terminated: {s}")
            if total and r >= total:
                break
            time.sleep(REFRESH_TIME)
        # Postprocess phase
        BatchTask(batch_id).postprocess(batch_type="RF_SWEEP", worker_group=worker_group)
        while True:
            d = _batch_detail(batch_id)
            postprocess_status = d.postprocessStatus
            if postprocess_status == "success":
                break
            elif postprocess_status in TERMINAL_ERRORS:
                raise WebError(
                    f"Batch {batch_id} terminated. Please contact customer support and provide this Component Modeler batch ID: '{batch_id}'"
                )
            time.sleep(REFRESH_TIME)
        return

    progress_columns = (
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=25),
        TaskProgressColumn(),
        TimeElapsedColumn(),
    )
    with Progress(*progress_columns, console=console, transient=False) as progress:
        # Phase: Run (aggregate + per-task)
        p_run = progress.add_task("Run Total", total=1.0)
        task_bars: dict[str, int] = {}

        while True:
            detail = _batch_detail(batch_id)
            status = detail.totalStatus.value
            total = detail.totalTask or 0
            r = detail.runSuccess or 0

            # Create per-task bars as soon as tasks appear
            if total and total <= max_detail_tasks and detail.tasks:
                name_to_task = {(t.taskName or t.taskId): t for t in (detail.tasks or [])}
                for name, t in name_to_task.items():
                    if name not in task_bars:
                        tstatus = (t.status or "draft").lower()
                        _, idx = _status_to_stage(tstatus)
                        pbar = progress.add_task(
                            f"  {name}",
                            total=len(RUN_STATUSES) - 1,
                            completed=min(idx, len(RUN_STATUSES) - 1),
                        )
                        task_bars[name] = pbar

            # Aggregate run progress: average stage fraction across tasks
            if detail.tasks:
                acc = 0.0
                n_members = 0
                for t in detail.tasks or []:
                    n_members += 1
                    tstatus = (t.status or "draft").lower()
                    _, idx = _status_to_stage(tstatus)
                    acc += max(0.0, min(1.0, idx / 6.0))
                run_frac = (acc / float(n_members)) if n_members else 0.0
            else:
                run_frac = (r / total) if total else 0.0
            progress.update(p_run, completed=run_frac)

            # Update per-task bars
            if task_bars and detail.tasks:
                name_to_task = {(t.taskName or t.taskId): t for t in (detail.tasks or [])}
                for tname, pbar in task_bars.items():
                    t = name_to_task.get(tname)
                    if not t:
                        continue
                    tstatus = (t.status or "draft").lower()
                    _, idx = _status_to_stage(tstatus)
                    completed = min(idx, 6)
                    desc = f"  {tname} [{tstatus or 'draft'}]"
                    progress.update(pbar, completed=completed, description=desc, refresh=False)

            if total and r >= total:
                break
            if status in TERMINAL_ERRORS:
                raise WebError(f"Batch {batch_id} terminated: {status}")
            progress.refresh()
            time.sleep(REFRESH_TIME)

        # Phase: Postprocess
        BatchTask(batch_id).postprocess(batch_type="RF_SWEEP", worker_group=worker_group)
        p_post = progress.add_task("Postprocess", total=1.0)
        while True:
            detail = _batch_detail(batch_id)
            postprocess_status = detail.postprocessStatus
            if postprocess_status == "success":
                progress.update(p_post, completed=1.0)
                progress.refresh()
                break
            elif postprocess_status == "queued":
                progress.update(p_post, completed=0.22)
            elif postprocess_status == "preprocess":
                progress.update(p_post, completed=0.33)
            elif postprocess_status == "running":
                progress.update(p_post, completed=0.55)
            elif postprocess_status in TERMINAL_ERRORS:
                raise WebError(
                    f"Batch {batch_id} terminated. Please contact customer support and provide this Component Modeler batch ID: '{batch_id}'"
                )
            progress.refresh()
            time.sleep(REFRESH_TIME)

        if console is not None:
            console.log("Modeler has finished running successfully.")
            real_cost(batch_id, verbose=verbose)


@wait_for_connection
def delete(task_id: TaskId, versions: bool = False) -> TaskInfo:
    """Delete server-side data associated with task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    versions : bool = False
        If ``True``, delete all versions of the task in the task group. Otherwise, delete only the version associated with the current task ID.

    Returns
    -------
    :class:`.TaskInfo`
        Object containing information about status, size, credits of task.

    """
    if not task_id:
        raise ValueError("Task id not found.")
    task = SimulationTask.get(task_id, verbose=False)
    task.delete(versions)
    return TaskInfo(**{"taskId": task.task_id, **task.dict()})


@wait_for_connection
def download_simulation(
    task_id: TaskId,
    path: str = SIM_FILE_HDF5,
    verbose: bool = True,
    progress_callback: Optional[Callable[[float], None]] = None,
) -> None:
    """Download the ``.hdf5`` file associated with the :class:`.Simulation` of a given task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    path : str = "simulation.hdf5"
        Download path to .hdf5 file of simulation (including filename).
    verbose : bool = True
        If ``True``, will print progressbars and status, otherwise, will run silently.
    progress_callback : Callable[[float], None] = None
        Optional callback function called when downloading file with ``bytes_in_chunk`` as argument.

    """
    task_info = get_info(task_id)
    task_type = task_info.taskType

    remote_sim_file = SIM_FILE_HDF5_GZ
    if task_type == "MODE_SOLVER":
        remote_sim_file = MODE_FILE_HDF5_GZ

    task = SimulationTask(taskId=task_id)
    task.get_simulation_hdf5(
        path, verbose=verbose, progress_callback=progress_callback, remote_sim_file=remote_sim_file
    )


@wait_for_connection
def get_tasks(
    num_tasks: Optional[int] = None, order: Literal["new", "old"] = "new", folder: str = "default"
) -> list[dict]:
    """Get a list with the metadata of the last ``num_tasks`` tasks.

    Parameters
    ----------
    num_tasks : int = None
        The number of tasks to return, or, if ``None``, return all.
    order : Literal["new", "old"] = "new"
        Return the tasks in order of newest-first or oldest-first.
    folder: str = "default"
        Folder from which to get the tasks.

    Returns
    -------
    List[Dict]
        List of dictionaries storing the information for each of the tasks last ``num_tasks`` tasks.
    """
    folder = Folder.get(folder, create=True)
    tasks = folder.list_tasks()
    if not tasks:
        return []
    if order == "new":
        tasks = sorted(tasks, key=lambda t: t.created_at, reverse=True)
    elif order == "old":
        tasks = sorted(tasks, key=lambda t: t.created_at)
    if num_tasks is not None:
        tasks = tasks[:num_tasks]
    return [task.dict() for task in tasks]


@wait_for_connection
def estimate_cost(
    task_id: str, verbose: bool = True, solver_version: Optional[str] = None
) -> float:
    """Compute the maximum FlexCredit charge for a given task.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    verbose : bool = True
        Whether to log the cost and helpful messages.
    solver_version : str = None
        Target solver version.

    Returns
    -------
    float
        Estimated maximum cost for :class:`.Simulation` associated with given ``task_id``.

    Note
    ----
    Cost is calculated assuming the simulation runs for
    the full ``run_time``. If early shut-off is triggered, the cost is adjusted proportionately.
    A minimum simulation cost may also apply, which depends on the task details.

    Notes
    -----

        We can get the cost estimate of running the task before actually running it. This prevents us from
        accidentally running large jobs that we set up by mistake. The estimated cost is the maximum cost
        corresponding to running all the time steps.

    Examples
    --------

    Basic example:

    .. code-block:: python

        # initializes job, puts task on server (but doesn't run it)
        job = web.Job(simulation=sim, task_name="job", verbose=verbose)

        # estimate the maximum cost
        estimated_cost = web.estimate_cost(job.task_id)

        print(f'The estimated maximum cost is {estimated_cost:.3f} Flex Credits.')

    """
    if not isinstance(task_id, str):
        raise ValueError(
            f"Task ID: {task_id} is not a string. You can get it using 'web.upload(<WorkflowType>)'."
        )

    console = get_logging_console() if verbose else None

    if _is_modeler_batch(task_id):
        d = _batch_detail(task_id)
        status = d.totalStatus.value

        # Wait for a termination status
        while status not in ["validate_success", "success", "error", "failed"]:
            time.sleep(REFRESH_TIME)
            d = _batch_detail(task_id)
            status = d.totalStatus.value

            if status in ["validate_success", "success"]:
                est_flex_unit = _batch_detail(task_id).estFlexUnit
                if verbose:
                    console.log(
                        f"Maximum FlexCredit cost: {est_flex_unit:1.3f}. Minimum cost depends on "
                        "task execution details. Use 'web.real_cost(task_id)' to get the billed FlexCredit "
                        "cost after a simulation run."
                    )
                return est_flex_unit
            elif status in TERMINAL_ERRORS:
                log.error(f"The ComponentModeler '{task_id}' has failed: {status}")

                if status == "validate_fail":
                    assert d.validateErrors is not None
                    for key, error in d.validateErrors.items():
                        # I don't like this ideally but would like to control the endpoint to make this better
                        error_dict = json.loads(error)
                        validation_error = error_dict["validation_error"]
                        log.error(
                            f"Subtask '{key}' has failed to validate:"
                            f" \n {validation_error} \n "
                            f"Fix your component modeler configuration. "
                            f"Generate subtask simulations locally using `ComponentModelerType.sim_dict`."
                        )
                break
    else:
        task = SimulationTask.get(task_id)

        if not task:
            raise ValueError("Task not found.")

        task.estimate_cost(solver_version=solver_version)
        task_info = get_info(task_id)
        status = task_info.metadataStatus

        # Wait for a termination status
        while status not in ["processed", "success", "error", "failed"]:
            time.sleep(REFRESH_TIME)
            task_info = get_info(task_id)
            status = task_info.metadataStatus

        if status in ["processed", "success"]:
            if verbose:
                console.log(
                    f"Estimated FlexCredit cost: {task_info.estFlexUnit:1.3f}. Minimum cost depends on "
                    "task execution details. Use 'web.real_cost(task_id)' to get the billed FlexCredit "
                    "cost after a simulation run."
                )
                fc_mode = task_info.estFlexCreditMode
                fc_post = task_info.estFlexCreditPostProcess
                if fc_mode:
                    console.log(f"  {fc_mode:1.3f} FlexCredit of the total cost from mode solves.")
                if fc_post:
                    console.log(
                        f"  {fc_post:1.3f} FlexCredit of the total cost from post-processing."
                    )
            return task_info.estFlexUnit

        # Something went wrong
        raise WebError("Could not get estimated cost!")


@wait_for_connection
def real_cost(task_id: str, verbose=True) -> float | None:
    """Get the billed cost for given task after it has been run.

    Parameters
    ----------
    task_id : str
        Unique identifier of task on server.  Returned by :meth:`upload`.
    verbose : bool = True
        Whether to log the cost and helpful messages.

    Returns
    -------
    float
        The flex credit cost that was billed for the given ``task_id``.

    Note
    ----
        The billed cost may not be immediately available when the task status is set to ``success``,
        but should be available shortly after.

    Examples
    --------

    To obtain the cost of a simulation, you can use the function ``tidy3d.web.real_cost(task_id)``. In the example
    below, a job is created, and its cost is estimated. After running the simulation, the real cost can be obtained.

    .. code-block:: python

        import time

        # initializes job, puts task on server (but doesn't run it)
        job = web.Job(simulation=sim, task_name="job", verbose=verbose)

        # estimate the maximum cost
        estimated_cost = web.estimate_cost(job.task_id)

        print(f'The estimated maximum cost is {estimated_cost:.3f} Flex Credits.')

        # Runs the simulation.
        sim_data = job.run(path="data/sim_data.hdf5")

        time.sleep(5)

        # Get the billed FlexCredit cost after a simulation run.
        cost = web.real_cost(job.task_id)
    """
    if not isinstance(task_id, str):
        raise ValueError(
            f"Task ID: {task_id} is not a string. You can get it using 'web.upload(<WorkflowType>)'."
        )

    console = get_logging_console() if verbose else None
    if _is_modeler_batch(task_id):
        status = _batch_detail(task_id).totalStatus.value
        flex_unit = _batch_detail(task_id).realFlexUnit or None
        if (status not in ["success", "run_success"]) or (flex_unit is None):
            log.warning(
                f"Billed FlexCredit for task '{task_id}' is not available. If the task has been "
                "successfully run, it should be available shortly. If this issue persists, contact customer support."
            )
        else:
            if verbose:
                console.log(
                    f"Billed FlexCredit cost: {flex_unit:1.3f}. Minimum cost depends on "
                    "task execution details. Use 'web.real_cost(task_id)' to get the billed FlexCredit "
                    "cost after a simulation run."
                )

        return flex_unit
    else:
        task_info = get_info(task_id)
        flex_unit = task_info.realFlexUnit
        ori_flex_unit = task_info.oriRealFlexUnit
        if not flex_unit:
            log.warning(
                f"Billed FlexCredit for task '{task_id}' is not available. If the task has been "
                "successfully run, it should be available shortly."
            )
        else:
            if verbose:
                console.log(f"Billed flex credit cost: {flex_unit:1.3f}.")
                if flex_unit != ori_flex_unit and task_info.taskType == "FDTD":
                    console.log(
                        "Note: the task cost pro-rated due to early shutoff was below the minimum "
                        "threshold, due to fast shutoff. Decreasing the simulation 'run_time' should "
                        "decrease the estimated, and correspondingly the billed cost of such tasks."
                    )
        return flex_unit


@wait_for_connection
def account(verbose=True) -> Account:
    """Get account information including FlexCredit balance and usage limits.

    Parameters
    ----------
    verbose : bool = True
        If ``True``, prints account information including credit balance, expiration,
        and free simulation counts.

    Returns
    -------
    Account
        Object containing account information such as credit balance, expiration dates,
        and daily free simulation counts.

    Examples
    --------
    Get account information:

    .. code-block:: python

        account_info = web.account()
        # Displays:
        # Current FlexCredit balance: 10.00 and expiration date: 2024-12-31 23:59:59.
        # Remaining daily free simulations: 3.
    """
    account_info = Account.get()
    if verbose and account_info:
        console = get_logging_console()
        credit = account_info.credit
        credit_expiration = account_info.credit_expiration
        cycle_type = account_info.allowance_cycle_type
        cycle_amount = account_info.allowance_current_cycle_amount
        cycle_end_date = account_info.allowance_current_cycle_end_date
        free_simulation_counts = account_info.daily_free_simulation_counts

        message = ""
        if credit is not None:
            message += f"Current FlexCredit balance: {credit:.2f}"
            if credit_expiration is not None:
                message += (
                    f" and expiration date: {credit_expiration.strftime('%Y-%m-%d %H:%M:%S')}. "
                )
            else:
                message += ". "
        if cycle_type is not None and cycle_amount is not None and cycle_end_date is not None:
            cycle_end = cycle_end_date.strftime("%Y-%m-%d %H:%M:%S")
            message += f"{cycle_type} FlexCredit balance: {cycle_amount:.2f} and expiration date: {cycle_end}. "
        if free_simulation_counts is not None:
            message += f"Remaining daily free simulations: {free_simulation_counts}."

        console.log(message)

    return account_info


@wait_for_connection
def test() -> None:
    """Confirm whether Tidy3D authentication is configured.

    Raises
    ------
    WebError
        If Tidy3D authentication is not configured correctly.

    Notes
    -----
    This method tests the authentication configuration by attempting to retrieve
    the task list. If authentication is not properly set up, it will raise an
    exception with instructions on how to configure authentication.

    Examples
    --------
    Test authentication:

    .. code-block:: python

        web.test()
        # If successful, displays:
        # Authentication configured successfully!
    """
    try:
        # note, this is a little slow, but the only call that doesn't require providing a task id.
        get_tasks(num_tasks=0)
        console = get_logging_console()
        console.log("Authentication configured successfully!")
    except (WebError, HTTPError) as e:
        url = "https://docs.flexcompute.com/projects/tidy3d/en/latest/index.html"
        msg = (
            str(e)
            + "\n\n"
            + "It looks like the Tidy3D Python interface is not configured with your "
            "unique API key. "
            "To get your API key, sign into 'https://tidy3d.simulation.cloud' and copy it "
            "from your 'Account' page. Then you can configure tidy3d through command line "
            "'tidy3d configure' (recommended). Alternatively, one can manually create the configuration "
            "file by creating a file at your home directory '~/.tidy3d/config' (unix) or "
            "'.tidy3d/config' (windows) with content like: \n\n"
            "apikey = 'XXX' \n\nHere XXX is your API key copied from your account page within quotes.\n\n"
            f"For details, check the instructions at {url}."
        )
        raise WebError(msg) from e
