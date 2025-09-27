import joblib
import logging

import numpy as np
from prop_profiler.predictors.base import Predictor
from prop_profiler.utils import chem_helpers as chem

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LogDPredictor(Predictor):
    """
        Predicts lipophilicity (log D).
    """
    def __init__(self, model_path: str):
        super().__init__(model_path)
        self._load_model()

    def _load_model(self):
        self.model = joblib.load(self.model_paths['default'])

    def preprocess(self, mols: list[chem.Mol]):
        """
            Compute feature vector for a list of molecules.

            Args:
                mols: List of RDKit Mol objects.

            Returns:
                List of descriptor vectors
        """
        # Feature computation must be done in the same way as training
        X = np.array([chem.compute_features(mol, True, ['logp']) for mol in mols])
        return X
            
