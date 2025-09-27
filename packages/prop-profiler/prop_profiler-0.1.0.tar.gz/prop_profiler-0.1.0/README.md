# Prop Profiler

A molecular property profiler for drug discovery applications. This package provides machine learning models to predict various molecular properties including water solubility (ESOL, mg/L), logD, most basic pKa and other essential chemical properties, along with drug-likeliness scores (e.g. CNS-MPO, Stoplight, QED scores).

## Features

- **Water Solubility (ESOL, mg/L)**: Predicts aqueous solubility using molecular descriptors
- **logD Prediction**: Estimates distribution coefficient at physiological pH
- **pKa Prediction**: Predicts most basic site using [MolGpKa](https://github.com/Xundrug/MolGpKa) *(requires `[pka]` extra)*
- **CNS-MPO Scoring**: Calculates Central Nervous System Multiparameter Optimization scores [Paper](https://pubs.acs.org/doi/10.1021/acschemneuro.6b00029) *(requires `[pka]` extra)*
- **Stoplight Scoring**: Provides color-coded molecular property assessments ([Stoplight](https://github.com/jimmyjbling/Stoplight))
- **Command Line Interface**: Easy-to-use CLI for batch processing

## Installation

### From PyPI (Recommended)
```bash
# Basic installation (without pKa/CNS-MPO prediction)
pip install prop-profiler

# Full installation with pKa prediction capabilities
pip install prop-profiler[pka]

# For development
pip install prop-profiler[pka,dev]
```

### From Source
```bash
# Clone the repository
git clone https://github.com/eneskelestemur/prop_profiler.git
cd prop_profiler

# Install in development mode
pip install -e .

# Or with all features
pip install -e .[pka,dev]
```

### Conda Environment (Alternative)
If you prefer conda environments:
```bash
# Create conda environment with all dependencies
conda env create -f environment.yml
conda activate prop-profiler
pip install -e .
```

### Verify Installation
```bash
# Test the command line interface
prop-profiler --help

# Test the Python API
python -c "from prop_profiler import profile_molecules; print('Installation successful!')"
```

## Quick Start

### Command Line Usage

```bash
# Show help message and available options
prop-profiler --help

# Profile molecules from a SMILES file
prop-profiler -i molecules.smi -o results.csv

# Profile molecules from an SDF file
prop-profiler -i molecules.sdf -o results.csv

# Skip CNS-MPO scoring for faster processing
prop-profiler -i molecules.smi -o results.csv --skip-cns-mpo

# Use GPU for pKa prediction
prop-profiler -i molecules.smi -o results.csv --device cuda
```

### Python API Usage

```python
from prop_profiler import profile_molecules

# Create some example smiles/molecules
smiles = ['CCO', 'CC(=O)O', 'c1ccccc1']

# Profile the molecules (basic features only)
results = profile_molecules(smiles, skip_cns_mpo=True, verbose=True)
print(results)

# Profile with CNS-MPO and pKa (requires [pka] extra)
# results = profile_molecules(smiles, verbose=True)
```

## Input Formats

- **SMILES files** (`.smi`): One SMILES string per line
- **SDF files** (`.sdf`): Standard structure-data format
- **CSV files** (`.csv`): Must contain a column with SMILES strings

## Output

The profiler returns a pandas DataFrame with the following columns:

- `smiles`: Input SMILES string
- `mw`: Molecular weight
- `logp`: Octanol-water partition coefficient
- `hba`: Hydrogen bond acceptors
- `hbd`: Hydrogen bond donors
- `tpsa`: Topological polar surface area
- `num_rotatable_bonds`: Number of rotatable bonds
- `fsp3`: Fraction of sp3 hybridized carbons
- `qed`: Quantitative Estimate of Drug-likeness
- `esol_mg/L`: Water solubility prediction (in mg/L)
- `stoplight_score`: Stoplight score (0-2) based on [Stoplight paper](https://pubs.acs.org/doi/10.1021/acs.jcim.4c00412)
- `stoplight_color`: Color-coded assessment (Green/Yellow/Red)

When CNS-MPO scoring is enabled (requires `[pka]` extra):
- `most_basic_pka`: Most basic pKa value
- `logd`: LogD prediction at pH 7.4
- `cns_mpo_score`: CNS-MPO score (0-6)

## Requirements

### Core Dependencies
- Python >= 3.8
- NumPy, Pandas for data handling
- RDKit for cheminformatics
- scikit-learn for machine learning
- matplotlib for plotting
- tqdm for progress bars

### Optional Dependencies (for pKa/CNS-MPO)
- PyTorch >= 2.0.0
- PyTorch Geometric >= 2.0.0

Install with: `pip install prop-profiler[pka]`

## License

MIT License - see LICENSE file for details.

## Third-Party Components

This package includes a modified version of MolGpKa for pKa prediction:
- **MolGpKa**: Graph-convolutional neural network for pKa prediction
- **Original Repository**: https://github.com/Xundrug/MolGpKa
- **License**: MIT License
- **Modifications**: Optimized for integration and performance

## Citation

If you use this package in your research, please cite:

```
@software{prop_profiler,
  author = {Enes Kelestemur},
  title = {Prop Profiler: A molecular property profiler for drug discovery},
  url = {https://github.com/eneskelestemur/prop_profiler},
  year = {2025}
}
```

If you use the pKa prediction functionality (Included in CNS-MPO calculation), please also cite the original MolGpKa work:

```
@article{pan2021molgpka,
  title={MolGpka: A Web Server for Small Molecule pKa Prediction Using a Graph-Convolutional Neural Network},
  author={Pan, Xiaolin and Wang, Hao and Li, Cuiyu and Zhang, John Z. H. and Ji, Changge},
  journal={Journal of Chemical Information and Modeling},
  volume={61},
  number={7},
  pages={3159--3165},
  year={2021},
  publisher={American Chemical Society},
  doi={10.1021/acs.jcim.1c00075}
}
```

If you use the CNS-MPO scoring functionality, please cite MolGpKa (above) along with the CNS-MPO paper:

```
@article{wager2016cns,
  title={Central Nervous System Multiparameter Optimization Desirability: Application in Drug Discovery},
  author={Wager, Travis T and Hou, Xinjun and Verhoest, Patrick R and Villalobos, Anabella},
  journal={ACS Chemical Neuroscience},
  volume={7},
  number={6},
  pages={767--775},
  year={2016},
  publisher={American Chemical Society},
  doi={10.1021/acschemneuro.6b00029}
}
```

If you use the Stoplight scoring functionality, please cite the original Stoplight paper:

```
@article{wellnitz2024stoplight,
  title={STOPLIGHT: A Hit Scoring Calculator},
  author={Wellnitz, James and Martin, Holli-Joi and Hossain, Mohammad Anwar and others},
  journal={Journal of Chemical Information and Modeling},
  volume={64},
  number={11},
  pages={4387--4391},
  year={2024},
  publisher={American Chemical Society},
  doi={10.1021/acs.jcim.4c00412}
}
```

## Data Sources

The package uses the following datasets for training and evaluation:
- **ESOL Dataset**: Aqueous solubility dataset for training ESOL models ([website](https://tdcommons.ai/single_pred_tasks/adme/#solubility-aqsoldb))
- **LogD Dataset**: Distribution coefficient dataset for logD prediction ([website](https://github.com/WangYitian123/RTlogD))

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For questions and issues, please open an issue on the [GitHub repository](https://github.com/eneskelestemur/prop_profiler/issues).