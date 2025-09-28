r"""
Templates and Jacobians
=======================

This module provides functions to evaluate the Jacobian of a template function.

Templates
---------

Template functions model the observed data. In this framework, we assume they
are given in the Fourier domain as complex-valued functions of the model
parameters and frequencies,

.. math::

    h_i(\theta)(f),

where :math:`i` is the channel (observable) index, :math:`\theta` is a set of
model parameters, and :math:`f` is the frequency vector.

The implementation of the template function is expected to be in JAX. It should
be a function of the model parametrers as positional arguments and return an
array of complex values for all frequencies and channels.

.. autoclass:: Template

Jacobians
---------

Given a template function :math:`h_i(\theta, f)` that depends on a set of
parameters :math:`\theta` and frequencies :math:`f`, the Jacobian is a
matrix of partial derivatives of the template with respect to the model
parameters,

.. math::

    J_{ij}(\theta)(f) = \frac{\partial h_i}{\partial \theta_j}(\theta)(f).

The implementation of the Jacobian function is expected to be in JAX. It should
be a function of the model parameters as positional arguments and return an
array of complex values for all frequencies, channels, and parameters (along
which the partial derivatives are computed).

.. autoclass:: Jacobian

This module provides convenience functions to compute Jacobians using automatic
differentiation and finite differences. It also provides a function to mix
multiple Jacobians along the parameter axis.

Automatic differentiation
^^^^^^^^^^^^^^^^^^^^^^^^^

The :func:`autograd` function computes the Jacobian using automatic
differentiation. This function uses JAX forward-mode automatic differentiation
to compute the Jacobian of the template function.

.. note:: Vectorization

    To vectorize the computation of the Jacobian for multiple sets of
    parameters, use :func:`jax.vmap` on the non-vectorized Jacobian function, to
    avoid computing partial derivatives for each parameter array element.

.. autofunction:: autograd

Finite differences
^^^^^^^^^^^^^^^^^^

The :func:`findiff` function computes the Jacobian using finite differences.
This function uses numerical differentiation to compute the Jacobian of the
template function.

The function requires a set of steps for numerical differentiation. These can
be either a scalar or an array with the same shape as the parameters to
differentiate. If a scalar, the same step is used for all parameters.

.. autofunction:: findiff

Mixing Jacobians
^^^^^^^^^^^^^^^^

The :func:`mix` function concatenates multiple Jacobians along the parameter
axis, based on the given argument indices.

.. autofunction:: mix

"""

from __future__ import annotations

from typing import Callable, Sequence, TypeAlias

import jax
import jax.numpy as jnp
import numpy as np
from jax import Array
from jax._src.typing import ArrayLike as JaxArrayLike
from numpy.typing import ArrayLike as NumpyArrayLike

Template: TypeAlias = Callable[..., Array]
r"""Template function.

Example
-------
Below is an example of a template function that models a single channel
with two parameters.

.. code-block:: python

    import jax.numpy as jnp
    from jax import Array

    freqs = jnp.linspace(0, 1, 10)

    def template(a: float, b: float) -> Array:
        channel = a**2 * freqs + 42j * jnp.cos(a) * b**2
        return jnp.stack([channel], axis=-1)

    template(1.0, 2.0)

This template can be vectorized for efficient computation of multiple sets
of parameters using :func:`jax.vmap` (see `JAX documentation
<https://docs.jax.dev/en/latest/_autosummary/jax.vmap.html>`_).

.. code-block:: python

    from jax import vmap

    a = jnp.array([1.0, 2.0, 3.0])
    b = jnp.array([4.0, 5.0, 6.0])
    vtemplate = vmap(template, in_axes=(0, 0), out_axes=0)
    vtemplate(a, b)

Parameters
----------
*args : Array-like
    Model parameters as positional arguments.

Returns
-------
Complex-valued array
    Template values.

    The returned shape is often ``(..., Nf, Nc)``, with ``Nf`` is the number
    of frequencies, ``Nc`` is the number of channels. The ellipsis
    represents any number of additional dimensions.
"""

Jacobian: TypeAlias = Callable[..., Array]
r"""Jacobian function.

    Example
    -------
    .. code-block:: python

        import jax.numpy as jnp
        from jax import Array

        freqs = jnp.linspace(0, 1, 10)

        def jac(a: float, b: float) -> Array:
            # Compute Jacobian elements
            jac_0 = jnp.stack([2 * a * freqs - 42j * b**2 * jnp.sin(a)], axis=-1)
            jac_1 = jnp.stack([84j * jnp.cos(a) * b * jnp.ones_like(freqs)], axis=-1)

            return jnp.stack([jac_0, jac_1], axis=-1)

        jac(1.0, 2.0)

    This Jacobian can be vectorized for efficient computation of multiple sets
    of parameters using :func:`jax.vmap` (see `JAX documentation
    <https://docs.jax.dev/en/latest/_autosummary/jax.vmap.html>`_).

    .. code-block:: python

        from jax import vmap

        a = jnp.array([1.0, 2.0, 3.0])
        b = jnp.array([4.0, 5.0, 6.0])
        vjac = vmap(jac, in_axes=(0, 0), out_axes=0)
        vjac(a, b)

    Parameters
    ----------
    *args : Array-like
        Model parameters as positional arguments.

    Returns
    -------
    Complex-valued array
        Template Jacobian values.

        The returned shape is often ``(..., Nf, Nc, Np)``, with ``Nf`` is the
        number of frequencies, ``Nc`` is the number of channels, and ``Np`` the
        number of parameters. The ellipsis represents any number of additional
        dimensions.
    """


