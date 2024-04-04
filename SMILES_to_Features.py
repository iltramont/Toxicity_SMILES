import pandas as pd
import numpy as np
import os

from useful_rdkit_utils import RDKitDescriptors
from rdkit import Chem

desc_calc = RDKitDescriptors()

def smile_to_feature(smiles):
    
    """Featurizza uno SMILES e restituisce un dataframe composto da 208 colonne (features) e 1 riga."""
    
    rdkit_obj = Chem.MolFromSmiles(smiles)
    smiles_featurized = desc_calc.calc_mol(rdkit_obj)
    smiles_featurized = smiles_featurized.reshape(1,208)
    df_res = pd.DataFrame(data =smiles_featurized, columns = desc_calc.desc_names)
    
    return df_res

