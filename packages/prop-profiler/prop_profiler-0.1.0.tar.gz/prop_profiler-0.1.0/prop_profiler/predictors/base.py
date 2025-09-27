from abc import ABC, abstractmethod
from typing import Dict
import logging

import pandas as pd
import numpy as np
from tqdm import tqdm

from prop_profiler.utils import chem_helpers as chem

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Predictor(ABC):
    """
        Base class for molecular property predictors.
        Supports a primary model via `model_path` and optional named models via kwargs.
    """
    def __init__(
        self,
        model_path: str=None,
        **model_paths: str
    ):
        # Primary model under 'default'; additional models under their kwargs names
        self.model_paths: Dict[str, str] = {'default': model_path}
        self.model_paths.update(model_paths)
        self.model = None

    @abstractmethod
    def _load_model(self):
        """
            Load model(s) into `self.model`. Multi-model predictors 
            should be wrapped to have a single predict logic.
        """
        pass

    @abstractmethod
    def preprocess(self, mols: list[chem.Mol]):
        """Compute feature vector for a list of molecules."""
        pass

    def postprocess(self, predictions: list):
        """Post-process the predictions if needed."""
        return predictions

    def predict(self, mols: list[chem.Mol], batch_size: int=256, verbose: bool=False):
        """
            Predict property values for a list of molecules.

            NOTE: Run Predictor.curate() before this method to ensure valid input.
                Otherwise, it will fail on invalid SMILES or RDKit Mol objects.

            Args:
                mols: List of RDKit Mol objects.

            Returns:
                List of predictions.
        """
        if self.model is None:
            self._load_model()
        feats = self.preprocess(mols)
        preds = np.zeros(len(feats))
        for i in tqdm(range(0, len(feats), batch_size), desc='Predicting', total=len(feats)//batch_size, disable=not verbose):
            batch = feats[i:i+batch_size]
            pred = self.model.predict(batch)
            preds[i:i+batch_size] = pred
        return preds
    
    def curate(self, mols: list):
        """
            Curate the input molecules.

            Args:
                mols: List of SMILES or RDKit Mol objects.

            Returns:
                List of RDKit Mol objects.
        """
        if len(mols) == 0:
            return []
        
        if chem.is_mol_instance(mols[0]):
            mols = [chem.get_smiles(mol) for mol in mols]
        initial_count = len(mols)
        mols = chem.curate_df(pd.DataFrame({'smiles': mols}))['mols'].tolist()
        logger.info(f"Curated molecule count: {len(mols)} dropped {initial_count - len(mols)}")
        return mols
    
