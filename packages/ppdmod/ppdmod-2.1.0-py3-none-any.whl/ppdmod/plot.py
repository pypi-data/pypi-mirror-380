from itertools import chain, zip_longest
from pathlib import Path
from typing import List

import astropy.units as u
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from dynesty import DynamicNestedSampler, NestedSampler
from dynesty import plotting as dyplot
from matplotlib.axes import Axes
from matplotlib.legend import Legend

from .base import FourierComponent
from .options import OPTIONS


def get_best_plot_arrangement(nplots):
    """Gets the best plot arrangement for a given number of plots."""
    sqrt_nplots = np.sqrt(nplots)
    cols = int(np.ceil(sqrt_nplots))
    rows = int(np.floor(sqrt_nplots))

    while rows * cols < nplots:
        if cols < rows:
            cols += 1
        else:
            rows += 1

    while (rows - 1) * cols >= nplots:
        rows -= 1

    return rows, cols


def set_axes_color(
    ax: Axes,
    background_color: str,
    set_label: bool = True,
    direction: str | None = None,
) -> None:
    """Sets all the axes' facecolor."""
    opposite_color = "white" if background_color == "black" else "black"
    ax.set_facecolor(background_color)
    ax.spines["bottom"].set_color(opposite_color)
    ax.spines["top"].set_color(opposite_color)
    ax.spines["right"].set_color(opposite_color)
    ax.spines["left"].set_color(opposite_color)

    if set_label:
        ax.xaxis.label.set_color(opposite_color)
        ax.yaxis.label.set_color(opposite_color)

    ax.tick_params(axis="both", colors=opposite_color, direction=direction)


def set_legend_color(legend: Legend, background_color: str) -> None:
    """Sets the legend's facecolor."""
    opposite_color = "white" if background_color == "black" else "black"
    plt.setp(legend.get_texts(), color=opposite_color)
    legend.get_frame().set_facecolor(background_color)


def format_labels(
    labels: List[str], units: List[str] | None = None, split: bool = False
) -> List[str]:
    """Formats the labels in LaTeX.

    Parameters
    ----------
    labels : list of str
        The labels.
    units : list of str, optional
        The units. The default is None.
    split : bool, optional
        If True, splits into labels, units, and uncertainties.
        The default is False.

    Returns
    -------
    labels : list of str
        The formatted labels.
    units : list of str, optional
        The formatted units. If split is True
    """
    nice_labels = {
        "rin": {"letter": "R", "indices": [r"\text{in}"]},
        "rout": {"letter": "R", "indices": [r"\text{out}"]},
        "p": {"letter": "p"},
        "q": {"letter": "q"},
        "rho": {"letter": r"\rho"},
        "theta": {"letter": r"\theta"},
        "logsigma0": {"letter": r"\Sigma", "indices": ["0"]},
        "sigma0": {"letter": r"\Sigma", "indices": ["0"]},
        "weight_cont": {"letter": "w", "indices": [r"\text{cont}"]},
        "pa": {"letter": r"\theta", "indices": []},
        "cinc": {"letter": r"\cos\left(i\right)"},
        "temp0": {"letter": "T", "indices": ["0"]},
        "tempc": {"letter": "T", "indices": [r"\text{c}"]},
        "f": {"letter": "f"},
        "fr": {"letter": "fr"},
        "fwhm": {"letter": r"\sigma"},
        "r": {"letter": "r"},
        "phi": {"letter": r"\phi"},
    }

    formatted_labels = []
    for label in labels:
        if "-" in label:
            name, index = label.split("-")
        else:
            name, index = label, ""

        if name in nice_labels or name[-1].isdigit():
            if ".t" in name:
                name, time_index = name.split(".")
            else:
                time_index = None

            if name not in nice_labels and name[-1].isdigit():
                letter = nice_labels[name[:-1]]["letter"]
                indices = [name[-1]]
                if index:
                    indices.append(index)
            else:
                letter = nice_labels[name]["letter"]
                if name in ["temp0", "tempc"]:
                    indices = nice_labels[name].get("indices", [])
                else:
                    indices = [*nice_labels[name].get("indices", [])]
                    if index:
                        indices.append(rf"\mathrm{{{index}}}")

            if time_index is not None:
                indices.append(rf"\mathrm{{{time_index}}}")

            indices = r",\,".join(indices)
            formatted_label = f"{letter}_{{{indices}}}"
            if "log" in label:
                formatted_label = rf"\log_{{10}}\left({formatted_label}\right)"

            formatted_labels.append(f"${formatted_label}$")
        else:
            if "weight" in name:
                name, letter = name.replace("weight", ""), "w"

                indices = []
                if "small" in name:
                    name = name.replace("small", "")
                    indices = [r"\text{small}"]
                elif "large" in name:
                    name = name.replace("large", "")
                    indices = [r"\text{large}"]

                name = name.replace("_", "")
                indices.append(rf"\text{{{name}}}")

                indices = r",\,".join(indices)
                formatted_label = f"{letter}_{{{indices}}}"
                if "log" in label:
                    formatted_label = rf"\log_{{10}}\left({formatted_label}\right)"
            elif "scale" in name:
                formatted_label = (
                    rf"w_{{\text{{{name.replace('scale_', '').upper()}}}}}"
                )
            elif "lnf" in name:
                formatted_label = (
                    rf"\ln\left(f\right)_{{\text{{{name.split('_')[0]}}}}}"
                )
            else:
                formatted_label = label

            formatted_labels.append(f"${formatted_label}$")

    if units is not None:
        reformatted_units = []
        for unit in units:
            if unit == u.g / u.cm**2:
                unit = r"\gram\per\square\centi\metre"
            elif unit == u.au:
                unit = r"\astronomicalunit"
            elif unit == u.deg:
                unit = r"\degree"
            elif unit == u.pct:
                unit = r"\percent"

            reformatted_units.append(unit)

        reformatted_units = [
            rf"$(\unit{{{str(unit).strip()}}})$" if str(unit) else ""
            for unit in reformatted_units
        ]
        if split:
            return formatted_labels, reformatted_units

        formatted_labels = [
            rf"{label} {unit}"
            for label, unit in zip(formatted_labels, reformatted_units)
        ]
    return formatted_labels


