"""Abstract base for classes that define simulation sources."""

from __future__ import annotations

from abc import ABC, abstractmethod

import pydantic.v1 as pydantic

from tidy3d.components.base import Tidy3dBaseModel
from tidy3d.components.validators import validate_name_str
from tidy3d.components.viz import PlotParams


class AbstractSource(Tidy3dBaseModel, ABC):
    """Abstract base class for all sources."""

    name: str = pydantic.Field(None, title="Name", description="Optional name for the source.")

    @abstractmethod
    def plot_params(self) -> PlotParams:
        """Default parameters for plotting a Source object."""

    _name_validator = validate_name_str()
