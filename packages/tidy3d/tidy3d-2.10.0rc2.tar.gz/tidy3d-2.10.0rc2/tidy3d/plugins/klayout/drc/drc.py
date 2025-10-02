"""Methods for integrating KLayout's DRC with Tidy3D."""

from __future__ import annotations

import re
from pathlib import Path
from subprocess import run
from typing import Union

import pydantic.v1 as pd
from pydantic.v1 import validator

from tidy3d.components.base import Tidy3dBaseModel
from tidy3d.components.geometry.base import Geometry
from tidy3d.components.simulation import Simulation
from tidy3d.components.structure import Structure
from tidy3d.exceptions import ValidationError
from tidy3d.log import get_logging_console
from tidy3d.plugins.klayout.drc.defaults import (
    DEFAULT_GDSFILE,
    DEFAULT_RESULTSFILE,
    DEFAULT_VERBOSE,
)
from tidy3d.plugins.klayout.drc.results import DRCResults
from tidy3d.plugins.klayout.util import check_installation


class DRCConfig(Tidy3dBaseModel):
    """Configuration for KLayout DRC."""

    gdsfile: pd.FilePath = pd.Field(
        title="GDS File",
        description="The path to the GDS file to write the Tidy3D object to.",
    )
    drc_runset: pd.FilePath = pd.Field(
        title="DRC Runset file",
        description="Path to the KLayout DRC runset file.",
    )
    resultsfile: Path = pd.Field(
        title="DRC Results File",
        description="Path to the KLayout DRC results file.",
    )
    verbose: bool = pd.Field(
        title="Verbose",
        description="Whether to print logging.",
    )

    @validator("gdsfile")
    def _validate_gdsfile_filetype(cls, v: pd.FilePath) -> pd.FilePath:
        """Check GDS filetype is ``.gds``."""
        if v.suffix != ".gds":
            raise ValidationError(f"GDS file '{v}' must end with '.gds'.")
        return v

    @validator("drc_runset")
    def _validate_drc_runset_filetype(cls, v: pd.FilePath) -> pd.FilePath:
        """Check DRC runset filetype is ``.drc``."""
        if v.suffix != ".drc":
            raise ValidationError(f"DRC runset file '{v}' must end with '.drc'.")
        return v

    @validator("drc_runset")
    def _validate_drc_runset_format(cls, v: pd.FilePath) -> pd.FilePath:
        """Check if the DRC runset file is formatted correctly.
        The checks are:
        1. The GDS source must be loaded with 'source($gdsfile)'.
        2. The report must be defined as 'report("<your string>", $resultsfile)'.
        """
        with Path(v).open("r") as f:
            content = f.read()
            if not re.search(r"source\(\s*\$gdsfile\s*\)", content):
                raise ValidationError(
                    "DRC runset is not formatted correctly. The GDS source must be loaded with 'source($gdsfile)'. Please refer to the documentation at 'tidy3d/plugins/klayout/drc/README.md' for more details."
                )
            if not re.search(r"""report\(['"](.*?)['"],\s*\$resultsfile\)""", content):
                raise ValidationError(
                    "DRC runset is not formatted correctly. The report must be defined as 'report(\"<your report name>\", $resultsfile)'. Please refer to the documentation at 'tidy3d/plugins/klayout/drc/README.md' for more details."
                )
        return v


