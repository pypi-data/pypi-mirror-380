import logging

import pandas as pd
import numpy as np
from prop_profiler.utils import chem_helpers as chem

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def load_esol_dataset(path: str):
    """
        Load ESOL dataset from a tab-separated file or DataFrame.

        Args:
            path: Path to the tab-separated file.
        
        Returns:
            X: List of descriptor vectors
            y: List of solubility values
    """
    data = pd.read_csv(path, sep='\t', usecols=['Drug', 'Y'])
    data = data.rename(columns={'Drug': 'smiles', 'Y': 'esol'})

    logger.info(f"Input count: {len(data)} molecules")
    data = chem.curate_df(data)
    logger.info(f"Curated count: {len(data)} molecules")

    X = np.array([chem.compute_features(mol, True, ['logp']) for mol in data['mols']])
    y = data['esol'].to_numpy()
    return X, y


def load_logd_dataset(path: str):
    """
        Load LogD dataset from a CSV file.

        Args:
            path: Path to the CSV file.

        Returns:
            X: List of descriptor vectors
            y: List of logD values
    """
    data = pd.read_csv(path)

    logger.info(f"Input count: {len(data)} molecules")
    data = chem.curate_df(data)
    logger.info(f"Curated count: {len(data)} molecules")

    X = np.array([chem.compute_features(mol, True, ['logp']) for mol in data['mols']])
    y = data['logD'].to_numpy()
    return X, y

