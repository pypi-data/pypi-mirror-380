# WeJAX

Compute the Fisher Information Matrix (FIM) of your favorite models using
their Jacobians; take advantage of automatic differentiation if your model
is implemented in JAX to switly compute the Jacobian, or evaluate it
numerically with finite differences.

WeJAX also provide convenience fonctions to invert the FIM and compute error
bars and correlations on the estimated parameters, as well as nice-looking
plots.

## Contributing

This project uses Poetry for dependency management. To install the dependencies
and the project itself, run the following command:

```bash
poetry install
```

You can now run commands inside a dedicated virtual environment by running:

```bash
poetry run <your-command>
```