def autograd(template: Template, argnums: Sequence[int]) -> Jacobian:
    r"""Compute the Jacobian of a function using automatic differentiation.

    This function use JAX forward-mode (column-wise :func:`jax.jacfwd`)
    automatic differentiation to compute the Jacobian of the template function.

    Example
    -------
    >>> from wejax.jacobian import autograd
    >>> jac = autograd(template, argnums=(0, 1))
    >>> jac(1.0, 2.0)
    Array([[[[...]]]], dtype=complex64)

    Parameters
    ----------
    template : :class:`Template`
        Template function, implemented in JAX.
    argnums : Sequence[int]
        Indices of the positional arguments to differentiate with respect to.

    Returns
    -------
    :class:`Jacobian`
        Jacobian function.
    """

    def jac(*args: JaxArrayLike) -> Array:
        return jnp.stack(
            jax.jacfwd(template, argnums=argnums)(*args),
            axis=-1,
        )

    return jac


def findiff(
    template: Template, argnums: Sequence[int], steps: NumpyArrayLike
) -> Jacobian:
    r"""Compute the Jacobian of a function using finite differences.

    This function use numerical differentiation to compute the Jacobian of the
    template function,

    .. math::

        J_{ij}(\theta)(f) = \frac{h_i(\theta + \delta_j)(f) - h_i(\theta -
        \delta_j)(f)}{2 \delta_j},

    where :math:`h_i(\theta)` is the template function, :math:`\theta` is the
    model parameters, :math:`f` is the frequency vector, and :math:`\delta_j`
    is the step for numerical differentiation.

    Example
    -------
    >>> from wejax.jacobian import findiff
    >>> jac = findiff(template, argnums=(0, 1), steps=(1e-6, 2e-6))
    >>> jac(1.0, 2.0)
    Array([[[[...]]]], dtype=complex64)

    Parameters
    ----------
    template : :class:`Template`
        Template function, implemented in JAX.
    argnums : Sequence[int]
        Indices of the positional arguments to differentiate with respect to.
    steps: Array-like
        Steps for numerical differentiation.

        These can be either a scalar or an array with the same shape as the
        parameters to differentiate. If a scalar, the same step is used for
        all parameters.

    Returns
    -------
    :class:`Jacobian`
        Jacobian function.
    """
    # Broadcast steps
    n_params = len(argnums)
    steps = np.broadcast_to(steps, (n_params,))

    def jac(*args: JaxArrayLike) -> Array:

        # Broadcast and stack parameters
        params = jnp.stack(
            jnp.broadcast_arrays(*args),
            axis=0,
        )

        # Compute finite differences per parameter
        findiffs = []
        for i, argnum in enumerate(argnums):
            left = params.at[argnum].subtract(steps[i])
            right = params.at[argnum].add(steps[i])
            diff = (template(*right) - template(*left)) / (2 * steps[i])
            findiffs.append(diff)

        return jnp.stack(findiffs, axis=-1)

    return jac


def mix(
    jacobians: Sequence[Jacobian],
    argnums: Sequence[Sequence[int]],
    sort_args: bool = False,
) -> Jacobian:
    r"""Concatenate Jacobians along the parameter axis.

    This function concatenates multiple Jacobians along the parameter axis,
    based on the given argument indices.

    Example
    -------
    >>> from wejax.jacobian import autograd, findiff, mix
    >>> jac1 = autograd(template1, argnums=(1,))
    >>> jac2 = findiff(template2, argnums=(0,), steps=1e-6)
    >>> jac = mix([jac1, jac2], argnums=[(1,), (0,)])
    >>> associated_argnums = (0, 2, 1,)

    You can sort the arguments before concatenating the Jacobians by setting
    ``sort_args=True``.

    >>> jac = mix([jac1, jac2], argnums=[(1,), (0,)], sort_args=True)
    >>> associated_argnums = (0, 1)

    Parameters
    ----------
    jacobians : Sequence[Jacobian]
        List of Jacobian functions.
    argnums : Sequence[Sequence[int]]
        List of lists of indices of argument indices attached to each Jacobian,
        in the same order as ``jacobians``.
    sort_args : bool, optional
        Whether to sort the arguments (i.e., Jacobian columns) before
        concatenating the Jacobians.

    Returns
    -------
    :class:`Jacobian`
        Mixed Jacobian function.
    """
    # Make sure indices are not repeated
    flat_argnums = [argnum for indices in argnums for argnum in indices]
    if len(flat_argnums) != len(set(flat_argnums)):
        raise ValueError("Indices in `argnums` must not be repeated.")

    # For each parameter, find out which Jacobian it belongs to and its index
    # That will allow us to concatenate the Jacobians along the parameter axis
    param_indices: list[tuple[int, int]]
    if sort_args:
        # To sort the arguments, prepare a list with placeholder tuples and
        # then populate it with the actual indices
        param_indices_temp: list[tuple[int, int] | None] = [None] * len(flat_argnums)
        for i, indices in enumerate(argnums):
            for j, index in enumerate(indices):
                param_indices_temp[index] = (i, j)
        # Assert that all indices were populated
        param_indices = [x for x in param_indices_temp if x is not None]
        if param_indices_temp != param_indices:
            raise RuntimeError("Could not sort the arguments.")
    else:
        # Here it's easier: just go through the argnums list and populate the
        # param_indices list with the actual Jacobian and parameter indices
        param_indices = [(i, j) for i, indices in enumerate(argnums) for j in indices]

    def jac(*args: JaxArrayLike) -> Array:
        jac_values = [jacobian(*args) for jacobian in jacobians]
        jac_columns = [jac_values[i][..., j] for i, j in param_indices]
        return jnp.stack(jac_columns, axis=-1)

    return jac
