r"""
Fisher information matrix
=========================

Use this module to compute Fisher Information Matrices (FIM) for set of
observables, assuming a Gaussian-noise matched filter-like likelihood.

Noise-weighted inner products
-----------------------------

Noise-weighted inner products are used to compute the Fisher Information Matrix.
They are defined as

.. math::

    (a|b) = 4 \Re \int_{f_{\min}}^{f_{\max}} \tilde{a}(f) \Sigma^{-1}(f)
    \tilde{b}^+(f) \, \mathrm{d}f,

where :math:`\tilde{a}(f)` and :math:`\tilde{b}(f)` are single or multi-channel
complex-valued Fourier transforms of the observables :math:`a(t)` and
:math:`b(t)`. The noise covariance matrix :math:`\Sigma(f)` characterizes the
noise correlations between the various observable channels.

.. autofunction:: univariate_inner_product

.. autofunction:: inner_product

FIM computation
---------------

Use the :func:`matched_filter_gaussian_fim` function to compute the Fisher
Information Matrix from a Jacobian function. The function returns another
function, which can evaluate the Fisher Information Matrix for a set of
parameters.

.. autofunction:: matched_filter_gaussian_fim

.. autoclass:: FIMFunction
    :members:

"""

from __future__ import annotations

from typing import Callable, Protocol

import jax.numpy as jnp
from jax import Array
from jax._src.typing import ArrayLike as JaxArrayLike

from wejax.jacobian import Jacobian


def univariate_inner_product(
    a: Array,
    b: Array,
    noise_psd: Array,
    *,
    df: float,
    sum_func: Callable = jnp.trapezoid,
) -> Array:
    r"""Compute the noise-weighted inner product of two univariate observables.

    The inner product is computed in the frequency domain, and for two
    univariate real-valued observables. The inner product is defined as

    .. math::

        (a|b) = 4 \Re \int_0^\infty \frac{\tilde{a}(f) \tilde{b}^*(f)}{S(f)} \,
        \mathrm{d}f,

    where :math:`\tilde{a}(f)` and :math:`\tilde{b}(f)` are the Fourier
    transforms of the observables :math:`a(t)` and :math:`b(t)`, respectively,
    and :math:`S(f)` is the one-sided power spectral density of the noise.

    Note that we assume here that the noise is stationary, such that there is no
    correlation between the noise at different frequencies; ie., the noise power
    spectral density characterizes the noise power at each frequency.

    For multivariate observables, use :func:`inner_product` instead.

    Example
    -------
    >>> result = univariate_inner_product(a, b, my_psd, df=df)

    Parameters
    ----------
    a, b : Array of shape ``(..., Nf)``
        Discrete Fourier transforms for the observables to compute the
        inner product of. Since the signals are assumed to be real, we only need
        the positive frequencies, as returned by :func:`jax.numpy.fft.rfft`.

        Here, ``Nf`` is the number of frequencies and ``...`` are any additional
        dimensions.
    noise_psd : Array of shape ``(..., Nf)``
        Noise covariance matrix [/Hz].

        Here ``Nf`` is the number of frequencies and ``...`` are any additional
        dimensions.
    df
        Frequency spacing [Hz].
    sum_func : Callable, default :func:`jax.numpy.trapezoid`
        Function to use to sum over the frequencies.

        The function should take as first positional argument an JAX Array, and
        should accept the keyword arguments `dx` and `axis`. It should return an
        array of shape ``(...)``, where ``...`` are any additional dimensions.

        We suggest using :func:`jax.numpy.trapezoid`, or :func:`jax.numpy.sum`.

    Returns
    -------
    Array of shape ``(...)``
        Noise-weighted inner product.
    """
    # Convert to JAX arrays
    a = jnp.asarray(a)  # (..., Nf)
    b = jnp.asarray(b)  # (..., Nf)
    a, b = jnp.broadcast_arrays(a, b)  # (..., Nf)
    noise_psd = jnp.asarray(noise_psd)  # (..., Nf)

    # Compute the integrand
    integrand = a * jnp.conj(b) / noise_psd  # (..., Nf)

    # Sum over the frequencies
    return 4 * jnp.real(sum_func(integrand, dx=df, axis=-1))  # (...)