def needs_sci_notation(ax):
    """Checks if scientific notation is needed"""
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()
    return (
        abs(x_min) <= 1e-3
        or abs(x_max) <= 1e-3
        or abs(y_min) <= 1e-3
        or abs(y_max) <= 1e-3
    )


def plot_chains(
    sampler: NestedSampler | DynamicNestedSampler,
    labels: List[str],
    units: List[str] | None = None,
    savefig: Path | None = None,
    **kwargs,
) -> None:
    """Plots the fitter's chains.

    Parameters
    ----------
    sampler : dynesty.NestedSampler or dynesty.DynamicNestedSampler
        The sampler.
    labels : list of str
        The parameter labels.
    units : list of str, optional
    discard : int, optional
    savefig : pathlib.Path, optional
        The save path. The default is None.
    """
    labels = format_labels(labels, units)
    quantiles = [x / 100 for x in OPTIONS.fit.quantiles]
    results = sampler.results
    dyplot.traceplot(
        results,
        labels=labels,
        truths=np.zeros(len(labels)),
        quantiles=quantiles,
        truth_color="black",
        show_titles=True,
        trace_cmap="viridis",
        connect=True,
        connect_highlight=range(5),
    )

    if savefig:
        plt.savefig(savefig, format=Path(savefig).suffix[1:], dpi=OPTIONS.plot.dpi)
    else:
        plt.show()
    plt.close()


def plot_product(
    points,
    product,
    xlabel,
    ylabel,
    save_path=None,
    ax=None,
    colorbar=False,
    cmap: str = "",
    scale=None,
    label=None,
):
    norm = None
    if label is not None:
        if isinstance(label, (np.ndarray, u.Quantity)):
            norm = mcolors.Normalize(vmin=label[0].value, vmax=label[-1].value)

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    if product.ndim > 1:
        for lb, prod in zip(label, product):
            color = None
            if norm is not None:
                colormap = get_colormap(cmap)
                color = colormap(norm(lb.value))
            ax.plot(points, prod, label=lb, color=color)
        if not colorbar:
            ax.legend()
    else:
        ax.plot(points, product, label=label)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if scale == "log":
        ax.set_yscale("log")
    elif scale == "loglog":
        ax.set_yscale("log")
        ax.set_xscale("log")
    elif scale == "sci":
        ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
        ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))

    if colorbar:
        sm = cm.ScalarMappable(cmap=get_colormap(cmap), norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax)
        cbar.set_ticks(OPTIONS.plot.ticks)
        cbar.set_ticklabels([f"{wavelength:.1f}" for wavelength in OPTIONS.plot.ticks])
        cbar.set_label(label=r"$\lambda$ ($\mathrm{\mu}$m)")

    if save_path is not None:
        fig.savefig(save_path, format=Path(save_path).suffix[1:], dpi=OPTIONS.plot.dpi)
        plt.close(fig)


