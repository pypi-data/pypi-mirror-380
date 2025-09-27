from abc import ABC, abstractmethod
from typing import List, Any


class BaseWrapper(ABC):
    """
        Abstract base for all model-like wrappers.
    """
    @abstractmethod
    def predict(self, input_data: List[str]) -> List[Any]:
        """
            Compute predictions for a list of SMILES strings.
        """
        pass

    