def inner_product(
    a: Array,
    b: Array,
    noise_cov: Array,
    *,
    df: float,
    should_invert_noise_cov: bool = True,
    sum_func: Callable = jnp.trapezoid,
) -> Array:
    r"""Compute the noise-weighted inner product of two sets of observables.

    The inner product is computed in the frequency domain, and for two
    sets of real-valued observables. The inner product is defined as

    .. math::

        (a|b) = 4 \Re \int_0^\infty \tilde{a}(f) \Sigma^{-1}(f)
        \tilde{b}^+(f) \, \mathrm{d}f,

    where :math:`\tilde{a}(f)` and :math:`\tilde{b}(f)` are the Fourier
    transforms of the sets of observables :math:`a(t)` and :math:`b(t)`,
    respectively, and :math:`\Sigma(f)` is the noise covariance matrix.

    By default, the inverse of the noise covariance matrix is computed and used
    to compute the inner product. If you want to provide the inverse noise
    covariance matrix directly, set `should_invert_noise_cov` to `False`.

    Note that we assume here that the noise is stationary, such that there is no
    correlation between the noise at different frequencies (i.e., the noise
    covariance matrix is frequency-dependent and only characterize the noise
    correlations between the various observables channels).

    For univariate observables, use :func:`univariate_inner_product` instead.

    Example
    -------
    >>> result = inner_product(a, b, noise_cov=noise_cov, df=df)

    Parameters
    ----------
    a, b : Array of shape ``(..., Nf, Nc)``
        Discrete Fourier transforms for the observables to compute the
        inner product of. Since the signals are assumed to be real, we only need
        the positive frequencies, as returned by :func:`jax.numpy.fft.rfft`.

        Here, ``Nf`` is the number of frequencies, ``Nc`` is the number of
        observable channels, and ``...`` are any additional dimensions.
    noise_cov : Array of shape ``(..., Nf, Nc, Nc)``
        Noise covariance matrix [/Hz].

        Here ``Nf`` is the number of frequencies, ``Nc`` is the number of
        observable channels, and ``...`` are any additional dimensions.
    df
        Frequency spacing [Hz].
    should_invert_noise_cov : bool, optional
        If `True`, the inverse of the noise covariance matrix is computed and
        used to compute the inner product. If `False`, the provided
        `noise_cov` is used directly as the inverse noise covariance matrix.
    sum_func : Callable, default :func:`jax.numpy.trapezoid`
        Function to use to sum over the frequencies.

        The function should take as first positional argument an JAX Array, and
        should accept the keyword arguments `dx` and `axis`. It should return an
        array of shape ``(...)``, where ``...`` are any additional dimensions.

        We suggest using :func:`jax.numpy.trapezoid`, or :func:`jax.numpy.sum`.

    Returns
    -------
    Array of shape ``(...)``
        Noise-weighted inner product.
    """
    # Inverse noise covariance matrix if needed
    if should_invert_noise_cov:
        inv_noise_cov = jnp.linalg.inv(noise_cov)  # (..., Nf, Nc, Nc)
    else:
        inv_noise_cov = noise_cov  # (..., Nf, Nc, Nc)

    # Convert to JAX arrays
    a = jnp.asarray(a)  # (..., Nf, Nc)
    b = jnp.asarray(b)  # (..., Nf, Nc)
    a, b = jnp.broadcast_arrays(a, b)  # (..., Nf, Nc)

    # Contract over the channel axis
    subscripts = "...i, ...ij, ...j -> ..."
    contracted = jnp.einsum(subscripts, a, inv_noise_cov, jnp.conj(b))

    # Sum over the frequencies
    summed = 4 * jnp.real(sum_func(contracted, dx=df, axis=-1))  # (...)
    return summed