# TODO: Clean and split this function into multiple ones
def plot_products(
    dim: int,
    components: List[FourierComponent],
    component_labels: List[str],
    save_dir: Path | None = None,
) -> None:
    """Plots the intermediate products of the model (temperature, density, etc.)."""
    component_labels = [
        " ".join(map(str.title, label.split("_"))) for label in component_labels
    ]
    for t in range(OPTIONS.data.nt):
        wls = np.linspace(OPTIONS.fit.wls[0], OPTIONS.fit.wls[-1], dim)
        radii, surface_density, optical_depth = [], [], []
        fluxes, emissivity, intensity = [], [], []
        _, ax = plt.subplots(figsize=(5, 5))
        for label, component in zip(component_labels, components):
            component.dim.value = dim
            flux = component.fr(t, wls) * component.compute_flux(t, wls).squeeze()
            plot_product(
                wls,
                flux,
                r"$\lambda$ ($\mathrm{\mu}$m)",
                r"$F_{\nu}$ (Jy)",
                scale="log",
                ax=ax,
                label=label,
            )
            fluxes.append(flux)
            if component.name in ["Point", "Gauss", "BBGauss"]:
                continue

            radius = component.compute_internal_grid(t, wls)
            radii.append(radius)

            surface_density.append(component.compute_surface_density(radius, t, wls))
            optical_depth.append(
                component.compute_optical_depth(radius, t, wls[:, np.newaxis])
            )
            emissivity.append(
                component.compute_emissivity(radius, t, wls[:, np.newaxis])
            )
            intensity.append(component.compute_intensity(radius, t, wls[:, np.newaxis]))

        surface_density = u.Quantity(surface_density)
        optical_depth = u.Quantity(optical_depth)
        emissivity = u.Quantity(emissivity)
        intensity = u.Quantity(intensity)

        total_flux = np.sum(fluxes, axis=0)
        ax.plot(wls, total_flux, label="Total")
        ax.set_yscale("log")
        ax.set_ylim([1e-1, None])
        ax.legend()
        plt.savefig(save_dir / f"fluxes_t{t}.png", format="png", dpi=OPTIONS.plot.dpi)
        plt.close()

        _, ax = plt.subplots(figsize=(5, 5))
        for label, flux_ratio in zip(component_labels, np.array(fluxes) / total_flux):
            plot_product(
                wls,
                flux_ratio * 100,
                r"$\lambda$ ($\mathrm{\mu}$m)",
                r"$F_{\nu}$ / $F_{\nu,\,\mathrm{tot}}$ (%)",
                ax=ax,
                label=label,
            )

        ax.legend()
        ax.set_ylim([0, 100])
        plt.savefig(
            save_dir / f"flux_ratios_t{t}.png", format="png", dpi=OPTIONS.plot.dpi
        )
        plt.close()

        radii_bounds = [
            (prev[-1], current[0]) for prev, current in zip(radii[:-1], radii[1:])
        ]
        fill_radii = [np.linspace(lower, upper, dim) for lower, upper in radii_bounds]
        merged_radii = list(chain.from_iterable(zip_longest(radii, fill_radii)))[:-1]
        merged_radii = u.Quantity(np.concatenate(merged_radii, axis=0))
        fill_zeros = np.zeros((len(fill_radii), wls.size, dim))
        disc_component = [
            comp for comp in components if comp.name not in ["Point", "Gauss"]
        ][0]

        # TODO: Make it so that the temperatures are somehow continous in the plot? (Maybe check for self.temps in the models?)
        # or interpolate smoothly somehow (see the one youtube video?) :D
        temperature = disc_component.compute_temperature(merged_radii, t, wls)
        surface_density = u.Quantity(
            list(
                chain.from_iterable(
                    zip_longest(surface_density, fill_zeros[:, 0, :] * u.g / u.cm**2)
                )
            )[:-1]
        )
        surface_density = np.concatenate(surface_density, axis=0)
        optical_depth = u.Quantity(
            list(chain.from_iterable(zip_longest(optical_depth, fill_zeros)))[:-1]
        )
        optical_depth = np.hstack(optical_depth)
        emissivity = u.Quantity(
            list(chain.from_iterable(zip_longest(emissivity, fill_zeros)))[:-1]
        )
        emissivity = np.hstack(emissivity)
        intensity = u.Quantity(
            list(
                chain.from_iterable(
                    zip_longest(
                        intensity, fill_zeros * u.erg / u.cm**2 / u.s / u.Hz / u.sr
                    )
                )
            )[:-1]
        )
        intensity = np.hstack(intensity)
        intensity = intensity.to(u.W / u.m**2 / u.Hz / u.sr)
        merged_radii_mas = (
            (merged_radii.to(u.au) / components[1].dist().to(u.pc)).value * 1e3 * u.mas
        )

        # TODO: Code this in a better manner
        wls = [1.7, 2.15, 3.4, 8, 11.3, 13] * u.um
        cumulative_intensity = (
            np.zeros((wls.size, merged_radii_mas.size))
            * u.erg
            / u.s
            / u.Hz
            / u.cm**2
            / u.sr
        )
        # for index, wl in enumerate(wls):
        #     tmp_intensity = [
        #         component.compute_intensity(radius, t, wl)
        #         for radius, component in zip(radii, components[1:])
        #     ]
        #     tmp_intensity = u.Quantity(
        #         list(
        #             chain.from_iterable(
        #                 zip_longest(
        #                     tmp_intensity,
        #                     fill_zeros[0, 0][np.newaxis, :]
        #                     * u.erg
        #                     / u.cm**2
        #                     / u.s
        #                     / u.Hz
        #                     / u.sr,
        #                 )
        #             )
        #         )[:-1]
        #     )
        #     cumulative_intensity[index, :] = np.hstack(tmp_intensity)
        #
        # cumulative_intensity = cumulative_intensity.to(
        #     u.erg / u.s / u.Hz / u.cm**2 / u.mas**2
        # )
        # cumulative_total_flux = (
        #     2
        #     * np.pi
        #     * disc_component.cinc(t, wls)
        #     * np.trapz(merged_radii_mas * cumulative_intensity, merged_radii_mas).to(
        #         u.Jy
        #     )[:, np.newaxis]
        # )
        #
        # cumulative_flux = np.zeros((wls.size, merged_radii.size)) * u.Jy
        # for index, _ in enumerate(merged_radii):
        #     cumulative_flux[:, index] = (
        #         2
        #         * np.pi
        #         * disc_component.cinc(t, wls)
        #         * np.trapz(
        #             merged_radii_mas[:index] * cumulative_intensity[:, :index],
        #             merged_radii_mas[:index],
        #         ).to(u.Jy)
        #     )
        # cumulative_flux_ratio = cumulative_flux / cumulative_total_flux
        # plot_product(
        #     merged_radii.value,
        #     cumulative_flux_ratio.value,
        #     "$R$ (AU)",
        #     r"$F_{\nu}\left(r\right)/F_{\nu,\,\mathrm{{tot}}}$ (a.u.)",
        #     label=wls,
        #     save_path=save_dir / f"cumulative_flux_ratio_t{t}.png",
        # )

        plot_product(
            merged_radii.value,
            temperature.value,
            "$R$ (AU)",
            "$T$ (K)",
            scale="log",
            save_path=save_dir / f"temperature_t{t}.png",
        )
        plot_product(
            merged_radii.value,
            surface_density.value,
            "$R$ (au)",
            r"$\Sigma$ (g cm$^{-2}$)",
            save_path=save_dir / f"surface_density_t{t}.png",
            scale="sci",
        )
        plot_product(
            merged_radii.value,
            optical_depth.value,
            "$R$ (AU)",
            r"$\tau_{\nu}$",
            save_path=save_dir / f"optical_depths_t{t}.png",
            scale="log",
            colorbar=True,
            label=wls,
        )
        # plot_product(merged_radii.value, emissivities.value,
        #              "$R$ (AU)", r"$\epsilon_{\nu}$",
        #              save_path=save_dir / "emissivities.png",
        #              label=wavelength)
        # plot_product(merged_radii.value, brightnesses.value,
        #              "$R$ (AU)", r"$I_{\nu}$ (W m$^{-2}$ Hz$^{-1}$ sr$^{-1}$)",
        #              save_path=save_dir / "brightnesses.png",
        #              scale="log", label=wavelength)
