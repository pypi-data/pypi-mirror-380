"""
Our DC sources ultimately need to follow this standard form if we want to enable full electrical integration.

```
11.3.2 .DC: DC Transfer Function

General form:

    .dc srcnam vstart vstop vincr [src2 start2 stop2 incr2]

Examples:

    .dc VIN 0.25 5.0 0.25
    .dc VDS 0 10 .5 VGS 0 5 1
    .dc VCE 0 10 .25 IB 0 10u 1u
    .dc RLoad 1k 2k 100
    .dc TEMP -15 75 5
```

"""

from __future__ import annotations

from typing import Literal, Optional

import pydantic.v1 as pd

from tidy3d.components.base import Tidy3dBaseModel
from tidy3d.components.types import ArrayFloat1D
from tidy3d.constants import AMP, VOLT
from tidy3d.constants import inf as td_inf


class DCVoltageSource(Tidy3dBaseModel):
    """
    DC voltage source in volts.

    Notes
    -----

        This voltage refers to potential above the equivalent simulation ground. Currently, electrical ports
        are not defined.

    Examples
    --------
    >>> import tidy3d as td
    >>> voltages = [-0.5, 0, 1, 2, 3, 4]
    >>> voltage_source = td.DCVoltageSource(voltage=voltages)
    """

    name: Optional[str]
    voltage: ArrayFloat1D = pd.Field(
        ...,
        title="Voltage",
        description="DC voltage usually used as source in :class:`VoltageBC` boundary conditions.",
        units=VOLT,
    )

    # TODO: This should have always been in the field above but was introduced wrongly as a
    # standalone field. Keeping for compatibility, remove in 3.0.
    units: Literal[VOLT] = VOLT

    @pd.validator("voltage")
    def check_voltage(cls, val):
        for v in val:
            if v == td_inf:
                raise ValueError(f"Voltages must be finite. Currently  voltage={val}.")
        return val


class DCCurrentSource(Tidy3dBaseModel):
    """
    DC current source in amperes.

    Example
    -------
    >>> import tidy3d as td
    >>> current_source = td.DCCurrentSource(current=0.4)
    """

    name: Optional[str]
    current: pd.FiniteFloat = pd.Field(
        title="Current",
        description="DC current usually used as source in :class:`CurrentBC` boundary conditions.",
        units=AMP,
    )

    # TODO: This should have always been in the field above but was introduced wrongly as a
    # standalone field. Keeping for compatibility, remove in 3.0.
    units: Literal[AMP] = AMP
