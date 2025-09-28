# Ratemaking Tools

A comprehensive Python library for Property & Casualty actuarial ratemaking, providing tools for credibility analysis, trending, exposure calculations, and data processing.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

### Currently Available
- **Credibility Analysis**: Classical, Bühlmann, and Bayesian credibility methods
- **Comprehensive Testing**: Test suite with actuarial validation

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Classical Credibility

```python
from ratemaking_tools import (
    classical_full_credibility_frequency,
    classical_partial_credibility
)

# Calculate full credibility standard
n_full = classical_full_credibility_frequency(p=0.95, k=0.05)

# Calculate credibility factor  
z = classical_partial_credibility(n=observed_claims, n_full=n_full)

# Apply credibility blend
estimate = z * observed_rate + (1 - z) * complement_rate
```

### Bühlmann Credibility

```python
from ratemaking_tools import BuhlmannInputs, buhlmann

data = {"risk_1": [1.2, 1.5], "risk_2": [2.1, 1.9]}
result = buhlmann(BuhlmannInputs(data=data))
print(f"Credibility weights: {result.Z_by_risk}")
```

### Bayesian Credibility

```python
from ratemaking_tools import bayes_poisson_gamma

# Poisson-Gamma conjugate updating
posterior = bayes_poisson_gamma(
    prior_alpha=2.0, prior_beta=100.0,
    total_counts=15, total_exposure=120
)
print(f"Posterior mean: {posterior.mean}")
print(f"Credibility weight: {posterior.credibility_Z}")
```

## Package Structure

```
ratemaking_tools/
├── credibility/           # Credibility analysis tools
│   ├── classical.py      # Classical (Limited Fluctuation) credibility
│   ├── buhlmann.py       # Bühlmann & Bühlmann-Straub credibility
│   └── bayesian.py       # Bayesian credibility with conjugate priors
├── trending/             # Trending analysis tools (coming soon)
├── exposure/             # Exposure calculation tools (coming soon)
└── utils/                # Data processing utilities (coming soon)
```

## Modular Usage

For organized imports, use the submodules:

```python
# Organized by functionality
from ratemaking_tools.credibility import classical, buhlmann, bayesian

# Use specific functions
n_full = classical.classical_full_credibility_frequency(p=0.95, k=0.05)
```

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

## Development

### Setting up for development:

```bash
git clone https://github.com/YOUR_USERNAME/ratemaking-tools.git
cd ratemaking-tools
pip install -e .
pip install -e ".[test]"
```

## License

MIT License 
