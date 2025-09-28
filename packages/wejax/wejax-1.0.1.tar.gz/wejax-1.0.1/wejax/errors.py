r"""
Estimation errors
=================

This module provides functions to compute and plot error covariance and
correlation matrices.

Error covariance matrix
-----------------------

The errors on the estimated parameters can be characterized by their covariance
matrix :math:`\Sigma`, which is defined as the inverse of the Fisher information
matrix,

.. math::

    \mathrm{Cov}(\theta_i, \theta_j) = \Sigma_{ij} = \left( I^{-1} \right)_{ij}.

The diagonal elements of :math:`\Sigma` provide the variances of the estimated
parameters, and the off-diagonal elements describe the correlations.

.. autofunction:: covariance_matrix

.. autofunction:: stddevs

Correlation matrix
------------------

The correlation matrix :math:`P` is defined as the normalized covariance matrix,
i.e., the matrix of the standard deviations and the correlation coefficients.

.. autofunction:: correlation_matrix

Plotting
--------

You can plot the error covariance matrix using the function
:func:`wejax.errors.plot_covariance_matrix`.

.. image:: _static/img/correlation-matrix.png
    :alt: Example correlation matrix
    :align: center

.. autofunction:: plot_correlation_matrix

"""

from itertools import product
from typing import Sequence

import jax.numpy as jnp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from jax import Array
from jax._src.typing import ArrayLike
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def covariance_matrix(
    fim: ArrayLike,
    *,
    argnums: Sequence[int] | None = None,
    rtol: float | None = None,
) -> Array:
    """Compute the error covariance matrix from the Fisher information matrix.

    If the matrix is singular, use ``argnums`` to select the parameters for
    which the error covariance matrix is computed. If ``rtol`` is not ``None``,
    the Moore-Penrose pseudo-inverse is computed.

    Examples
    --------
    >>> cov = covariance_matrix(fim)

    Fixing some parameters yields a different covariance matrix:

    >>> cov2 = covariance_matrix(fim, argnums=(0, 1))
    >>> np.testing.assert_array_almost_equal(cov2, cov[..., :2, :2])
    False

    Parameters
    ----------
    F : Array-like of shape ``(..., Np, Np)``
        Fisher information matrix. Here, ``Np`` is the number of parameters.
    argnums : Sequence of int or None, optional
        Indices of the parameters for which the error covariance matrix is
        computed. By default, the error covariance matrix is computed for all
        parameters.
    rtol : float or None, optional
        Cutoff parameter for small singular values.

        Singular values smaller than ``rtol`` times the largest singular value
        are considered zero and the function returns the Moore-Penrose
        pseudo-inverse. If ``None``, the exact inverse is computed.

    Returns
    -------
    Array of shape ``(..., Na, Na)``
        Error covariance matrix. Here, ``Na`` is the number of parameters for
        which the error covariance matrix is computed (length of ``argnums``).
    """
    fim = jnp.asarray(fim)

    # By default, compute error covariance matrix for all parameters
    if argnums is None:
        argnums = list(range(fim.shape[-1]))

    # Check indices are valid
    if not all(0 <= i < fim.shape[-1] for i in argnums):
        raise ValueError("Invalid indices in argnums.")

    # Compute the error covariance matrix
    restricted_fim = fim[..., argnums, :][..., argnums]
    if rtol is None:
        error_covariance = jnp.linalg.inv(restricted_fim)
    else:
        error_covariance = jnp.linalg.pinv(restricted_fim, rtol=rtol, hermitian=True)

    return error_covariance


def _invert_fim_if_needed(
    *, fim: ArrayLike | None = None, cov: ArrayLike | None = None
) -> Array:
    """Invert FIM to get covariance matrix if not provided.

    Parameters
    ----------
    fim : Array-like of shape ``(..., Np, Np)`` or None
        Fisher information matrix. Here, ``Np`` is the number of parameters.
    cov : Array-like of shape ``(..., Np, Np)`` or None
        Error covariance matrix. Here, ``Np`` is the number of parameters.

    Returns
    -------
    Array of shape ``(..., Np, Np)``
        Error covariance matrix.

    Raises
    ------
    ValueError
        If neither ``fim`` nor ``cov`` is provided.
    ValueError
        If both ``fim`` and ``cov`` are provided.
    """
    if cov is None and fim is None:
        raise ValueError("Either cov or fim must be provided.")
    if cov is not None and fim is not None:
        raise ValueError("Only one of cov and fim must be provided.")

    # Invert FIM to get covariance matrix if not provided
    if fim is not None:
        cov = covariance_matrix(fim)
    assert cov is not None

    return jnp.asarray(cov)


