import pytest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
from prop_profiler.profiler import profile_molecules


@pytest.fixture
def sample_smiles_list():
    """Sample SMILES strings for testing."""
    return [
        'c1ccccc1',
        'CC(=O)O', 
        'c1ccncc1',
        'CCN(CC)CC'
    ]


@pytest.fixture
def expected_columns():
    """Expected columns in the profiler output."""
    return [
        'smiles', 'mw', 'logp', 'hba', 'hbd', 'tpsa', 'num_rotatable_bonds',
        'fsp3', 'qed', 'esol_mg/L', 'most_basic_pka', 'logd', 'cns_mpo_score',
        'stoplight_score', 'stoplight_color'
    ]


@pytest.fixture
def expected_values():
    """Expected values from your actual data."""
    return {
        'c1ccccc1': {
            'mw': 78.114,
            'logp': 1.6866,
            'hba': 0,
            'hbd': 0,
            'tpsa': 0.00,
            'num_rotatable_bonds': 0,
            'fsp3': 0.0,
            'qed': 0.442628,
            'esol_mg/L': 1998.360544,
            'most_basic_pka': np.nan,
            'logd': 1.495730,
            'cns_mpo_score': 4.000000,
            'stoplight_score': 0.333333,
            'stoplight_color': 'yellow'
        },
        'CC(=O)O': {
            'mw': 60.052,
            'logp': 0.0909,
            'hba': 1,
            'hbd': 1,
            'tpsa': 37.30,
            'num_rotatable_bonds': 0,
            'fsp3': 0.5,
            'qed': 0.429883,
            'esol_mg/L': 75044.685139,
            'most_basic_pka': 4.468792,
            'logd': -0.584336,
            'cns_mpo_score': 5.698333,
            'stoplight_score': 0.000000,
            'stoplight_color': 'green'
        },
        'c1ccncc1': {
            'mw': 79.102,
            'logp': 1.0816,
            'hba': 1,
            'hbd': 0,
            'tpsa': 12.89,
            'num_rotatable_bonds': 0,
            'fsp3': 0.0,
            'qed': 0.453148,
            'esol_mg/L': 143622.462057,
            'most_basic_pka': 5.127060,
            'logd': 0.551284,
            'cns_mpo_score': 5.000000,
            'stoplight_score': 0.333333,
            'stoplight_color': 'yellow'
        },
        'CCN(CC)CC': {
            'mw': 101.193,
            'logp': 1.3481,
            'hba': 1,
            'hbd': 0,
            'tpsa': 3.24,
            'num_rotatable_bonds': 3,
            'fsp3': 1.0,
            'qed': 0.518375,
            'esol_mg/L': 121387.605374,
            'most_basic_pka': 1.696782,
            'logd': 0.779436,
            'cns_mpo_score': 5.000000,
            'stoplight_score': 0.000000,
            'stoplight_color': 'green'
        }
    }


