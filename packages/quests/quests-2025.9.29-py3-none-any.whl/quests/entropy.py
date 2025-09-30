import math
from typing import List, Tuple, Union

import numba as nb
import numpy as np

from .geometry import cutoff_fn
from .matrix import cdist, norm, sumexp, wsumexp

DEFAULT_BANDWIDTH = 0.015
DEFAULT_BATCH = 20000
DEFAULT_UQ_NBRS = 3
DEFAULT_GRAPH_NBRS = 10


def perfect_entropy(
    x: np.ndarray,
    h: Union[float, List[float]] = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Deprecated. Please use `entropy`.

    Computes the perfect entropy of a dataset using a batch distance
        calculation. This is necessary because the full distance matrix
        often does not fit in the memory for a big dataset. This function
        can be SLOW, despite the optimization of the computation, as it
        does not approximate the results.

    Arguments:
        x (np.ndarray): an (N, d) matrix with the descriptors
        h (int or np.nadarray): bandwidth (value / vector) for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        entropy (float): entropy of the dataset given by `x`.
            or (np.ndarray): if 'h' is a vector
    """
    return entropy(x, h, batch_size)


def entropy(
    x: np.ndarray,
    h: Union[float, List[float]] = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the perfect entropy of a dataset using a batch distance
        calculation. This is necessary because the full distance matrix
        often does not fit in the memory for a big dataset. This function
        can be SLOW, despite the optimization of the computation, as it
        does not approximate the results.

    Arguments:
        x (np.ndarray): an (N, d) matrix with the descriptors
        h (int or np.nadarray): bandwidth (value / vector) for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        entropy (float): entropy of the dataset given by `x`.
            or (np.ndarray): if 'h' is a vector
    """
    N = x.shape[0]
    if type(h) is np.ndarray:
        p_x = kernel_sum_multi_bandwidth(x, x, h=h, batch_size=batch_size)
        # normalizes the p(x) prior to the log for numerical stability
        p_x = np.log(p_x / N)
        return -np.mean(p_x, axis=0)
    else:
        p_x = kernel_sum(x, x, h=h, batch_size=batch_size)
        # normalizes the p(x) prior to the log for numerical stability
        p_x = np.log(p_x / N)
        return -np.mean(p_x)


def delta_entropy(
    y: np.ndarray,
    x: np.ndarray,
    h: float = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the differential entropy of a dataset `y` using the dataset
        `x` as reference. This function can be SLOW, despite the optimization
        of the computation, as it does not approximate the results.

    Arguments:
        y (np.ndarray): an (M, d) matrix with the descriptors of the test set
        x (np.ndarray): an (N, d) matrix with the descriptors of the reference
        h (int or np.nadarray): bandwidth (value / vector) for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        dH (np.ndarray): an (M,) vector of differential entropy dH ( Y | X )
            or (np.ndarray): an (H,M) matrix if 'h' is a vector of length H
    """
    if type(h) is np.ndarray:
        p_y = kernel_sum_multi_bandwidth(y, x, h=h, batch_size=batch_size)
    else:
        p_y = kernel_sum(y, x, h=h, batch_size=batch_size)
    return -np.log(p_y)


def diversity(
    x: np.ndarray,
    h: Union[float, List[float]] = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the diversity of a dataset `x` by assuming a sum over the
        inverse p(x). This approximates the number of unique data points
        in the system, as Kij >= 1 for a kernel matrix of a dataset.

    Arguments:
        x (np.ndarray): an (N, d) matrix with the descriptors of the dataset
        h (int or np.nadarray): bandwidth (value / vector) for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        entropy (float): entropy of the dataset given by `x`.
            or (np.ndarray): if 'h' is a vector
    """
    if type(h) is np.ndarray:
        p_x = kernel_sum_multi_bandwidth(x, x, h=h, batch_size=batch_size)
        return np.log(np.sum((1 / p_x), axis=0))
    else:
        p_x = kernel_sum(x, x, h=h, batch_size=batch_size)
        return np.log(np.sum(1 / p_x))


def get_all_metrics(
    x: np.ndarray,
    h: Union[float, List[float]] = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the entropy and diversity of a dataset `x`. This function is
        slightly faster than computing them separately, as one computes p(x)
        only once instead of twice.

    Arguments:
        x (np.ndarray): an (N, d) matrix with the descriptors of the dataset
        h (int or np.nadarray): bandwidth (value / vector) for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        entropy (float): entropy of the dataset given by `x`.
        diversity (float): diversity of the dataset given by `x`.
        dH (np.ndarray): an (M,) vector of differential entropy dH ( X | X )
    """
    N = x.shape[0]
    p_x = kernel_sum(x, x, h=h, batch_size=batch_size)
    dH = -np.log(p_x)
    div = np.log(np.sum(1 / p_x))
    ent = -np.mean(np.log(p_x / N))
    return ent, div, dH


@nb.njit(fastmath=True, parallel=True, cache=True)
def find_equal(
    x: np.ndarray,
    y: np.ndarray,
    batch_size: int = DEFAULT_BATCH,
    eps: float = 1e-5,
):
    """Find the data points in x corresponding to those in y.
        Because the entire matrix cannot fit in the memory, this function
        performs the calculations in batches.

    Arguments:
        x (np.ndarray): an (M, d) matrix with the test descriptors
        y (np.ndarray): an (N, d) matrix with the reference descriptors
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.
        eps (float): threshold to consider points as equal.

    Returns:
        idx (np.ndarray): a (N,) vector containing the indices of the
            rows of `x` corresponding to the rows of `y`.
    """
    M = x.shape[0]
    max_step_x = math.ceil(M / batch_size)

    N = y.shape[0]
    max_step_y = math.ceil(N / batch_size)

    # precomputing the norms saves us some time
    norm_x = norm(x)
    norm_y = norm(y)

    # variables that are going to store the results
    idx = np.full(N, -1, dtype=nb.int64)

    # loops over rows and columns to compute the
    # distance matrix without keeping it entirely
    # in the memory
    for step_x in nb.prange(0, max_step_x):
        i = step_x * batch_size
        imax = min(i + batch_size, M)
        x_batch = x[i:imax]
        x_batch_norm = norm_x[i:imax]

        # loops over all columns in batches to prevent memory overflow
        for step_y in range(0, max_step_y):
            j = step_y * batch_size
            jmax = min(j + batch_size, N)
            y_batch = y[j:jmax]
            y_batch_norm = norm_y[j:jmax]

            # computing the distance
            z = cdist(x_batch, y_batch, x_batch_norm, y_batch_norm)

            # find the index
            for kj in range(j, jmax):
                # skip the comparison if we already found one equivalent
                if idx[kj] > -1:
                    continue

                # compares all rows with all columns
                for ki in range(i, imax):
                    if z[ki - i, kj - j] < eps:
                        idx[kj] = ki

    return idx


@nb.njit(fastmath=True, parallel=True, cache=True)
def kernel_sum(
    x: np.ndarray,
    y: np.ndarray,
    h: float = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the kernel matrix K_ij for the descriptors x_i and y_j.
        Because the entire matrix cannot fit in the memory, this function
        automatically applies the kernel and sums the results, essentially
        recovering the probability distribution p(x) up to a normalization
        constant.

    Arguments:
        x (np.ndarray): an (M, d) matrix with the test descriptors
        y (np.ndarray): an (N, d) matrix with the reference descriptors
        h (int): bandwidth for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        ki (np.ndarray): a (M,) vector containing the probability of x_i
            given `y`
    """
    M = x.shape[0]
    max_step_x = math.ceil(M / batch_size)

    N = y.shape[0]
    max_step_y = math.ceil(N / batch_size)

    # precomputing the norms saves us some time
    norm_x = norm(x)
    norm_y = norm(y)

    # variables that are going to store the results
    p_x = np.zeros(M, dtype=x.dtype)

    # loops over rows and columns to compute the
    # distance matrix without keeping it entirely
    # in the memory
    for step_x in nb.prange(0, max_step_x):
        i = step_x * batch_size
        imax = min(i + batch_size, M)
        x_batch = x[i:imax]
        x_batch_norm = norm_x[i:imax]

        # loops over all columns in batches to prevent memory overflow
        for step_y in range(0, max_step_y):
            j = step_y * batch_size
            jmax = min(j + batch_size, N)
            y_batch = y[j:jmax]
            y_batch_norm = norm_y[j:jmax]

            # computing the estimated probability distribution for the batch
            z = cdist(x_batch, y_batch, x_batch_norm, y_batch_norm)
            z = z / h
            z = sumexp(-0.5 * (z**2))

            for k in range(i, imax):
                p_x[k] = p_x[k] + z[k - i]

    return p_x


@nb.njit(fastmath=True, parallel=True, cache=True)
def kernel_sum_multi_bandwidth(
    x: np.ndarray,
    y: np.ndarray,
    h: np.ndarray = np.array(DEFAULT_BANDWIDTH),
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the kernel matrix K_ij for the descriptors x_i and y_j.
        Because the entire matrix cannot fit in the memory, this function
        automatically applies the kernel and sums the results, essentially
        recovering the probability distribution p(x) up to a normalization
        constant.

    Arguments:
        x (np.ndarray): an (M, d) matrix with the test descriptors
        y (np.ndarray): an (N, d) matrix with the reference descriptors
        h (np.ndarray): bandwidth (H) vector for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        ki (np.ndarray): an (M, H) matrix containing the probability of x_i
            given `y` for each bandwidth 'h'
    """
    M = x.shape[0]
    max_step_x = math.ceil(M / batch_size)

    N = y.shape[0]
    max_step_y = math.ceil(N / batch_size)

    # precomputing the norms saves us some time
    norm_x = norm(x)
    norm_y = norm(y)

    # variables that are going to store the results
    H = h.shape[0]
    p_x = np.zeros((M, H), dtype=x.dtype)

    # loops over rows and columns to compute the
    # distance matrix without keeping it entirely
    # in the memory
    for step_x in nb.prange(0, max_step_x):
        i = step_x * batch_size
        imax = min(i + batch_size, M)
        x_batch = x[i:imax]
        x_batch_norm = norm_x[i:imax]

        # loops over all columns in batches to prevent memory overflow
        for step_y in range(0, max_step_y):
            j = step_y * batch_size
            jmax = min(j + batch_size, N)
            y_batch = y[j:jmax]
            y_batch_norm = norm_y[j:jmax]

            # computing the estimated probability distribution for the batch
            z = cdist(x_batch, y_batch, x_batch_norm, y_batch_norm)
            for h_i in range(H):
                h0 = h[h_i]
                zm = z / h0
                zm = sumexp(-0.5 * (zm**2))
                for k in range(i, imax):
                    p_x[k, h_i] = p_x[k, h_i] + zm[k - i]
    return p_x


@nb.njit(fastmath=True, parallel=True, cache=True)
def weighted_kernel_sum(
    x: np.ndarray,
    y: np.ndarray,
    w: np.ndarray,
    h: float = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the product w_j * K_ij for the descriptors x_i and y_j, and
        a given weight w_j of same size as y_j.

    Arguments:
        x (np.ndarray): an (M, d) matrix with the test descriptors
        y (np.ndarray): an (N, d) matrix with the reference descriptors
        w (np.ndarray): an (N,) vector with the weights
        h (int): bandwidth for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        (q, ki) (tuple): where q and ki are as described below
        q (np.ndarray): a (M,) vector containing the weighted average of w
            given `y`
        ki (np.ndarray): a (M,) vector containing the probability of x_i
            given `y`
    """
    M = x.shape[0]
    max_step_x = math.ceil(M / batch_size)

    N = y.shape[0]
    max_step_y = math.ceil(N / batch_size)

    # precomputing the norms saves us some time
    norm_x = norm(x)
    norm_y = norm(y)

    # variables that are going to store the results
    p_x = np.zeros(M, dtype=x.dtype)
    w_x = np.zeros(M, dtype=x.dtype)

    # loops over rows and columns to compute the
    # distance matrix without keeping it entirely
    # in the memory
    for step_x in nb.prange(0, max_step_x):
        i = step_x * batch_size
        imax = min(i + batch_size, M)
        x_batch = x[i:imax]
        x_batch_norm = norm_x[i:imax]

        # loops over all columns in batches to prevent memory overflow
        for step_y in range(0, max_step_y):
            j = step_y * batch_size
            jmax = min(j + batch_size, N)
            y_batch = y[j:jmax]
            y_batch_norm = norm_y[j:jmax]

            w_batch = w[j:jmax]

            # computing the estimated probability distribution for the batch
            z = cdist(x_batch, y_batch, x_batch_norm, y_batch_norm)
            z = z / h
            z = -0.5 * (z**2)

            # computed the expected value of the error
            p = sumexp(z)
            wp = wsumexp(z, w_batch)

            for k in range(i, imax):
                p_x[k] = p_x[k] + p[k - i]
                w_x[k] = w_x[k] + wp[k - i]

        for k in range(i, imax):
            w_x[k] = w_x[k] / p_x[k]

    return w_x, p_x


@nb.njit(fastmath=True, parallel=True, cache=True)
def weighted_kernel_sum_multi_bandwidth(
    x: np.ndarray,
    y: np.ndarray,
    w: np.ndarray,
    h: float = DEFAULT_BANDWIDTH,
    batch_size: int = DEFAULT_BATCH,
):
    """Computes the product w_j * K_ij for the descriptors x_i and y_j, and
        a given weight w_j of same first dimension length as y_j.

    Arguments:
        x (np.ndarray): an (M, d) matrix with the test descriptors
        y (np.ndarray): an (N, d) matrix with the reference descriptors
        w (np.ndarray): an (N,) vector with the weights
        h (np.ndarray): bandwidth (H) vector for the Gaussian kernel
        batch_size (int): maximum batch size to consider when
            performing a distance calculation.

    Returns:
        (q, ki) (tuple): where q and ki are as described below
        q (np.ndarray): an (M, H) matrix containing the weighted average of w
            given `y` for each bandwidth 'h'
        ki (np.ndarray): an (M, H) matrix containing the probability of x_i
            given `y` for each bandwidth 'h'
    """
    M = x.shape[0]
    max_step_x = math.ceil(M / batch_size)

    N = y.shape[0]
    max_step_y = math.ceil(N / batch_size)

    # precomputing the norms saves us some time
    norm_x = norm(x)
    norm_y = norm(y)

    # variables that are going to store the results
    H = h.shape[0]
    p_x = np.zeros((M, H), dtype=x.dtype)
    w_x = np.zeros((M, H), dtype=x.dtype)

    # loops over rows and columns to compute the
    # distance matrix without keeping it entirely
    # in the memory
    for step_x in nb.prange(0, max_step_x):
        i = step_x * batch_size
        imax = min(i + batch_size, M)
        x_batch = x[i:imax]
        x_batch_norm = norm_x[i:imax]

        # loops over all columns in batches to prevent memory overflow
        for step_y in range(0, max_step_y):
            j = step_y * batch_size
            jmax = min(j + batch_size, N)
            y_batch = y[j:jmax]
            y_batch_norm = norm_y[j:jmax]

            w_batch = w[j:jmax]

            # computing the estimated probability distribution for the batch
            z = cdist(x_batch, y_batch, x_batch_norm, y_batch_norm)
            for h_i in range(H):
                h0 = h[h_i]
                zm = z / h0
                zm = -0.5 * (zm**2)

                # computed the expected value of the error
                p = sumexp(zm)
                wp = wsumexp(zm, w_batch)
                for k in range(i, imax):
                    p_x[k, h_i] = p_x[k, h_i] + p[k - i]
                    w_x[k, h_i] = w_x[k, h_i] + wp[k - i]

        for k in range(i, imax):
            for h_i in range(H):
                w_x[k, h_i] = w_x[k, h_i] / p_x[k, h_i]

    return w_x, p_x


def get_bandwidth(volume: float, method: str = "gaussian"):
    """Estimate of the bandwidth based on the dependence
        of the entropy w.r.t. volume per atom (or density).
        The hard-coded parameters here were shown to work
        well for some systems.

    Arguments:
        volume (float): volume per atom (in Å^3/atom)

    Returns:
        bandwidth (float)
    """
    if method == "gaussian":
        z = volume / 10.896
        return 0.0897141 * np.exp(-0.5 * z**2) + 0.0119417

    if method == "cutoff":
        z = np.power(np.log(volume), 2)
        return 0.086164 * cutoff_fn(z, 11.61172) + 0.016


def approx_delta_entropy(
    y: np.ndarray,
    x: np.ndarray,
    h: float = DEFAULT_BANDWIDTH,
    n: int = DEFAULT_UQ_NBRS,
    graph_neighbors: int = DEFAULT_GRAPH_NBRS,
    **kwargs,
):
    """Computes an approximate differential entropy of a dataset `y` using the dataset
        `x` as reference. This function was optimized to be FAST and multithreaded, but
        the recall may not be 100%. If recall is an issue, please consult the PyNNDescent
        documentation for the choice of keywords.

    Arguments:
        y (np.ndarray): an (M, d) matrix with the descriptors of the test set
        x (np.ndarray): an (N, d) matrix with the descriptors of the reference
        h (int or np.nadarray): bandwidth (value / vector) for the Gaussian kernel
        k (int): number of nearest-neighbors to take into account when computing
            the approximate dH

    Returns:
        dH (np.ndarray): (M,) approx. differential entropy of the dataset given by `x`.
            or (np.ndarray): an (H,M) matrix if 'h' is a vector of length H
    """
    import pynndescent as nnd

    index = nnd.NNDescent(x, n_neighbors=graph_neighbors, **kwargs)
    index.prepare()

    _, d = index.query(y, k=n)
    if type(h) is np.ndarray:
        # variables that are going to store the results
        len_h = h.shape[0]
        imax = y.shape[0]
        p_y = np.zeros((len_h, imax), dtype=y.dtype)
        for h_i in range(len_h):
            h0 = h[h_i]
            zm = d / h0
            zm = sumexp(-0.5 * zm**2)
            p_y[h_i, :] = zm

    else:
        z = d / h
        p_y = sumexp(-0.5 * z**2)

    return -np.log(p_y)
