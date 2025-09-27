import logging
from prop_profiler.training.base_trainer import Trainer
from prop_profiler.data.loader import load_logd_dataset
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

logger = logging.getLogger(__name__)

class LogDTrainer(Trainer):
    """
        Trainer for lipophilicity (log D) model.
    """
    def __init__(
        self,
        data_path: str = 'data/raw/DB29_logD_data.csv',
        model_path: str = 'models/logD_model.pkl.gz',
        cv: int = 5,
        test_size: float = 0.1,
        random_state: int = 42,
        **kwargs
    ):
        super().__init__(data_path, model_path,
                         cv=cv, test_size=test_size,
                         random_state=random_state, **kwargs)
        logger.info("Initialized LogDTrainer")

    def load_data(self, data_path: str = None):
        if data_path is not None:
            self.data_path = data_path

        logger.info(f"Loading LogD dataset from {self.data_path}")
        X, y = load_logd_dataset(self.data_path)
        self.X, self.y = X, y

    def build_model(self):
        logger.info("Building LogD training pipeline")
        self.model = Pipeline([
            ('scaler', MinMaxScaler()),
            ('regressor', RandomForestRegressor(
                n_estimators=150, random_state=self.random_state, max_depth=35, n_jobs=-1))
        ])