
[![PyPI - Version](https://img.shields.io/pypi/v/FeNNol?link=https%3A%2F%2Fpypi.org%2Fproject%2FFeNNol%2F)](https://pypi.org/project/FeNNol/)
[![DOI:10.1063/5.0217688](https://zenodo.org/badge/DOI/10.1063/5.0217688.svg)](https://doi.org/10.1063/5.0217688) 


## FeNNol: Force-field-enhanced Neural Networks optimized library
FeNNol is a library for building, training and running neural network potentials for molecular simulations. It is based on the JAX library and is designed to be fast and flexible.

FeNNol's documentation is available [here](https://fennol-tools.github.io/FeNNol/) and the article describing the library at https://doi.org/10.1063/5.0217688

Active Learning tutorial in this [Colab notebook](https://colab.research.google.com/drive/1Z3G_jVSF60_nbDdJwbgyLdJBHTYuQ5nL?usp=sharing)

## Installation
### From PyPI
```bash
# CPU version
pip install fennol

# GPU version
pip install "fennol[cuda]"
```

### Latest version from Github repo
You can start with a fresh environment, for example using venv:
```bash
python -m venv fennol
source fennol/bin/activate
```

The first step is to install jax (see details at: https://jax.readthedocs.io/en/latest/installation.html). For example, to install the latest version using pip:
```bash
# CPU version
pip install -U jax

# GPU version
pip install -U "jax[cuda12]"
```

Then, you can clone the repo and install FeNNol using pip:
```bash
git clone https://github.com/FeNNol-tools/FeNNol.git
cd FeNNol
pip install .
```

### Optional dependencies
- Some modules require e3nn-jax (https://github.com/e3nn/e3nn-jax) which can be installed with:
```bash
pip install --upgrade e3nn-jax
```
- The provided training script requires pytorch (at least the cpu version) for dataloaders:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```
- For the Deep-HP interface, cffi and pycuda are required:
```bash
pip install cffi pycuda
```

## Examples
To learn how to train a FeNNol model, you can check the examples in the [`examples/training`](https://github.com/fennol-tools/FeNNol/tree/main/examples/training) directory. The `README.md` file in that directory contains instructions on how to train a model on the aspirin revMD17 dataset.

To learn how to run molecular dynamics simulations with FeNNol models, you can check the examples in the [`examples/md`](https://github.com/fennol-tools/FeNNol/tree/main/examples/md) directory. The `README.md` file in that directory contains instructions on how to run simulations with the provided ANI-2x model.


## Citation

Please cite this paper if you use the library.
```
T. Plé, O. Adjoua, L. Lagardère and J-P. Piquemal. FeNNol: an Efficient and Flexible Library for Building Force-field-enhanced Neural Network Potentials. J. Chem. Phys. 161, 042502 (2024)
```

```
@article{ple2024fennol,
    author = {Plé, Thomas and Adjoua, Olivier and Lagardère, Louis and Piquemal, Jean-Philip},
    title = {FeNNol: An efficient and flexible library for building force-field-enhanced neural network potentials},
    journal = {The Journal of Chemical Physics},
    volume = {161},
    number = {4},
    pages = {042502},
    year = {2024},
    month = {07},
    doi = {10.1063/5.0217688},
    url = {https://doi.org/10.1063/5.0217688},
}

```

## License

This project is licensed under the terms of the GNU LGPLv3 license. See [LICENSE](https://github.com/fennol-tools/FeNNol/blob/main/LICENSE) for additional details.
