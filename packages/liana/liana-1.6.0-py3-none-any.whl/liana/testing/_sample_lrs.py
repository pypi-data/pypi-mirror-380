import string

import numpy as np
import pandas as pd


# Function to generate a liana_res sample/example
def sample_lrs(by_sample=False):
    """Create sample method output for testing metrics in this task."""
    row_num = 200
    rng = np.random.default_rng(seed=1)

    label_vector = list(string.ascii_uppercase[0:10])
    entity_vector = list(string.ascii_lowercase[0:10])

    df = pd.DataFrame(rng.random((row_num, 1)), columns=["magnitude"])
    df["source"] = rng.choice(label_vector, row_num)
    df["target"] = rng.choice(label_vector, row_num)
    df["ligand_complex"] = rng.choice(entity_vector, row_num)
    df["receptor_complex"] = rng.choice(entity_vector, row_num)
    df["specificity_rank"] = rng.random((row_num, 1))

    # deduplicate
    df = df.loc[~df.duplicated()]

    if by_sample:
        df['sample'] = rng.choice(['A', 'B', 'C', 'D'], row_num)
        df['sample'] = df['sample'].astype('category')

    # add some metrics by entity
    row_num = df.shape[0]
    df['ligand_means'] = rng.random((row_num, 1))
    df['receptor_means'] = rng.random((row_num, 1))
    df['ligand_pvals'] = rng.random((row_num, 1))
    df['receptor_pvals'] = rng.random((row_num, 1))

    return df
