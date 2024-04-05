import pandas as pd

from useful_rdkit_utils import RDKitDescriptors
from rdkit import Chem


desc_calc = RDKitDescriptors()


def smiles_to_features(smiles):
    """
    Featurize SMILES with a Pandas DataFrame with 210 columns (features) and 1 row.
    """
    
    rdkit_molecule = Chem.MolFromSmiles(smiles)
    smiles_featured = desc_calc.calc_mol(rdkit_molecule)
    smiles_featured = smiles_featured.reshape(1, 210)
    df_res = pd.DataFrame(data=smiles_featured, columns=desc_calc.desc_names)
    return df_res

