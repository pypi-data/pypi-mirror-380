from dataclasses import dataclass
from typing import Any, List

import astropy.units as u
import numpy as np
from numpy.typing import ArrayLike, NDArray

from .options import STANDARD_PARAMS
from .utils import smooth_interpolation


@dataclass()
class Parameter:
    """Defines a parameter."""

    name: str | None = None
    description: str | None = None
    value: Any | None = None
    grid: np.ndarray | None = None
    unit: u.Quantity | None = None
    min: float | None = None
    max: float | None = None
    dtype: type | None = None
    smooth: bool | None = None
    reflective: bool | None = None
    periodic: bool | None = None
    free: bool | None = None
    shared: bool | None = None
    base: str | None = None
    uniform: float | None = None

    def _process_base(self, base: str | None) -> None:
        """Process the template attribute."""
        if base is None:
            return

        base_param = getattr(STANDARD_PARAMS, base)
        for key, value in base_param.items():
            if getattr(self, key) is None:
                setattr(self, key, value)

        for key in ["free", "shared", "smooth", "reflective", "periodic"]:
            if key not in base_param:
                if getattr(self, key) is not None:
                    continue

                setattr(self, key, False)

    def _set_to_numpy_array(self, array: ArrayLike | None = None) -> Any | np.ndarray:
        """Converts a value to a numpy array."""
        if array is None:
            return

        if isinstance(array, (tuple, list)):
            return np.array(array)

        return array

    def __setattr__(self, key: str, value: Any):
        """Sets an attribute."""
        if key != "unit":
            if isinstance(value, u.Quantity):
                value = value.value
        super().__setattr__(key, value)

    def __str__(self):
        message = (
            f"Parameter: {self.name} has the value "
            f"{np.round(self.value, 2)} and "
            f"is {'free' if self.free else 'fixed'}"
            f"is {'shared' if self.shared else 'non-shared'}"
        )
        if self.max is not None:
            message += f" with its limits being {self.min:.1f}-{self.max:.1f}"

        return message

    def __post_init__(self):
        """Post initialisation actions."""
        self.value = self._set_to_numpy_array(self.value)
        self.grid = self._set_to_numpy_array(self.grid)
        self._process_base(self.base)

    def __call__(
        self,
        t: NDArray[Any] | None = None,
        wl: NDArray[Any] | None = None,
    ) -> np.ndarray:
        """Gets the value for the parameter or the corresponding
        values for some points."""
        if self.value is None:
            return None

        if wl is None or self.grid is None:
            value = self.value
        else:
            if self.smooth:
                value = smooth_interpolation(wl.value, self.grid, self.value)
            else:
                value = np.interp(wl.value, self.grid, self.value)

        return u.Quantity(value, unit=self.unit, dtype=self.dtype)

    def copy(self) -> "Parameter":
        """Copies the parameter."""
        return Parameter(
            name=self.name,
            description=self.description,
            value=self.value,
            grid=self.grid,
            unit=self.unit,
            min=self.min,
            max=self.max,
            dtype=self.dtype,
            smooth=self.smooth,
            periodic=self.periodic,
            free=self.free,
            shared=self.shared,
            base=self.base,
            uniform=self.uniform,
        )

    def get_limits(self) -> List[float | None]:
        return self.min, self.max


@dataclass()
class MultiParam:
    params: List[Parameter] | None = None

    def __post_init__(self):
        """Post initialisation actions."""
        self.indices = np.array([i for i in range(len(self.params))])
        for index, param in zip(self.indices, self.params):
            if ".t" not in param.name:
                param.name += f".t{index}"

    def __getitem__(self, t):
        return self.params[t]

    def __call__(
        self,
        t: NDArray[Any] | None = None,
        wl: NDArray[Any] | None = None,
    ) -> np.ndarray:
        """Gets the value for the parameter or the corresponding
        values for some points."""
        return self.params[t](wl)

    def copy(self) -> "MultiParam":
        """Copies the parameter."""
        return MultiParam([param.copy() for param in self.params])