class FIMFunction(Protocol):  # pylint: disable=too-few-public-methods
    """Protocol for Fisher Information Matrices functions.

    Parameters
    ----------
    *args : Array-like
        Model parameters as positional arguments.

    Returns
    -------
    Array of shape ``(..., Np, Np)``
        The Fisher Information Matrix evaluated at ``args``.

        Here ``Np`` is the number of parameters, and ``...`` are any additional
        dimensions returned by the Jacobian function.
    """

    def __call__(self, *args: JaxArrayLike) -> Array: ...


def matched_filter_gaussian_fim(
    jacobian: Jacobian,
    noise_cov: Array,
    *,
    df: float,
    should_invert_noise_cov: bool = True,
    sum_func: Callable = jnp.trapezoid,
) -> FIMFunction:
    r"""Return a function that computes the Fisher Information Matrix.

    Compute the Fisher Information Matrix for a template function, assuming a
    stationary Gaussian noise. The Fisher Information Matrix is given by

    .. math::

        I_{ij}(\theta) = \left( \frac{\partial h}{\partial \theta_i} \middle|
        \frac{\partial h}{\partial \theta_j} \right).

    The returned function can be called with a set of parameters, and will
    return the Fisher Information Matrix evaluated at those parameters.

    Example
    -------
    >>> fim = matched_filter_gaussian_fim(jacobian, noise_cov=noise_cov, df=df)
    >>> result_1 = fim(1.0, 2.0)
    >>> result_2 = fim(3.0, 4.0)

    The returned FIM function can be vectorized for efficient computation of
    multiple sets of parameters using :func:`jax.vmap` (see `JAX documentation
    <https://docs.jax.dev/en/latest/_autosummary/jax.vmap.html>`_).

    >>> vmap_fim = jax.vmap(fim, in_axes=(0, 0), out_axes=0)

    Parameters
    ----------
    jacobian : :class:`Jacobian`
        Jacobian function.
    noise_cov : Array of shape ``(..., Nf, Nc, Nc)``
        Noise covariance matrix [/Hz].

        Here ``Nf`` is the number of frequencies, ``Nc`` is the number of
        observable channels, and ``...`` are any additional dimensions.
    df
        Frequency spacing [Hz].
    should_invert_noise_cov : bool, optional
        If `True`, the inverse of the noise covariance matrix is computed and
        used to compute the inner product. If `False`, the provided
        `noise_cov` is used directly as the inverse noise covariance matrix.
    sum_func : Callable, default :func:`jax.numpy.trapezoid`
        Function to use to sum over the frequencies.

        The function should take as first positional argument an JAX Array, and
        should accept the keyword arguments `dx` and `axis`. It should return an
        array of shape ``(...)``, where ``...`` are any additional dimensions.

        We suggest using :func:`jax.numpy.trapezoid`, or :func:`jax.numpy.sum`.

    Returns
    -------
    :class:`FIMFunction`
        A function that computes the Fisher Information Matrix for a set of
        parameters.
    """

    def fim(*args: JaxArrayLike) -> Array:

        # Evaluate the Jacobian
        jacobian_val = jacobian(*args)  # (..., Nf, Nc, Np)
        jacobian_val = jnp.moveaxis(jacobian_val, -1, -3)  # (..., Np, Nf, Nc)

        # Compute inner product column by column
        fim_columns = [
            inner_product(
                jacobian_val,
                jacobian_val[..., [i], :, :],
                noise_cov,
                df=df,
                sum_func=sum_func,
                should_invert_noise_cov=should_invert_noise_cov,
            )  # (..., Np)
            for i in range(len(args))
        ]

        return jnp.stack(fim_columns, axis=-1)  # (..., Np, Np)

    return fim
