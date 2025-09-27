import pandas as pd
from pathlib import Path
import sys

from prop_profiler.utils import chem_helpers as chem
from prop_profiler.predictors.cns_mpo import CnsMpoPredictor
from prop_profiler.predictors.stoplight import StoplightPredictor
from prop_profiler.predictors.esol import EsolPredictor


def _get_model_path(filename: str) -> Path:
    if sys.version_info >= (3, 9):
        try:
            from importlib import resources
            models_path = resources.files('prop_profiler').parent / 'models'
            return models_path / filename
        except (ImportError, AttributeError):
            pass
    
    root_dir = Path(__file__).resolve().parent.parent
    model_path = root_dir / 'models' / filename
    
    if model_path.exists():
        return model_path
    else:
        raise FileNotFoundError(f"Model file not found: {filename}")

ESOL_MODEL = _get_model_path('esol_model.pkl.gz')
LOGD_MODEL = _get_model_path('logd_model.pkl.gz')
ACID_MODEL = _get_model_path('weight_acid.pth')
BASE_MODEL = _get_model_path('weight_base.pth')


def profile_molecules(
    molecules: list,
    skip_cns_mpo: bool = False,
    device: str = 'cpu',
    verbose: bool = False
) -> pd.DataFrame:
    """
        Compute descriptor-based properties and optional CNS-MPO scores.

        Args:
            molecules: List of RDKit Mol objects or SMILES strings.
            skip_cns_mpo: If True, omit CNS-MPO scoring along with logD and pKa.
            device: Device to run the pka model on, 'cpu' or 'cuda'.
            verbose: If True, display progress bars.

        Returns:
            DataFrame with properties and scores.
    """
    stoplight = StoplightPredictor(
        esol_predictor=EsolPredictor(ESOL_MODEL)
    )
    mols = stoplight.curate(molecules)
    mol_props = [{'smiles': chem.get_smiles(m)} for m in mols]
    stoplight_scores = stoplight.predict(mols, verbose=verbose)
    stoplight_colors = stoplight.postprocess(stoplight_scores)

    if not skip_cns_mpo:
        try:
            from prop_profiler.predictors.logd import LogDPredictor
            from prop_profiler.predictors.pka import PkaPredictor
            
            cns_mpo = CnsMpoPredictor(
                pka_predictor=PkaPredictor(acid_model_path=ACID_MODEL, base_model_path=BASE_MODEL, device=device),
                logd_predictor=LogDPredictor(LOGD_MODEL),
            )
            cns_mpo_scores = cns_mpo.predict(mols, verbose=verbose)
            for i, props in enumerate(mol_props):
                props.update(chem.get_props(mols[i]))
                props.update(stoplight.mol_props[i])
                props.update(cns_mpo.mol_props[i])
                props.update({'cns_mpo_score': cns_mpo_scores[i]})
        except ImportError:
            if verbose:
                print("Warning: PyTorch not available. Skipping CNS-MPO prediction. Install with: pip install prop-profiler[pka]")
            skip_cns_mpo = True
    
    if skip_cns_mpo:
        for i, props in enumerate(mol_props):
            props.update(chem.get_props(mols[i]))
            props.update(stoplight.mol_props[i])

    # Convert to DataFrame
    df = pd.DataFrame(mol_props)
    df['stoplight_score'] = stoplight_scores
    df['stoplight_color'] = stoplight_colors

    return df