class DRCRunner(Tidy3dBaseModel):
    """A class for running KLayout DRC. Can be used to run DRC on a Tidy3D object or a GDS file.

    Parameters
    ----------
    drc_runset : Path
        The path to the KLayout DRC runset file.
    verbose : bool
        Whether to print logging. Default is ``True``.

    Example
    -------
    >>> # Running DRC on a GDS file:
    >>> from tidy3d.plugins.klayout.drc import DRCRunner
    >>> runner = DRCRunner(drc_runset="my_drc_runset.drc", verbose=True) # doctest: +SKIP
    >>> results = runner.run(source="my_layout.gds", resultsfile="drc_results.lyrdb") # doctest: +SKIP
    >>> print(results) # doctest: +SKIP
    >>> # Running DRC on a Tidy3D object:
    >>> import tidy3d as td
    >>> from tidy3d.plugins.klayout.drc import DRCRunner
    >>> vertices = [(-2, 0), (-1, 1), (0, 0.5), (1, 1), (2, 0), (0, -1)]
    >>> geom = td.PolySlab(vertices=vertices, slab_bounds=(0, 0.22), axis=2)
    >>> runner = DRCRunner(drc_runset="my_drc_runset.drc", verbose=True) # doctest: +SKIP
    >>> results = runner.run(source=geom, td_object_gds_savefile="geom.gds", resultsfile="drc_results.lyrdb", z=0.1, gds_layer=0, gds_dtype=0) # doctest: +SKIP
    >>> print(results) # doctest: +SKIP
    """

    drc_runset: pd.FilePath = pd.Field(
        title="DRC Runset file",
        description="Path to the KLayout DRC runset file.",
    )
    verbose: bool = pd.Field(
        default=DEFAULT_VERBOSE,
        title="Verbose",
        description="Whether to print logging.",
    )

    def run(
        self,
        source: Union[Geometry, Structure, Simulation, Path],
        td_object_gds_savefile: Path = DEFAULT_GDSFILE,
        resultsfile: Path = DEFAULT_RESULTSFILE,
        **to_gds_file_kwargs,
    ) -> None:
        """Runs KLayout's DRC on a GDS file or a Tidy3D object. The Tidy3D object can be a :class:`.Geometry`, :class:`.Structure`, or :class:`.Simulation`.

        Parameters
        ----------
        source : Union[:class:`.Geometry`, :class:`.Structure`, :class:`.Simulation`, Path]
            The :class:`.Geometry`, :class:`.Structure`, :class:`.Simulation`, or GDS file to run DRC on.
        td_object_gds_savefile : Path
            The path to save the Tidy3D object to. Defaults to ``"layout.gds"``.
        resultsfile : Path
            The path to save the KLayout DRC results file to. Defaults to ``"drc_results.lyrdb"``.
        **to_gds_file_kwargs
            Additional keyword arguments to pass to the Tidy3D object-specific ``to_gds_file()`` method.

        Returns
        -------
        :class:`.DRCResults`
            The DRC results object containing violations and status.

        Example
        -------
        Running DRC on a GDS file:
        >>> from tidy3d.plugins.klayout.drc import DRCRunner
        >>> runner = DRCRunner(drc_runset="my_drc_runset.drc", verbose=True) # doctest: +SKIP
        >>> results = runner.run(source="my_layout.gds") # doctest: +SKIP
        >>> print(results) # doctest: +SKIP

        Running DRC on a Tidy3D object:
        >>> import tidy3d as td
        >>> from tidy3d.plugins.klayout.drc import DRCRunner
        >>> vertices = [(-2, 0), (-1, 1), (0, 0.5), (1, 1), (2, 0), (0, -1)]
        >>> geom = td.PolySlab(vertices=vertices, slab_bounds=(0, 0.22), axis=2)
        >>> runner = DRCRunner(drc_runset="my_drc_runset.drc", verbose=True) # doctest: +SKIP
        >>> results = runner.run(source=geom, z=0.1, gds_layer=0, gds_dtype=0) # doctest: +SKIP
        >>> print(results) # doctest: +SKIP
        """
        if isinstance(source, (Geometry, Structure, Simulation)):
            gdsfile = td_object_gds_savefile
            if self.verbose:
                console = get_logging_console()
                console.log(f"Writing Tidy3D object to GDS file '{gdsfile}'.")
            source.to_gds_file(fname=gdsfile, **to_gds_file_kwargs)
        else:
            gdsfile = source

        config = DRCConfig(
            gdsfile=gdsfile,
            drc_runset=self.drc_runset,
            resultsfile=resultsfile,
            verbose=self.verbose,
        )
        return run_drc_on_gds(config=config)


def run_drc_on_gds(config: DRCConfig) -> DRCResults:
    """Runs KLayout's DRC on a GDS file.

    Parameters
    ----------
    config : :class:`.DRCConfig`
        The configuration for the DRC run.

    Returns
    -------
    :class:`.DRCResults`
        The DRC results object containing violations and status.

    Example
    -------
    >>> from tidy3d.plugins.klayout.drc import run_drc_on_gds, DRCConfig
    >>> config = DRCConfig(gdsfile="geom.gds", drc_runset="my_drc_runset.drc", resultsfile="drc_results.lyrdb", verbose=True) # doctest: +SKIP
    >>> results = run_drc_on_gds(config) # doctest: +SKIP
    >>> print(results) # doctest: +SKIP
    """
    check_installation(raise_error=True)

    if config.verbose:
        console = get_logging_console()
        console.log(
            f"Running KLayout DRC on GDS file '{config.gdsfile}' with runset '{config.drc_runset}' and saving results to '{config.resultsfile}'..."
        )
    # run klayout DRC as a subprocess
    output = run(
        [
            "klayout",
            "-b",
            "-r",
            config.drc_runset,
            "-rd",
            f"gdsfile={config.gdsfile}",
            "-rd",
            f"resultsfile={config.resultsfile}",
        ],
        capture_output=True,
    )

    if output.returncode != 0:
        raise RuntimeError(f"KLayout DRC failed with error message: '{output.stderr}'.")
    if config.verbose:
        console.log("KLayout DRC completed successfully.")

    return DRCResults.load(resultsfile=config.resultsfile)
