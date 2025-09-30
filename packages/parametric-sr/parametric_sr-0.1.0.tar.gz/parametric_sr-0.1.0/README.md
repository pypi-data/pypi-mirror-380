# parametric-symbolic-regression

Parametric Symbolic Regression with Genetic Algorithm

## Table of Contents

- [parametric-symbolic-regression](#parametric-symbolic-regression)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
  - [Contributing](#contributing)
  - [License](#license)
  - [Citation](#citation)

## Overview

Parametric Symbolic Regression (PSR) is a Python package that evolves symbolic expressions whose parameters
can be optimized (e.g. with `curve_fit` or `minimize`). It combines genetic-programming style search over
expression structure with numeric optimization of continuous parameters, which can be applied as classical
symbolic regression for closed-form equations or more advanced scenarios like system (series of equations) identification.

This repository provides:

- Tree/FuncUnit/Expression primitives for building symbolic expressions.
- Generation, mutation and crossover operators for evolving populations of expressions.
- Fitting utilities using SciPy (`curve_fit` / `minimize`) to tune numeric parameters.
- Scoring, selection and simple utilities for batch evaluation and parallel execution.

## Features

- Mixed discrete (structure) + continuous (parameters) optimization.
- Batch scoring and configurable scoring strategies.
- Pluggable optimization backends (SciPy).
- Multi-processing support for parallel evaluation.
- Helpers for logging and reproducible random seeds.

## Installation

**Python 3.12+** is required for the latest type hint features. We may consider supporting older versions in the future.

Install from source (to get the latest features):

```bash
git clone https://github.com/SijieFu/parametric-symbolic-regression.git
cd parametric-symbolic-regression
python -m pip install -e .
```

For development, you may also want to install testing dependencies using `pip install -e ".[dev]"`, followed by `pre-commit install` to set up pre-commit hooks.

Or install from PyPI (to get the latest stable release):

```bash
pip install parametric-sr
```

## Quick Start

Basic usage example:

```python
import numpy as np

from psr import ParametricSR

# Generate synthetic data
X = np.random.random((100, 2))
y = 3.14 * X[:, 0] + X[:, 1] ** 2 + np.random.normal(size=100) * 0.1

# Initialize and fit the model
psr_model = ParametricSR(
    n_gen=10, n_per_gen=1000, n_survivor=30, n_jobs=-1, random_state=42, verbose=10
)
psr_model.fit(X, y)

# Evaluate the model
print("Best Expression:", psr_model.best_estimator_.format())
```

To enable logging, you can set the log file as follows:

```python
from psr import add_file_handler

add_file_handler(log_file="test.log")
```

To save the model and reload it later:

```python
import pickle

# Save the model
with open("psr_model.pkl", "wb") as f:
    pickle.dump(psr_model, f)

# Load the model
from psr import config

with config.inplace_update(), open("psr_model.pkl", "rb") as f:
    # inplace update is needed to sync the function registry
    loaded_model = pickle.load(f)
```

## Contributing

Contributions are welcome! Please open issues or pull requests on the GitHub repository.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## Citation

We are working on a paper that will be available soon (preprint forthcoming).

If you find this repository useful, please consider citing it.
