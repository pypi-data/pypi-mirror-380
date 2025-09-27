import pytest
import numpy as np
import pandas as pd
from prop_profiler.data.loader import load_esol_dataset, load_logd_dataset


def test_load_esol_dataset(tmp_path):
    # Create a temporary TSV with Drug and Y columns including valid, invalid, and boron SMILES
    content = (
        "Drug\tY\n"
        "CCO\t-0.77\n"
        "invalid\t0.45\n"
        "CB\t0.12\n"
    )
    tsv_file = tmp_path / "esol_test.tsv"
    tsv_file.write_text(content)

    X, y = load_esol_dataset(str(tsv_file))
    # Only the valid CCO should remain after curation
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert X.shape[0] == 1
    assert y.shape == (1,)
    assert y[0] == pytest.approx(-0.77)


def test_load_logd_dataset(tmp_path):
    # Create a temporary CSV with smiles and logD columns
    content = (
        "smiles,logD\n"
        "CCO,0.50\n"
        "not_smiles,1.25\n"
        "CB,2.00\n"
    )
    csv_file = tmp_path / "logd_test.csv"
    csv_file.write_text(content)

    X, y = load_logd_dataset(str(csv_file))
    # Only the valid CCO should remain after curation
    assert isinstance(X, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert X.shape[0] == 1
    assert y.shape == (1,)
    assert y[0] == pytest.approx(0.50)


def test_loader_preserves_feature_dimension(tmp_path):
    # Ensure that feature length matches compute_features output
    # Use a single valid SMILES entry
    content = "Drug\tY\nCCO\t-0.00\n"
    tsv_file = tmp_path / "esol_dim.tsv"
    tsv_file.write_text(content)

    X, _ = load_esol_dataset(str(tsv_file))
    # Each row in X should be a 1D array of floats
    assert X.ndim == 2
    assert X.shape[1] > 0
    assert all(isinstance(v, float) for v in X.flat)

    # Similarly for logD
    content_csv = "smiles,logD\nCCO,0.00\n"
    csv_file = tmp_path / "logd_dim.csv"
    csv_file.write_text(content_csv)

    X2, _ = load_logd_dataset(str(csv_file))
    assert X2.ndim == 2
    assert X2.shape[1] == X.shape[1]
    assert all(isinstance(v, float) for v in X2.flat)