class TestProfileMolecules:
    """Test the main profile_molecules function."""
    
    def test_profile_molecules_basic(self, sample_smiles_list, expected_columns):
        """Test basic profiling functionality."""
        with patch('prop_profiler.predictors.esol.EsolPredictor') as mock_esol, \
             patch('prop_profiler.predictors.pka.PkaPredictor') as mock_pka, \
             patch('prop_profiler.predictors.logd.LogDPredictor') as mock_logd, \
             patch('prop_profiler.predictors.cns_mpo.CnsMpoPredictor') as mock_cns, \
             patch('prop_profiler.predictors.stoplight.StoplightPredictor') as mock_stoplight:
            
            # Mock predictor instances
            mock_esol_instance = MagicMock()
            mock_pka_instance = MagicMock()
            mock_logd_instance = MagicMock()
            mock_cns_instance = MagicMock()
            mock_stoplight_instance = MagicMock()
            
            mock_esol.return_value = mock_esol_instance
            mock_pka.return_value = mock_pka_instance
            mock_logd.return_value = mock_logd_instance
            mock_cns.return_value = mock_cns_instance
            mock_stoplight.return_value = mock_stoplight_instance
            
            # Mock curate methods
            mock_esol_instance.curate.return_value = sample_smiles_list
            mock_pka_instance.curate.return_value = sample_smiles_list
            mock_logd_instance.curate.return_value = sample_smiles_list
            mock_cns_instance.curate.return_value = sample_smiles_list
            mock_stoplight_instance.curate.return_value = sample_smiles_list
            
            # Mock predict methods with actual values
            mock_esol_instance.predict.return_value = [-3.301, -4.876, -5.158, -5.084]
            mock_pka_instance.predict.return_value = [np.nan, 4.468792, 5.127060, 1.696782]
            mock_logd_instance.predict.return_value = [1.495730, -0.584336, 0.551284, 0.779436]
            mock_cns_instance.predict.return_value = [4.000000, 5.698333, 5.000000, 5.000000]
            mock_stoplight_instance.predict.return_value = [0.333333, 0.000000, 0.333333, 0.000000]
            
            # Mock postprocess methods
            mock_esol_instance.postprocess.return_value = [1998.360544, 75044.685139, 143622.462057, 121387.605374]
            mock_stoplight_instance.postprocess.return_value = ['yellow', 'green', 'yellow', 'green']
            
            result = profile_molecules(sample_smiles_list)
            
            # Verify the result structure
            assert isinstance(result, pd.DataFrame)
            assert len(result) == 4
            assert list(result.columns) == expected_columns
            
            # Verify SMILES are correct
            assert result['smiles'].tolist() == sample_smiles_list
            
            # Verify some expected values
            assert result['stoplight_color'].tolist() == ['yellow', 'green', 'yellow', 'green']
            # Use approximate comparison for floating point values
            assert np.allclose(result['esol_mg/L'].tolist(), [1998.360544, 75044.685139, 143622.462057, 121387.605374], rtol=1e-6)
    
    def test_profile_molecules_with_single_smiles(self, expected_columns):
        """Test profiling with a single SMILES string."""
        with patch('prop_profiler.predictors.esol.EsolPredictor') as mock_esol, \
             patch('prop_profiler.predictors.pka.PkaPredictor') as mock_pka, \
             patch('prop_profiler.predictors.logd.LogDPredictor') as mock_logd, \
             patch('prop_profiler.predictors.cns_mpo.CnsMpoPredictor') as mock_cns, \
             patch('prop_profiler.predictors.stoplight.StoplightPredictor') as mock_stoplight:
            
            # Mock all predictors
            for mock_pred in [mock_esol, mock_pka, mock_logd, mock_cns, mock_stoplight]:
                mock_instance = MagicMock()
                mock_pred.return_value = mock_instance
                mock_instance.curate.return_value = ['c1ccccc1']
                mock_instance.predict.return_value = [1.0]
                mock_instance.postprocess.return_value = [1.0]
            
            # Mock stoplight postprocess to return color
            mock_stoplight.return_value.postprocess.return_value = ['yellow']
            
            # Pass as list to avoid scalar DataFrame issues
            result = profile_molecules(['c1ccccc1'])
            
            assert isinstance(result, pd.DataFrame)
            assert len(result) == 1
            assert list(result.columns) == expected_columns
            assert result['smiles'].iloc[0] == 'c1ccccc1'
    
    def test_profile_molecules_empty_input(self):
        """Test profiling with empty input."""
        with patch('prop_profiler.predictors.stoplight.StoplightPredictor') as mock_stoplight:
            mock_instance = MagicMock()
            mock_stoplight.return_value = mock_instance
            mock_instance.curate.return_value = []  # Empty list after curation
            
            result = profile_molecules([])
            
            assert isinstance(result, pd.DataFrame)
            assert len(result) == 0
    
    def test_profile_molecules_invalid_smiles(self):
        """Test profiling with invalid SMILES."""
        with patch('prop_profiler.utils.chem_helpers.curate_df') as mock_curate_df:
            # Mock curate_df to return empty DataFrame for invalid SMILES
            empty_df = pd.DataFrame(columns=['smiles', 'mols'])
            mock_curate_df.return_value = empty_df
            
            result = profile_molecules(['INVALID_SMILES'])
            
            assert isinstance(result, pd.DataFrame)
            assert len(result) == 0
    
    def test_profile_molecules_with_device(self, sample_smiles_list):
        """Test profiling with device parameter."""
        with patch('prop_profiler.predictors.esol.EsolPredictor') as mock_esol, \
             patch('prop_profiler.predictors.pka.PkaPredictor') as mock_pka, \
             patch('prop_profiler.predictors.logd.LogDPredictor') as mock_logd, \
             patch('prop_profiler.predictors.cns_mpo.CnsMpoPredictor') as mock_cns, \
             patch('prop_profiler.predictors.stoplight.StoplightPredictor') as mock_stoplight:
            
            # Mock all predictors
            for mock_pred in [mock_esol, mock_pka, mock_logd, mock_cns, mock_stoplight]:
                mock_instance = MagicMock()
                mock_pred.return_value = mock_instance
                mock_instance.curate.return_value = sample_smiles_list
                mock_instance.predict.return_value = [1.0] * len(sample_smiles_list)
                mock_instance.postprocess.return_value = [1.0] * len(sample_smiles_list)
            
            # Mock stoplight postprocess to return colors
            mock_stoplight.return_value.postprocess.return_value = ['green'] * len(sample_smiles_list)
            
            result = profile_molecules(sample_smiles_list, device='cuda')
            
            # Verify pKa predictor was called with correct device
            mock_pka.assert_called_once()
            call_args = mock_pka.call_args
            assert 'device' in call_args[1]
            assert call_args[1]['device'] == 'cuda'
    
    def test_profile_molecules_data_types(self, sample_smiles_list):
        """Test that the returned DataFrame has correct data types."""
        with patch('prop_profiler.predictors.esol.EsolPredictor') as mock_esol, \
             patch('prop_profiler.predictors.pka.PkaPredictor') as mock_pka, \
             patch('prop_profiler.predictors.logd.LogDPredictor') as mock_logd, \
             patch('prop_profiler.predictors.cns_mpo.CnsMpoPredictor') as mock_cns, \
             patch('prop_profiler.predictors.stoplight.StoplightPredictor') as mock_stoplight:
            
            # Mock all predictors with appropriate return types
            for mock_pred in [mock_esol, mock_pka, mock_logd, mock_cns, mock_stoplight]:
                mock_instance = MagicMock()
                mock_pred.return_value = mock_instance
                mock_instance.curate.return_value = sample_smiles_list
                mock_instance.predict.return_value = [1.0] * len(sample_smiles_list)
                mock_instance.postprocess.return_value = [1.0] * len(sample_smiles_list)
            
            # Mock stoplight postprocess to return strings
            mock_stoplight.return_value.postprocess.return_value = ['green'] * len(sample_smiles_list)
            
            result = profile_molecules(sample_smiles_list)
            
            # Check that string columns are strings
            assert result['smiles'].dtype == 'object'
            assert result['stoplight_color'].dtype == 'object'
            
            # Check that numeric columns are numeric
            assert np.issubdtype(result['mw'].dtype, np.number)
            assert np.issubdtype(result['logp'].dtype, np.number)
            assert np.issubdtype(result['qed'].dtype, np.number)
    
    def test_profile_molecules_column_names(self, sample_smiles_list, expected_columns):
        """Test that all expected columns are present."""
        with patch('prop_profiler.predictors.esol.EsolPredictor') as mock_esol, \
             patch('prop_profiler.predictors.pka.PkaPredictor') as mock_pka, \
             patch('prop_profiler.predictors.logd.LogDPredictor') as mock_logd, \
             patch('prop_profiler.predictors.cns_mpo.CnsMpoPredictor') as mock_cns, \
             patch('prop_profiler.predictors.stoplight.StoplightPredictor') as mock_stoplight:
            
            # Mock all predictors
            for mock_pred in [mock_esol, mock_pka, mock_logd, mock_cns, mock_stoplight]:
                mock_instance = MagicMock()
                mock_pred.return_value = mock_instance
                mock_instance.curate.return_value = sample_smiles_list
                mock_instance.predict.return_value = [1.0] * len(sample_smiles_list)
                mock_instance.postprocess.return_value = [1.0] * len(sample_smiles_list)
            
            # Mock stoplight postprocess to return strings
            mock_stoplight.return_value.postprocess.return_value = ['green'] * len(sample_smiles_list)
            
            result = profile_molecules(sample_smiles_list)
            
            # Check all expected columns are present
            for col in expected_columns:
                assert col in result.columns, f"Column '{col}' missing from result"
            
            # Check no extra columns
            assert len(result.columns) == len(expected_columns)
