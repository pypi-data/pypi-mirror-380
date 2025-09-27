import logging

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from prop_profiler.training.base_trainer import Trainer
from prop_profiler.data.loader import load_esol_dataset

logger = logging.getLogger(__name__)


class EsolTrainer(Trainer):
    """
        Trainer for ESOL (water solubility) model.
    """
    def __init__(
        self,
        data_path: str = 'data/raw/solubility_aqsoldb.tab',
        model_path: str = 'models/esol_model.pkl.gz',
        cv: int = 5,
        test_size: float = 0.1,
        random_state: int = 42,
        **kwargs
    ):
        super().__init__(data_path, model_path,
                         cv=cv, test_size=test_size,
                         random_state=random_state, **kwargs)
        logger.info("Initialized EsolTrainer")

    def load_data(self):
        logger.info(f"Loading ESOL dataset from {self.data_path}")
        X, y = load_esol_dataset(self.data_path)
        self.X, self.y = X, y

    def build_model(self):
        logger.info("Building ESOL training pipeline")
        self.model = Pipeline([
            ('scaler', MinMaxScaler()),
            ('regressor', RandomForestRegressor(
                n_estimators=150, random_state=self.random_state, max_depth=30, n_jobs=-1))
        ])

