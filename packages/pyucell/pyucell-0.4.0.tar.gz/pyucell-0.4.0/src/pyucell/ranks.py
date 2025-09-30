from warnings import warn
from anndata import AnnData
from scipy import sparse
from scipy.stats import rankdata
import numpy as np

def get_rankings(
    data,
    layer: str = None,
    max_rank: int = 1500,
    ties_method: str = "average",
) -> sparse.csr_matrix:
    """
    Compute per-cell ranks of genes for an AnnData object.

    Parameters
    ----------
    data : AnnData | np.ndarray | sparse matrix
        Either an AnnData object (cells x genes) or directly a 2D matrix.
    layer : str, optional
        Only used if input is AnnData. Which layer to use (None = adata.X).
    max_rank : int, optional
        Cap ranks at this value (ranks > max_rank are dropped for sparsity).
    ties_method : str, optional
        Passed to scipy.stats.rankdata.

    Returns
    -------
    ranks : csr_matrix of shape (genes, cells)
        Sparse matrix of ranks.
    """

    # Accept either AnnData or matrix directly
    if isinstance(data, AnnData):
        X = data.layers[layer] if layer else data.X
    else:
        X = data

    n_cells, n_genes = X.shape

    # Convert to array
    is_sparse = sparse.issparse(X)
    Xarr = X.toarray() if is_sparse else np.asarray(X)

    # Allocate vectors, at most max_rank entries per cell
    n_cells, n_genes = X.shape
    nnz_per_cell = max_rank 
    nnz_total = n_cells * nnz_per_cell

    data = np.empty(nnz_total, dtype=np.int32)
    rows = np.empty(nnz_total, dtype=np.int32)
    cols = np.empty(nnz_total, dtype=np.int32)

    #Calculate ranks, while keeping the matrix sparse
    ptr = 0
    for j in range(n_cells):
        col = Xarr[j, :].astype(float)
        col[np.isnan(col)] = -np.inf
        ranks = rankdata(-col, method=ties_method)
        mask = ranks <= max_rank  #mask out ranks to impose sparsity
        idx = np.nonzero(mask)[0]
        rks = ranks[idx].astype(np.int32)
        n = len(idx)

        data[ptr:ptr+n] = rks
        rows[ptr:ptr+n] = idx
        cols[ptr:ptr+n] = j
        ptr += n

    # slice arrays to actual size
    data = data[:ptr]
    rows = rows[:ptr]
    cols = cols[:ptr]

    ranks_mat = sparse.coo_matrix((data, (rows,cols)), shape=(n_genes,n_cells)).tocsr()
    
    return ranks_mat
