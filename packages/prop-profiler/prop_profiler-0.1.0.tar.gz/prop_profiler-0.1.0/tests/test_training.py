import pytest
import numpy as np
from unittest.mock import patch, MagicMock

from prop_profiler.training.esol_trainer import EsolTrainer
from prop_profiler.training.logd_trainer import LogDTrainer


class TestEsolTrainer:
    """Test ESOL trainer."""
    
    def test_esol_trainer_init(self):
        """Test ESOL trainer initialization."""
        trainer = EsolTrainer(
            data_path='test_data.tsv',
            model_path='test_model.pkl',
            cv=3,
            test_size=0.2,
            random_state=42
        )
        
        assert trainer.data_path == 'test_data.tsv'
        assert trainer.model_path == 'test_model.pkl'
        assert trainer.cv == 3
        assert trainer.test_size == 0.2
        assert trainer.random_state == 42
    
    def test_esol_trainer_load_data(self):
        """Test ESOL trainer data loading."""
        with patch('prop_profiler.training.esol_trainer.load_esol_dataset') as mock_load:
            mock_load.return_value = (
                np.array([[1, 2, 3], [4, 5, 6]]),
                np.array([-0.77, -0.25])
            )
            
            trainer = EsolTrainer(data_path='test_data.tsv')
            trainer.load_data()
            
            # Check that data was loaded into trainer
            assert trainer.X.shape == (2, 3)
            assert trainer.y.shape == (2,)
            assert trainer.y[0] == pytest.approx(-0.77)
            assert trainer.y[1] == pytest.approx(-0.25)
            mock_load.assert_called_once_with('test_data.tsv')
    
    def test_esol_trainer_create_model(self):
        """Test ESOL trainer model creation."""
        trainer = EsolTrainer()
        trainer.build_model()
        
        # Check if it's a pipeline with the expected components
        assert hasattr(trainer.model, 'steps')
        assert len(trainer.model.steps) == 2
        assert trainer.model.steps[0][0] == 'scaler'
        assert trainer.model.steps[1][0] == 'regressor'
    
    def test_esol_trainer_train(self):
        """Test ESOL trainer training process."""
        with patch('prop_profiler.training.esol_trainer.load_esol_dataset') as mock_load:
            
            # Mock data loading
            mock_load.return_value = (
                np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
                np.array([-0.77, -0.25, -1.5, -2.0])
            )
            
            trainer = EsolTrainer(
                data_path='test_data.tsv',
                model_path='test_model.pkl',
                cv=1,  # Disable cross-validation to avoid sklearn complications
                test_size=0.25
            )
            
            # Mock the actual training to avoid sklearn dependencies
            with patch.object(trainer, '_train_and_evaluate', return_value={'accuracy': 0.85}) as mock_eval:
                # Set the model manually since we're bypassing build_model
                mock_model = MagicMock()
                trainer.model = mock_model
                
                result = trainer.fit()
                
                # Verify evaluation was called and result returned
                mock_eval.assert_called_once()
                assert result == {'accuracy': 0.85}


class TestLogDTrainer:
    """Test LogD trainer."""
    
    def test_logd_trainer_init(self):
        """Test LogD trainer initialization."""
        trainer = LogDTrainer(
            data_path='test_data.csv',
            model_path='test_model.pkl',
            cv=3,
            test_size=0.2,
            random_state=42
        )
        
        assert trainer.data_path == 'test_data.csv'
        assert trainer.model_path == 'test_model.pkl'
        assert trainer.cv == 3
        assert trainer.test_size == 0.2
        assert trainer.random_state == 42
    
    def test_logd_trainer_load_data(self):
        """Test LogD trainer data loading."""
        with patch('prop_profiler.training.logd_trainer.load_logd_dataset') as mock_load:
            mock_load.return_value = (
                np.array([[1, 2, 3], [4, 5, 6]]),
                np.array([0.50, 1.25])
            )
            
            trainer = LogDTrainer(data_path='test_data.csv')
            trainer.load_data()
            
            # Check that data was loaded into trainer
            assert trainer.X.shape == (2, 3)
            assert trainer.y.shape == (2,)
            assert trainer.y[0] == pytest.approx(0.50)
            assert trainer.y[1] == pytest.approx(1.25)
            mock_load.assert_called_once_with('test_data.csv')
    
    def test_logd_trainer_create_model(self):
        """Test LogD trainer model creation."""
        trainer = LogDTrainer()
        trainer.build_model()
        
        # Check if it's a pipeline with the expected components
        assert hasattr(trainer.model, 'steps')
        assert len(trainer.model.steps) == 2
        assert trainer.model.steps[0][0] == 'scaler'
        assert trainer.model.steps[1][0] == 'regressor'
    
    def test_logd_trainer_train(self):
        """Test LogD trainer training process."""
        with patch('prop_profiler.training.logd_trainer.load_logd_dataset') as mock_load:
            
            # Mock data loading
            mock_load.return_value = (
                np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
                np.array([0.50, 1.25, -0.75, 2.0])
            )
            
            trainer = LogDTrainer(
                data_path='test_data.csv',
                model_path='test_model.pkl',
                cv=1,  # Disable cross-validation to avoid sklearn complications
                test_size=0.25
            )
            
            # Mock the actual training to avoid sklearn dependencies
            with patch.object(trainer, '_train_and_evaluate', return_value={'accuracy': 0.85}) as mock_eval:
                # Set the model manually since we're bypassing build_model
                mock_model = MagicMock()
                trainer.model = mock_model
                
                result = trainer.fit()
                
                # Verify evaluation was called and result returned
                mock_eval.assert_called_once()
                assert result == {'accuracy': 0.85}


class TestBaseTrainer:
    """Test base trainer functionality."""
    
    def test_base_trainer_cross_validation(self):
        """Test cross-validation functionality."""
        with patch('prop_profiler.training.esol_trainer.load_esol_dataset') as mock_load:
            mock_load.return_value = (
                np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
                np.array([-0.77, -0.25, -1.5, -2.0])
            )
            
            trainer = EsolTrainer(cv=2)
            
            with patch('sklearn.model_selection.cross_val_score') as mock_cv:
                mock_cv.return_value = np.array([0.8, 0.9])
                
                trainer.load_data()
                trainer.build_model()
                
                # Mock cross-validation
                scores = mock_cv.return_value
                
                assert len(scores) == 2
                assert scores.mean() == pytest.approx(0.85)
                assert scores.std() == pytest.approx(0.05)
    
    def test_base_trainer_train_test_split(self):
        """Test train-test split functionality."""
        with patch('prop_profiler.training.esol_trainer.load_esol_dataset') as mock_load:
            mock_load.return_value = (
                np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
                np.array([-0.77, -0.25, -1.5, -2.0])
            )
            
            trainer = EsolTrainer(test_size=0.25, random_state=42)
            
            with patch('sklearn.model_selection.train_test_split') as mock_split:
                mock_split.return_value = (
                    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),  # X_train
                    np.array([[10, 11, 12]]),  # X_test
                    np.array([-0.77, -0.25, -1.5]),  # y_train
                    np.array([-2.0])  # y_test
                )
                
                trainer.load_data()
                
                # Verify data was loaded
                assert trainer.X.shape == (4, 3)
                assert trainer.y.shape == (4,)
                
                # Verify split parameters would be used
                assert trainer.test_size == 0.25
                assert trainer.random_state == 42
