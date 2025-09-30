# nsEVDx: A python Library for modelling non-stationary extreme value distributions

![Python](https://img.shields.io/badge/python-3.9%252B-blue) ![License](https://img.shields.io/badge/license-MIT-green)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15850043.svg)](https://doi.org/10.5281/zenodo.15850043)
[![PyPI version](https://img.shields.io/pypi/v/nsEVDx)](https://pypi.org/project/nsEVDx/)
[![PyPI downloads](https://pepy.tech/badge/nsEVDx)](https://pepy.tech/project/nsEVDx)
[![GitHub issues](https://img.shields.io/github/issues/nischalcs50/nsEVDx)](https://github.com/nischalcs50/nsEVDx/issues)
[![GitHub stars](https://img.shields.io/github/stars/nischalcs50/nsEVDx?style=social)](https://github.com/nischalcs50/nsEVDx)


`nsEVDx` is a Python library for estimating the parameters of Generalized Extreme Value (GEV) and Generalized Pareto Distributions (GPD), collectively referred to as extreme value distributions (EVDs), under both stationary and non-stationary assumptions, using frequentist and Bayesian methods. Designed for hydrologists, climate scientists, and engineers, especially those working on extreme rainfall or flood frequency analysis, it supports time-varying covariates, MCMC samplings (Metropolis hasting-Randomwalk, Adjusted Langevin Algorithm, Hamiltonian Monte Carlo) and essential model diagnostics. Although developed for environmental extremes, its features are broadly applicable to financial risk modeling and other domains concerned with rare, high-impact events.

## Features

-   Fits stationary and nonstationary EVDs
-   Supports Frequentist and Bayesian inference
-   Transparent, fully customizable MCMC engine implemented in NumPy
-   Advanced samplers: Metropolis Hasting RandomWalk, Metropolis Adjusted Langevin Algorithm (MALA), and Hamiltonian Monte Carlo (HMC)
-   Support arbitratry covariates in location, scale and shape parameters
-   Integrated diagnostic tools: trace plots, acceptance rates, and bayesian metrics
-   Visualization tool for posterior summaries
-   Lightweight and minimal dependency, only `numpy, scipy, matplotlib, seaborn`

## Implementation

The core `NonStationaryEVD` class handles parameter parsing, log-likelihood construction, prior specification, and proposal generation. Frequentist estimation uses `scipy.optimize` to minimize the negative log-likelihood, while Bayesian MCMC methods are implemented in `numpy` for transparency and flexibility.

Non-stationarity is controlled via a configuration vector `config = [a, b, c]`, where each entry specifies the number of covariates used to model the location, scale, and shape parameters of the EVD. Entry with a value of `0` implies stationarity, while values `> 0` indicate non-stationary modeling using that many covariates.

In Bayesian estimation, `nsEVDx` can infer prior specifications based on the data and configuration or accept user-defined priors. In the frequentist mode, it can determine suitable parameter bounds automatically. However, user defined priors or bounds are recommended for better convergence and interpretability.

### Config design

This package allows modeling the extreme value distribution (EVD) parameters as functions of covariates. Each parameter can be configured independently:

-   `location_model`: "constant" or "linear"
-   `scale_model`: "constant" or "exponential"
-   `shape_model`: "constant" or "linear"

Internally, these options apply a regression of the form:

-   Linear: θ(t) = θ₀ + θ₁·X(t)
-   Exponential: θ(t) = exp(θ₀ + θ₁·X(t))

This gives flexibility to model non-stationarity while maintaining parsimony.


Note: Polynomial relationships between the covariates and the parameters can be modeled by raising the power of the covariates before passing them into the model.

Splines : Comming soon...

## Installation

**For regular users**

``` bash
pip install nsEVDx  

# Or clone from GitHub:
git clone https://github.com/Nischalcs50/nsEVDx
cd nsEVDx
pip install .
```

**For developers/contributors**

``` bash
git clone https://github.com/Nischalcs50/nsEVDx
cd nsEVDx
pip install -e .[dev]
```

## Quick Start

``` python
from nsEVDx import NonStationaryEVD

sampler = NonStationaryEVD(...)
posterior, acc_rate = sampler.MH_RandWalk(...)
```

## Documentation
-   Webpage manual is here [user manual](https://Nischalcs50.github.io/nsEVDx/)
-   See [Documentation](API_docs/) for full [API](API_docs/API.md).
-   See examples such as, [bayesian inference of non-stationary GEV parameters](../examples/example_GEV.ipynb), [bayesian metrics example](../examples/example_bayesian_metrics.ipynb), [frequentist estimation of non-stationary GPD parameter and likelihood ratio test](../examples/example_GPD_frequentist.ipynb), and [generation of random variates from non-stationary GEV](../examples/example_generating_rv_from_nsEVD.ipynb) . These examples highlight the library's key capabilities, including parameter estimation and simulation under non-stationary conditions.

## Usage

The usage document is available [here](docs/usage.md). For more details, see the usage examples in the Jupyter notebooks [here](examples/).

## Dependencies

-   numpy
-   scipy
-   matplotlib, seaborn (for plots)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use `nsEVDx` in your research, please cite:

Kafle, N., & Meier, C. I. (2025). nsEVDx: A Python library for modeling Non-Stationary Extreme Value Distributions. arXiv preprint [arXiv:2509.07261](https://arxiv.org/abs/2509.07261).

Kafle, N., & Meier, C. (2025). nsEVDx: A Python Library for Modeling Non-Stationary Extreme Value Distributions (v0.1.0). Zenodo. https://doi.org/10.5281/zenodo.15850043

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project, and refer to our [Code of Conduct](CODE_OF_CONDUCT.md) to foster an inclusive and respectful community.

## References

-   Betancourt, M. (2017). A Conceptual Introduction to Hamiltonian Monte Carlo. arXiv: Methodology.
-    Coles, S. (2007). An introduction to statistical modeling of extreme values (4th. printing). Springer. <https://doi.org/10.1007/978-1-4471-3675-0>
-   Gilleland, E. (2025). extRemes: Extreme Value Analysis. <https://doi.org/10.326> 14/CRAN.package.extRemes
-   Heffernan J. E., Stephenson A.G., & Gilleland E. (2003). Ismev: An Introduction to Statistical Modeling of Extreme Values. <https://CRAN.R-project.org/pa> ckage=ismev
-   Hosking, J. R. M., & Wallis, J. R. (1997). Regional Frequency Analysis: An Approach Based on L-Moments (Vol. 93). Cambridge University Press. <https://doi.org/10.1017/cbo97805> 11529443
-   IRSN. (2024). NSGEV: Non-Stationary GEV Time Series. <https://github.com> /IRSN/NSGEV/
-   Kafle, N., & Meier, C. (n.d.). Detecting trends in short duration extreme precipitation over SEUS using neighborhood based method. Manuscript in Preparation.
-   Kafle, N., & Meier, C. (2025). Evaluating Methodologies for Detecting Trends in Short-Duration Extreme Rainfall in the Southeastern United States. Extreme Hydrological or Critical Event Analysis-III, EWRI Congress 2025, Anchorage, AK, U.S. <https://alaska2025.eventscribe.net
-   Oriol Abril-Pla, Virgile Andreani, C. Carroll, L. Y. Dong, Christopher Fonnesbeck, Maxim Kochurov, Ravin Kumar, Junpeng Lao, Christian C. Luhmann, Osvaldo A. Martin, Michael Osthege, Ricardo Vieira, Thomas V. Wiecki, & Robert Zinkov. (2023). PyMC: A modern, and comprehensive probabilistic programming framework in Python. PeerJ Computer Science, 9, e1516--e1516. <https://doi.org/10.7717/peerj-cs.1516>
-   Paciorek, C. (2016). climextRemes: Tools for Analyzing Climate Extremes. <https://CRAN.R-project.org/package=climextRemes>
-   Robert, C. P., & Casella, G. (2009). Introducing Monte Carlo Methods with R. <https://doi.org/10.1007/978-1-4419-1576-4>
-   Roberts, G. O., & Tweedie, R. L. (1996). Exponential Convergence of Langevin Distributions and Their Discrete Approximations. Bernoulli, 2 (4), 341. <https://doi.org/10.2307/3318418>
-   Stan development Team. (2023a). CmdStan: The command-line interface to Stan. <https://mc-stan.org/users/interfaces/cmdstan>
-   Stan development Team. (2023b). PyStan: The python interface to Stan. <https://pystan.readthedocs.io/>