def stddevs(*, fim: ArrayLike | None = None, cov: ArrayLike | None = None) -> Array:
    """Compute parameter standard deviations.

    You can provide the noise covariance matrix as input, to avoid inverting
    the Fisher information matrix.

    Examples
    --------
    >>> a = stddevs(fim=fim)
    >>> cov = covariance_matrix(fim)
    >>> b = stddevs(cov=cov)
    >>> np.testing.assert_array_almost_equal(a, b)
    True

    Parameters
    ----------
    fim : Array-like of shape ``(..., Np, Np)`` or None
        Fisher information matrix. Here, ``Np`` is the number of parameters.
    cov : Array-like of shape ``(..., Np, Np)`` or None
        Error covariance matrix. Here, ``Np`` is the number of parameters.

    Returns
    -------
    Array of shape ``(..., Np)``
        Standard deviations.
    """
    cov = _invert_fim_if_needed(fim=fim, cov=cov)
    return jnp.sqrt(jnp.diagonal(cov, axis1=-2, axis2=-1))


def correlation_matrix(
    *, fim: ArrayLike | None = None, cov: ArrayLike | None = None
) -> Array:
    """Compute the correlation matrix (normalized covariance matrix).

    You can provide the noise covariance matrix as input, to avoid inverting
    the Fisher information matrix.

    Examples
    --------
    >>> a = correlation_matrix(fim=fim)
    >>> cov = covariance_matrix(fim)
    >>> b = correlation_matrix(cov=cov)
    >>> np.testing.assert_array_almost_equal(a, b)
    True

    Parameters
    ----------
    fim : Array-like of shape ``(..., Np, Np)`` or None
        Fisher information matrix. Here, ``Np`` is the number of parameters.
    cov : Array-like of shape ``(..., Np, Np)`` or None
        Error covariance matrix. Here, ``Np`` is the number of parameters.

    Returns
    -------
    Array of shape ``(..., Np, Np)``
        Correlation matrix.
    """
    cov = _invert_fim_if_needed(fim=fim, cov=cov)

    # Normalize covariance matrix by the product of standard deviations
    # We use the outer product to compute the denominator efficiently
    std_devs = stddevs(cov=cov)
    outer_std_devs = jnp.einsum("...i, ...j -> ...ij", std_devs, std_devs)
    corr = cov / outer_std_devs

    # Replace diagonal elements with standard deviations
    diag = jnp.diag(std_devs)
    diag = jnp.broadcast_to(diag, corr.shape)
    corr = jnp.where(diag, diag, corr)

    return corr


