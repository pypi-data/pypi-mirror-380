import logging

from prop_profiler.predictors.base import Predictor
from prop_profiler.models.molgpka_wrapper import MolGpKaWrapper
from prop_profiler.utils import chem_helpers as chem

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class PkaPredictor(Predictor):
    """
        Predicts the most basic pKa using MolGpKaWrapper.
    """
    def __init__(
        self,
        acid_model_path: str,
        base_model_path: str,
        device: str='cpu',
        verbose: bool=False
    ):
        """
            Initialize the pKa predictor.

            Args:
                acid_model_path: Path to the acid model.
                base_model_path: Path to the base model.
                device: Device to run the model on ('cpu' or 'cuda').
                verbose: Whether to print verbose output.
        """
        super().__init__(acid=acid_model_path, base=base_model_path)
        self.device = device
        self.verbose = verbose
        self._load_model()

    def _load_model(self):
        molgpka = MolGpKaWrapper(
            acid_model_path=self.model_paths['acid'],
            base_model_path=self.model_paths['base'],
            device=self.device,
            verbose=self.verbose
        )
        self.model = molgpka

    def preprocess(self, mols: list[chem.Mol]):
        """
            Preprocess the input molecules.

            Args:
                mols: List of RDKit Mol objects.

            Returns:
                List of RDKit Mol objects.
        """
        return mols
    
