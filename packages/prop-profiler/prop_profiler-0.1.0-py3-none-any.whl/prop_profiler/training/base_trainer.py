import logging
from abc import ABC, abstractmethod
import joblib

from sklearn.model_selection import train_test_split, cross_validate
from sklearn import metrics as m
from sklearn.base import is_classifier, is_regressor

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Trainer(ABC):
    """
        Base class for training workflows with cross-validation and metric detection.
    """
    def __init__(
        self,
        data_path: str,
        model_path: str,
        cv: int = 5,
        test_size: float = 0.2,
        random_state: int = 42,
        **kwargs
    ):
        logger.info(
            f"Initializing Trainer: data_path={data_path}, model_path={model_path}, "
            f"cv={cv}, test_size={test_size}, random_state={random_state}"
        )
        self.data_path = data_path
        self.model_path = model_path
        self.cv = cv
        self.test_size = test_size
        self.random_state = random_state
        self.model = None
        self.X = None
        self.y = None
        self.kwargs = kwargs

    @abstractmethod
    def load_data(self):
        """Load raw features X and labels y into self.X, self.y."""
        ...

    @abstractmethod
    def build_model(self):
        """Initialize the model and assign to self.model."""
        ...

    def fit(
        self,
        X=None,
        y=None,
        cv=None,
        test_size=None,
        random_state=None
    ):
        """
            Train the model. Allows overriding data, CV, split size, and random state.
            Returns a dict of scores.
        """
        logger.info("Starting fit process")
        if X is not None and y is not None:
            self.X, self.y = X, y
        else:
            if self.X is None or self.y is None:
                self.load_data()
        if cv is not None:
            self.cv = cv
        if test_size is not None:
            self.test_size = test_size
        if random_state is not None:
            self.random_state = random_state

        if self.model is None:
            self.build_model()

        if self.cv and self.cv > 1:
            logger.info(f"Performing {self.cv}-fold cross-validation")
            cv_results = self._cross_validate()
            self.model.fit(self.X, self.y)
            return cv_results
        else:
            logger.info("Performing train/validation split evaluation")
            return self._train_and_evaluate()

    def _cross_validate(self):
        """
            Perform cross-validation and return scoring dictionary.
        """
        scoring = self._get_scoring()
        results = cross_validate(
            self.model,
            self.X,
            self.y,
            cv=self.cv,
            scoring=scoring,
            return_train_score=False
        )
        return {metric: results[f'test_{metric}'] for metric in scoring}

    def _train_and_evaluate(self):
        """
            Train on a single split and evaluate metrics.
        """
        X_train, X_val, y_train, y_val = train_test_split(
            self.X,
            self.y,
            test_size=self.test_size,
            random_state=self.random_state
        )
        self.model.fit(X_train, y_train)
        return self._evaluate_model(X_val, y_val)

    def _get_scoring(self):
        """
            Determine appropriate scoring metrics based on model type.
        """
        if is_classifier(self.model):
            return ['accuracy', 'precision', 'recall', 'f1']
        elif is_regressor(self.model):
            return ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error', 
                    'neg_root_mean_squared_error']
        else:
            raise ValueError("Unsupported model type for scoring")

    def _evaluate_model(self, X_val, y_val):
        """
            Evaluate on a validation split and return metrics.
        """
        preds = self.model.predict(X_val)
        if is_classifier(self.model):
            return {
                'accuracy': m.accuracy_score(y_val, preds),
                'precision': m.precision_score(y_val, preds, average='weighted'),
                'recall': m.recall_score(y_val, preds, average='weighted'),
                'f1': m.f1_score(y_val, preds, average='weighted')
            }
        elif is_regressor(self.model):
            return {
                'mse': m.mean_squared_error(y_val, preds),
                'rmse': m.root_mean_squared_error(y_val, preds),
                'mae': m.mean_absolute_error(y_val, preds),
                'r2': m.r2_score(y_val, preds)
            }
        else:
            raise ValueError("Unsupported model type for evaluation")

    def save_model(self, model_path=None):
        """Serialize the trained model to disk using joblib with compression."""
        path = model_path if model_path is not None else self.model_path
        logger.info(f"Saving model to {path}")
        joblib.dump(self.model, path, compress=('gzip', 3))