def plot_correlation_matrix(
    corr: ArrayLike,
    *,
    ax: plt.Axes | None = None,
    param_names: Sequence[str] | None = None,
    param_units: Sequence[str] | None = None,
    title: str = "Correlation matrix",
    cmap: str = "bwr",
    show_cbar: bool = True,
    font_size: float = 9,
    label_rotation: float = 0,
) -> tuple[plt.Figure, plt.Axes]:
    r"""Plot the correlation matrix.

    Examples
    --------
    >>> corr = correlation_matrix(fim=fim)
    >>> names = ["$f_0$", "$d_L$", "$\phi_0$"]
    >>> units = ["Hz", "Mpc", "rad"]
    >>> fig, ax = plot_correlation_matrix(corr, param_names=names, param_units=units)
    >>> fig.savefig("correlation_matrix.pdf", bbox_inches="tight")

    Parameters
    ----------
    corr : Array-like of shape ``(Np, Np)``
        Correlation matrix. Here, ``Np`` is the number of parameters.
    ax : Axes or None, optional
        Matplotlib axes. If None, a new figure is created.
    param_names : Sequence of ``Np`` str or None, optional
        Parameter names. By default, the parameters are labeled with their
        indices.
    param_units : Sequence of ``Np`` str or None, optional
        Parameter units. By default, the parameters are labeled without units.
    title : str, optional
        Figure title.
    cmap : str, optional
        Colormap. See `matplotlib colormaps
        <https://matplotlib.org/stable/gallery/color/colormap_reference.html>`_.
    show_cbar: bool, optional
        If True, show colorbar.
    font_size : float, optional
        Font size.
    label_rotation : float, optional
        Rotation angle for x-axis parameter labels.

    Returns
    -------
    Figure
        Matplotlib figure.
    Axes
        Matplotlib axes.
    """
    # pylint: disable=consider-using-f-string

    # Create figure and axes if not provided
    if ax is None:
        fig, ax = plt.subplots()
    else:
        assert isinstance(ax.figure, plt.Figure)
        fig = ax.figure

    # Check correlation matrix shape
    corr = jnp.asarray(corr)
    n_params = corr.shape[0]

    # Configure axes and add labels
    _setup_axes(
        ax,
        n_params=n_params,
        param_names=param_names,
        param_units=param_units,
        title=title,
        font_size=font_size,
        label_rotation=label_rotation,
    )

    # Plot color squares and values
    cmap_obj = plt.cm.get_cmap(cmap)
    for i, j in product(range(n_params), repeat=2):

        # Skip upper triangle
        if i > j:
            continue

        value = corr[i, j]
        latex = (
            _format_number_as_latex(value)
            if i == j
            else r"${\mathrm{" + "{:0.2f}".format(float(value)) + r"}}$"
        )

        center = (0.5 + i, 0.5 + j)
        rect_anchor = (center[0] - 0.5, center[1] - 0.5)
        rect = plt.Rectangle(rect_anchor, 1, 1, fill=True, linewidth=0)
        text = plt.Text(*center, latex, ha="center", va="center", size=font_size)

        if i == j:
            rect.set_color("lightgrey")
            text.set_color("black")
        if i < j:
            text_color = "black" if abs(value) < 0.5 else "white"
            text.set_color(text_color)
            text.set_fontweight("bold")
            rect_color = cmap_obj(0.5 + 0.5 * value)
            assert isinstance(rect_color, tuple)
            rect.set_color(rect_color)

        ax.add_patch(rect)
        ax.add_artist(text)

    ax.set_aspect("equal")

    if show_cbar:
        norm = mpl.colors.Normalize(vmin=-1, vmax=1)
        scalar_map = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
        cax = inset_axes(ax, width="5%", height="30%", loc="upper right", borderpad=1.5)
        cbar = plt.colorbar(scalar_map, cax=cax, orientation="vertical")
        cbar.ax.tick_params(labelsize=font_size)
        cbar.ax.yaxis.set_ticks_position("left")
        cbar.set_label("Correlation", fontsize=font_size, labelpad=5)

    return fig, ax


def _setup_axes(
    ax: plt.Axes,
    *,
    param_names: Sequence[str] | None,
    param_units: Sequence[str] | None,
    title: str,
    font_size: float,
    label_rotation: float,
    n_params: int,
) -> None:
    """Setup axes and add labels for the correlation matrix plot.

    Parameters
    ----------
    ax : Axes
        Matplotlib axes.
    param_names : Sequence of ``n_params`` str or None
        Parameter names.
    param_units : Sequence of ``n_params`` str or None
        Parameter units.
    title : str
        Figure title.
    font_size : float
        Font size.
    label_rotation : float
        Rotation angle for x-axis parameter labels.
    n_params : int
        Number of parameters.
    """
    # Check if parameter names and units are provided
    if param_names is None:
        param_names = [f"$p_{i}$" for i in range(n_params)]
    if len(param_names) != n_params:
        raise ValueError("Number of parameter names must match the matrix size.")
    if param_units is None:
        param_units = [""] * n_params
    if len(param_units) != n_params:
        raise ValueError("Number of parameter units must match the matrix size.")

    # Configure axes and labels
    ax.set_xlim(0, n_params)
    ax.set_ylim(0, n_params)
    ax.invert_yaxis()  # so it goes from top to bottom
    ax.set_xticks(np.arange(n_params) + 0.5)  # ticks in the middle of the squares
    ax.set_yticks(np.arange(n_params) + 0.5)  # ticks in the middle of the squares

    param_labels = [
        f"{name} [{unit}]" if unit else name
        for name, unit in zip(param_names, param_units, strict=True)
    ]
    ax.set_xticklabels(param_labels, size=font_size, rotation=label_rotation)
    ax.set_yticklabels(param_labels, size=font_size)
    ax.xaxis.set_ticks_position("bottom")
    ax.xaxis.set_label_position("bottom")

    ax.set_title(title, fontsize=1.4 * font_size)


def _format_number_as_latex(x, digits=2) -> str:
    """Format number in LaTeX style.

    Parameters
    ----------
    x : float
        Number to format.
    digits : int
        Number of significant digits.

    Returns
    -------
    str
        Formatted number.
    """

    if np.isnan(x):
        return "NaN"

    fmt = "{:." + str(digits) + "e}"
    a, n = fmt.format(x).split("e")

    if int(n) == 0:
        fmt = "{:." + str(digits) + "f}"
        return f"${fmt.format(x)}$"

    return f"${a}$ \n $\\times 10^{{{int(n)}}}$"
