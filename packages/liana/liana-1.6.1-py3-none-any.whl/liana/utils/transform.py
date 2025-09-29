import numpy as np
from scipy.sparse import csr_matrix, isspmatrix_csr


def zi_minmax(X, cutoff=0.5):
    """
    Zero-inflated min-max scaling, adopted from CiteFuse (Kim et al., 2020; https://academic.oup.com/bioinformatics/article/36/14/4137/5827474).

    This function scales the data to the range [0, 1] and sets values below a specified cutoff to 0.

    Parameters
    ----------
    X : array-like
        Data to be scaled.
    cutoff : float
        Cutoff value for zero-inflation -
        values less than this are set to 0. Default is 0.5.

    Returns
    -------
    X : csr_matrix

    """
    X = X.copy()
    if not isspmatrix_csr(X):
        X = csr_matrix(X)

    min_vals = np.array(X.min(axis=0).todense())[0]
    max_vals = np.array(X.max(axis=0).todense())[0]
    nonzero_rows, nonzero_cols = X.nonzero()
    scaled_values = (X.data - min_vals[nonzero_cols]) \
        / (max_vals[nonzero_cols] - min_vals[nonzero_cols])

    scaled_values[scaled_values < cutoff] = 0
    nonzero_rows, nonzero_cols = X.nonzero()

    X = csr_matrix(
        (scaled_values, (nonzero_rows, nonzero_cols)),
        shape=X.shape
    )

    return X


def neg_to_zero(X, cutoff=0):
    """
    Set negative values to 0.

    Parameters
    ----------
    X : array-like
        Data to be transformed.
    cutoff : float
        Cutoff value for zero-inflation - values less than
        this are set to 0. Default is 0.

    Returns
    -------
    A csr_matrix.

    """
    X = X.copy()
    if not isspmatrix_csr(X):
        X = csr_matrix(X)
    X.data[X.data < cutoff] = 0
    return X
