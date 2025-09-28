from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict

import astropy.units as u
import numpy as np
import toml


def get_units(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """Converts the units in a dictionary to astropy units."""
    converted_dictionary = dictionary.copy()
    for val in converted_dictionary.values():
        if "unit" in val:
            if val["unit"] == "one":
                val["unit"] = u.one
            else:
                val["unit"] = u.Unit(val["unit"])

    return converted_dictionary


def load_toml_to_namespace(toml_file: Path):
    """Loads a toml file into a namespace."""
    with open(toml_file, "r") as file:
        data = toml.load(file)["STANDARD_PARAMETERS"]

    return SimpleNamespace(**get_units(data))


STANDARD_PARAMS = load_toml_to_namespace(
    Path(__file__).parent / "config" / "standard_parameters.toml"
)


# NOTE: Data
vis_data = SimpleNamespace(
    val=np.array([]),
    err=np.array([]),
    u=np.array([]).reshape(1, -1),
    v=np.array([]).reshape(1, -1),
    count=0,
)
vis2_data = SimpleNamespace(
    val=np.array([]),
    err=np.array([]),
    u=np.array([]).reshape(1, -1),
    v=np.array([]).reshape(1, -1),
    count=0,
)
t3_data = SimpleNamespace(
    val=np.array([]),
    err=np.array([]),
    u123=np.array([]),
    v123=np.array([]),
    u=np.array([]).reshape(1, -1),
    v=np.array([]).reshape(1, -1),
    i123=np.array([]),
    count=0,
)
flux_data = SimpleNamespace(val=np.array([]), err=np.array([]), count=0)
gravity = SimpleNamespace(index=20)
dtype = SimpleNamespace(complex=np.complex128, real=np.float64)
binning = SimpleNamespace(
    unknown=0.2 * u.um,
    kband=0.2 * u.um,
    hband=0.2 * u.um,
    lband=0.1 * u.um,
    mband=0.1 * u.um,
    lmband=0.1 * u.um,
    nband=0.1 * u.um,
)
interpolation = SimpleNamespace(dim=10, kind="linear", fill_value=None)
data = SimpleNamespace(
    readouts=[],
    readouts_t=[],
    hduls=[],
    hduls_t=[],
    nt=1,
    bands=[],
    resolutions=[],
    do_bin=True,
    flux=flux_data,
    vis=vis_data,
    vis2=vis2_data,
    t3=t3_data,
    gravity=gravity,
    binning=binning,
    dtype=dtype,
    interpolation=interpolation,
    epoch_counts=[],
)

# NOTE: Model
model = SimpleNamespace(
    components=None,
    output="non-normed",
    gridtype="logarithmic",
)

# NOTE: Weights
weights = SimpleNamespace(
    flux=SimpleNamespace(general=1),
    t3=SimpleNamespace(general=1),
    vis=SimpleNamespace(general=1),
)

# NOTE: Fitting
fit = SimpleNamespace(
    weights=weights,
    type="disc",
    data=["flux", "vis", "t3"],
    bands=["all"],
    wls=None,
    quantiles=[2.5, 50, 97.5],
    fitter="dynesty",
    conditions=None,
)

# NOTE: All options
OPTIONS = SimpleNamespace(data=data, model=model, fit=fit)
