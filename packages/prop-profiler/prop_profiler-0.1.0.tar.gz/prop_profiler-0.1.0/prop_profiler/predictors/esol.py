import joblib
import logging

import numpy as np
from prop_profiler.predictors.base import Predictor
from prop_profiler.utils import chem_helpers as chem

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class EsolPredictor(Predictor):
    """
        Predicts ESOL water solubility (log S).
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
        # cache the molecular weights for later use
        self.mol_weights = np.array([chem.get_props(x, ['mw'])['mw'] for x in mols])
        return X

    def postprocess(self, predictions: np.ndarray):
        """
            Convert log of molarity predictions to solubility in mg/L.
        """
        return 10**predictions * self.mol_weights * 1000
            
