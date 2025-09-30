"""Collection of utility functions"""

import datetime
import logging
import os
import warnings
from typing import Any, Callable, List, Optional, Tuple, Union

import astropy.units as u
import numpy as np
import numpy.typing as npt
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy.io import fits
from patsy import dmatrix
from scipy import optimize, sparse
from scipy.ndimage import gaussian_filter1d

from . import PACKAGEDIR, __version__

log = logging.getLogger(__name__)

warnings.simplefilter("ignore", sparse.SparseEfficiencyWarning)


def _make_A_polar(
    phi: npt.ArrayLike,
    r: npt.ArrayLike,
    cut_r: float = 6,
    rmin: float = 1,
    rmax: float = 18,
    n_r_knots: int = 12,
    n_phi_knots: int = 15,
) -> sparse.spmatrix:
    """
    Creates a design matrix (DM) in polar coordinates (r, phi). It will enforce r-only
    dependency within `cut_r` radius. This is useful when less data points are available
    near the center.

    Parameters
    ----------
    phi : np.ndarray
        Array of angle (phi) values in polar coordinates. Must have values in the
        [-pi, pi] range.
    r : np.ndarray
        Array of radii values in polar coordinates.
    cut_r : float
        Radius (units consistent with `r`) whitin the DM only has radius dependency
        and not angle.
    rmin : float
        Radius where the DM starts.
    rmax : float
        Radius where the DM ends.
    n_r_knots : int
        Number of knots used for the spline in radius.
    n_phi_knots : int
        Number of knots used for the spline in angle.
    Returns
    -------
    X : sparse CSR matrix
        A DM with bspline basis in polar coordinates.
    """
    # create the spline bases for radius and angle
    phi_spline = sparse.csr_matrix(wrapped_spline(phi, order=3, nknots=n_phi_knots).T)
    r_knots = np.linspace(rmin**0.5, rmax**0.5, n_r_knots) ** 2
    cut_r_int = np.where(r_knots <= cut_r)[0].max()
    r_spline = sparse.csr_matrix(
        np.asarray(
            dmatrix(
                "bs(x, knots=knots, degree=3, include_intercept=True)",
                {"x": list(np.hstack([r, rmin, rmax])), "knots": r_knots},
            )
        )
    )[:-2]

    # build full desing matrix
    X = sparse.hstack(
        [phi_spline.multiply(r_spline[:, idx]) for idx in range(r_spline.shape[1])],
        format="csr",
    )
    # find and remove the angle dependency for all basis for radius < 6
    cut = np.arange(0, phi_spline.shape[1] * cut_r_int)
    a = list(set(np.arange(X.shape[1])) - set(cut))
    X1 = sparse.hstack(
        [X[:, a], r_spline[:, 1:cut_r_int], sparse.csr_matrix(np.ones(X.shape[0])).T],
        format="csr",
    )
    return X1


def spline1d(
    x: npt.ArrayLike, knots: npt.ArrayLike, degree: int = 3, include_knots: bool = False
) -> sparse.spmatrix:
    """
    Make a bspline design matrix (DM) for 1D variable `x`.

    Parameters
    ----------
    x : np.ndarray
        Array of values to create the DM.
    knots : np.ndarray
        Array of knots to be used in the DM.
    degree : int
        Degree of the spline, default is 3.
    include_knots : boolean
        Include or not the knots in the `x` vector, this forces knots in case
        out of bound values.

    Returns
    -------
    X : sparse CSR matrix
        A DM with bspline basis for vector `x`.
    """
    if include_knots:
        x = np.hstack([knots.min(), x, knots.max()])
    X = sparse.csr_matrix(
        np.asarray(
            dmatrix(
                "bs(x, knots=knots, degree=degree, include_intercept=True)",
                {"x": list(x), "knots": knots, "degree": degree},
            )
        )
    )
    if include_knots:
        X = X[1:-1]
        x = x[1:-1]
    if not X.shape[0] == x.shape[0]:
        raise ValueError("`patsy` has made the wrong matrix.")
    X = X[:, np.asarray(X.sum(axis=0) != 0)[0]]
    return X


def _make_A_cartesian(
    x: npt.ArrayLike,
    y: npt.ArrayLike,
    n_knots: int = 10,
    radius: Optional[float] = None,
    degree: int = 3,
    knot_spacing_type: str = "sqrt",
) -> sparse.spmatrix:
    """
    Creates a design matrix (DM) in Cartersian coordinates (r, phi).

    Parameters
    ----------
    x : np.ndarray
        Array of x values in Cartersian coordinates.
    y : np.ndarray
        Array of y values in Cartersian coordinates.
    n_knots : int
        Number of knots used for the spline.
    radius : float
        Distance from 0 to the furthes knot.
    knot_spacing_type : string
        Type of spacing betwen knots, options are "linear" or "sqrt".
    degree : int
        Degree of the spline, default is 3.

    Returns
    -------
    X : sparse CSR matrix
        A DM with bspline basis in Cartersian coordinates.
    """
    # Must be odd
    n_odd_knots = n_knots if n_knots % 2 == 1 else n_knots + 1
    if radius is not None:
        if knot_spacing_type == "sqrt":
            x_knots = np.linspace(-np.sqrt(radius), np.sqrt(radius), n_odd_knots)
            x_knots = np.sign(x_knots) * x_knots**2
            y_knots = np.linspace(-np.sqrt(radius), np.sqrt(radius), n_odd_knots)
            y_knots = np.sign(y_knots) * y_knots**2
        else:
            x_knots = np.linspace(-radius, radius, n_odd_knots)
            y_knots = np.linspace(-radius, radius, n_odd_knots)
    else:
        x_knots = np.linspace(*np.percentile(x, [0, 100]), n_odd_knots)
        y_knots = np.linspace(*np.percentile(y, [0, 100]), n_odd_knots)

    x_spline = spline1d(x, knots=x_knots, degree=degree, include_knots=True)
    y_spline = spline1d(y, knots=y_knots, degree=degree, include_knots=True)

    x_spline = x_spline[:, np.asarray(x_spline.sum(axis=0))[0] != 0]
    y_spline = y_spline[:, np.asarray(y_spline.sum(axis=0))[0] != 0]
    X = sparse.hstack(
        [x_spline.multiply(y_spline[:, idx]) for idx in range(y_spline.shape[1])],
        format="csr",
    )
    return X


def wrapped_spline(
    input_vector: npt.ArrayLike, order: int = 2, nknots: int = 10
) -> np.ndarray:
    """
    Creates a vector of folded-spline basis according to the input data. This is meant
    to be used to build the basis vectors for periodic data, like the angle in polar
    coordinates.

    Parameters
    ----------
    input_vector : numpy.ndarray
        Input data to create basis, angle values MUST BE BETWEEN -PI and PI.
    order : int
        Order of the spline basis
    nknots : int
         Number of knots for the splines

    Returns
    -------
    folded_basis : numpy.ndarray
        Array of folded-spline basis
    """

    if not ((input_vector >= -np.pi) & (input_vector <= np.pi)).all():
        raise ValueError("Must be between -pi and pi")
    x = np.copy(input_vector)
    x1 = np.hstack([x, x + np.pi * 2])
    nt = (nknots * 2) + 1

    t = np.linspace(-np.pi, 3 * np.pi, nt)
    dt = np.median(np.diff(t))
    # Zeroth order basis
    basis = np.asarray(
        [
            ((x1 >= t[idx]) & (x1 < t[idx + 1])).astype(float)
            for idx in range(len(t) - 1)
        ]
    )
    # Higher order basis
    for order in np.arange(1, 4):
        basis_1 = []
        for idx in range(len(t) - 1):
            a = ((x1 - t[idx]) / (dt * order)) * basis[idx]

            if (idx + order + 1) < (nt - 1):
                b = (-(x1 - t[(idx + order + 1)]) / (dt * order)) * basis[
                    (idx + 1) % (nt - 1)
                ]
            else:
                b = np.zeros(len(x1))
            basis_1.append(a + b)
        basis = np.vstack(basis_1)

    folded_basis = np.copy(basis)[: nt // 2, : len(x)]
    for idx in np.arange(-order, 0):
        folded_basis[idx, :] += np.copy(basis)[nt // 2 + idx, len(x) :]
    return folded_basis


def solve_linear_model(
    A: Union[npt.ArrayLike, sparse.spmatrix],
    y: npt.ArrayLike,
    y_err: Optional[npt.ArrayLike] = None,
    prior_mu: Optional[float] = None,
    prior_sigma: Optional[float] = None,
    k: Optional[npt.ArrayLike] = None,
    errors: bool = False,
    nnls: bool = False,
) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]:
    """
    Solves a linear model with design matrix A and observations y:
        Aw = y
    return the solutions w for the system assuming Gaussian priors.
    Alternatively the observation errors, priors, and a boolean mask for the
    observations (row axis) can be provided.

    Adapted from Luger, Foreman-Mackey & Hogg, 2017
    (https://ui.adsabs.harvard.edu/abs/2017RNAAS...1....7L/abstract)

    Parameters
    ----------
    A: numpy ndarray or scipy sparce csr matrix
        Desging matrix with solution basis
        shape n_observations x n_basis
    y: numpy ndarray
        Observations
        shape n_observations
    y_err: numpy ndarray, optional
        Observation errors
        shape n_observations
    prior_mu: float, optional
        Mean of Gaussian prior values for the weights (w)
    prior_sigma: float, optional
        Standard deviation of Gaussian prior values for the weights (w)
    k: boolean, numpy ndarray, optional
        Mask that sets the observations to be used to solve the system
        shape n_observations
    errors: boolean
        Whether to return error estimates of the best fitting weights

    Returns
    -------
    w: numpy ndarray
        Array with the estimations for the weights
        shape n_basis
    werrs: numpy ndarray
        Array with the error estimations for the weights, returned if `error` is True
        shape n_basis
    """
    if k is None:
        k = np.ones(len(y), dtype=bool)

    if y_err is not None:
        sigma_w_inv = A[k].T.dot(A[k].multiply(1 / y_err[k, None] ** 2))
        B = A[k].T.dot((y[k] / y_err[k] ** 2))
    else:
        sigma_w_inv = A[k].T.dot(A[k])
        B = A[k].T.dot(y[k])

    if prior_mu is not None and prior_sigma is not None:
        sigma_w_inv += np.diag(1 / prior_sigma**2)
        B += prior_mu / prior_sigma**2

    if isinstance(sigma_w_inv, (sparse.csr_matrix, sparse.csc_matrix)):
        sigma_w_inv = sigma_w_inv.toarray()
    if isinstance(sigma_w_inv, np.matrix):
        sigma_w_inv = np.asarray(sigma_w_inv)

    if nnls:
        w, _ = optimize.nnls(
            sigma_w_inv,
            B,
        )
    else:
        # w, _, _, _ = np.linalg.lstsq(sigma_w_inv, B)
        w = np.linalg.solve(sigma_w_inv, B)
    if errors is True:
        w_err = np.linalg.inv(sigma_w_inv).diagonal() ** 0.5
        return w, w_err
    return w


def sparse_lessthan(
    arr: sparse.spmatrix, limit: Union[float, npt.ArrayLike]
) -> sparse.spmatrix:
    """
    Compute less than operation on sparse array by evaluating only non-zero values
    and reconstructing the sparse array. This function return a sparse array, which is
    crutial to keep operating large matrices.

    Notes: when doing `x < a` for a sparse array `x` and `a > 0` it effectively compares
    all zero and non-zero values. Then we get a dense boolean array with `True` where
    the condition is met but also `True` where the sparse array was zero.
    To avoid this we evaluate the condition only for non-zero values in the sparse
    array and later reconstruct the sparse array with the right shape and content.
    When `x` is a [N * M] matrix and `a` is [N] array, and we want to evaluate the
    condition per row, we need to iterate over rows to perform the evaluation and then
    reconstruct the masked sparse array.

    Parameters
    ----------
    arr : scipy.sparse
        Sparse array to be masked, is a 2D matrix.
    limit : float, numpy.array
        Upper limit to evaluate less than. If float will do `arr < limit`. If array,
        shape has to match first dimension of `arr` to do `arr < limi[:, None]`` and
        evaluate the condition per row.

    Returns
    -------
    masked_arr : scipy.sparse.csr_matrix
        Sparse array after less than evaluation.
    """
    nonz_idx = arr.nonzero()
    # apply condition for each row
    if isinstance(limit, np.ndarray) and limit.shape[0] == arr.shape[0]:
        mask = [arr[s].data < limit[s] for s in set(nonz_idx[0])]
        # flatten mask
        mask = [x for sub in mask for x in sub]
    else:
        mask = arr.data < limit
    # reconstruct sparse array
    masked_arr = sparse.csr_matrix(
        (arr.data[mask], (nonz_idx[0][mask], nonz_idx[1][mask])),
        shape=arr.shape,
    ).astype(bool)
    return masked_arr


def _combine_A(
    A: sparse.spmatrix,
    poscorr: Optional[List[np.ndarray]] = None,
    time: Optional[npt.ArrayLike] = None,
) -> sparse.spmatrix:
    """
    Combines a design matrix A (cartesian) with a time corrector type.
    If poscorr is provided, A will be combined with both axis of the pos corr as a
    1st degree polynomial.
    If time is provided, A will be combined with the time values as a 3rd degree
    polynomialin time.

    Parameters
    ----------
    A : sparse.csr_matrix
        A sparse design matix in of cartesian coordinates created with _make_A_cartesian
    poscorr : list
        A list of pos_corr arrays for axis 1 and 2
    time : numpy.array
        An array with time values
    """
    if poscorr:
        # Cartesian spline with poscor dependence
        A2 = sparse.hstack(
            [
                A,
                A.multiply(poscorr[0].ravel()[:, None]),
                A.multiply(poscorr[1].ravel()[:, None]),
                A.multiply((poscorr[0] * poscorr[1]).ravel()[:, None]),
            ],
            format="csr",
        )
        return A2
    elif time is not None:
        # Cartesian spline with time dependence
        A2 = sparse.hstack(
            [
                A,
                A.multiply(time.ravel()[:, None]),
                A.multiply(time.ravel()[:, None] ** 2),
                A.multiply(time.ravel()[:, None] ** 3),
            ],
            format="csr",
        )
        return A2


def threshold_bin(
    x: npt.ArrayLike,
    y: npt.ArrayLike,
    z: npt.ArrayLike,
    z_err: Optional[npt.ArrayLike] = None,
    abs_thresh: int = 10,
    bins: int = 15,
    statistic: Callable = np.nanmedian,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Function to bin 2D data and compute array statistic based on density.
    This function inputs 2D coordinates, e.g. `X` and `Y` locations, and a number value
    `Z` for each point in the 2D space. It bins the 2D spatial data to then compute
    a `statistic`, e.g. median, on the Z value based on bin members. The `statistic`
    is computed only for bins with more than `abs_thresh` members. It preserves data
    when the number of bin memebers is lower than `abs_thresh`.

    Parameters
    ----------
    x : numpy.ndarray
        Data array with spatial coordinate 1.
    y : numpy.ndarray
        Data array with spatial coordinate 2.
    z : numpy.ndarray
        Data array with the number values for each (X, Y) point.
    z_err : numpy.ndarray
        Array with errors values for z.
    abs_thresh : int
        Absolute threshold is the number of bib members to compute the statistic,
        otherwise data will be preserved.
    bins : int or list of ints
        Number of bins. If int, both axis will have same number of bins. If list, number
        of bins for first (x) and second (y) dimension.
    statistic : callable()
        The statistic as a callable function that will be use in each bin.
        Default is `numpy.nanmedian`.

    Returns
    -------
    bin_map : numpy.ndarray
        2D histogram values
    new_x : numpy.ndarray
        Binned X data.
    new_y : numpy.ndarray
        Binned Y data.
    new_z : numpy.ndarray
        Binned Z data.
    new_z_err : numpy.ndarray
        BInned Z_err data if errors were provided. If no, inverse of the number of
        bin members are returned as weights.
    """
    if bins < 2 or bins > len(x):
        raise ValueError(
            "Number of bins is negative or higher than number of points in (x, y, z)"
        )
    if abs_thresh < 1:
        raise ValueError(
            "Absolute threshold is 0 or negative, please input a value > 0"
        )
    if isinstance(bins, int):
        bins = [bins, bins]

    xedges = np.linspace(np.nanmin(x), np.nanmax(x), num=bins[0] + 1)
    yedges = np.linspace(np.nanmin(y), np.nanmax(y), num=bins[1] + 1)
    bin_mask = np.zeros_like(z, dtype=bool)
    new_x, new_y, new_z, new_z_err, bin_map = [], [], [], [], []

    for j in range(1, len(xedges)):
        for k in range(1, len(yedges)):
            idx = np.where(
                (x >= xedges[j - 1])
                & (x < xedges[j])
                & (y >= yedges[k - 1])
                & (y < yedges[k])
            )[0]
            if len(idx) >= abs_thresh:
                bin_mask[idx] = True
                # we agregate bin memebers
                new_x.append((xedges[j - 1] + xedges[j]) / 2)
                new_y.append((yedges[k - 1] + yedges[k]) / 2)
                new_z.append(statistic(z[idx]))
                bin_map.append(len(idx))
                if isinstance(z_err, np.ndarray):
                    # agregate errors if provided and sccale by bin member number
                    new_z_err.append(np.sqrt(np.nansum(z_err[idx] ** 2)) / len(idx))

    # adding non-binned datapoints
    new_x.append(x[~bin_mask])
    new_y.append(y[~bin_mask])
    new_z.append(z[~bin_mask])
    bin_map.append(np.ones_like(z)[~bin_mask])

    if isinstance(z_err, np.ndarray):
        # keep original z errors if provided
        new_z_err.append(z_err[~bin_mask])
    else:
        new_z_err = 1 / np.hstack(bin_map)

    return (
        np.hstack(bin_map),
        np.hstack(new_x),
        np.hstack(new_y),
        np.hstack(new_z),
        np.hstack(new_z_err),
    )


def get_breaks(time: npt.ArrayLike, include_ext: bool = False) -> np.ndarray:
    """
    Finds discontinuity in the time array and return the break indexes.

    Parameters
    ----------
    time : numpy.ndarray
        Array with time values

    Returns
    -------
    splits : numpy.ndarray
        An array of indexes with the break positions
    """
    dts = np.diff(time)
    if include_ext:
        return np.hstack([0, np.where(dts > 5 * np.median(dts))[0] + 1, len(time)])
    else:
        return np.where(dts > 5 * np.median(dts))[0] + 1


def gaussian_smooth(
    y: npt.ArrayLike,
    x: Optional[npt.ArrayLike] = None,
    do_segments: bool = False,
    filter_size: int = 13,
    mode: str = "mirror",
    breaks: Optional[List[int]] = None,
) -> np.ndarray:
    """
    Applies a Gaussian smoothing to a curve.

    Parameters
    ----------
    y : numpy.ndarray or list of numpy.ndarray
        Arrays to be smoothen in the last axis
    x : numpy.ndarray
        Time array of same shape of `y` last axis used to find data discontinuity.
    filter_size : int
        Filter window size
    mode : str
        The `mode` parameter determines how the input array is extended
        beyond its boundaries. Options are {'reflect', 'constant', 'nearest', 'mirror',
        'wrap'}. Default is 'mirror'

    Returns
    -------
    y_smooth : numpy.ndarray
        Smooth array.
    """
    if isinstance(y, list):
        y = np.asarray(y)
    else:
        y = np.atleast_2d(y)

    if do_segments:
        if breaks is None and x is None:
            raise ValueError("Please provide `x` or `breaks` to have splits.")
        elif breaks is None and x is not None:
            splits = get_breaks(x, include_ext=True)
        else:
            splits = np.array(breaks)
        # find discontinuity in y according to x if provided
        if x is not None:
            grads = np.gradient(y, x, axis=1)
            # the 7-sigma here is hardcoded and found to work ok
            splits = np.unique(
                np.concatenate(
                    [splits, np.hstack([np.where(g > 7 * g.std())[0] for g in grads])]
                )
            )
    else:
        splits = [0, y.shape[-1]]

    y_smooth = []
    for i in range(1, len(splits)):
        y_smooth.append(
            gaussian_filter1d(
                y[:, splits[i - 1] : splits[i]],
                filter_size,
                mode=mode,
                axis=1,
            )
        )
    return np.hstack(y_smooth)


def bspline_smooth(
    y: npt.ArrayLike,
    x: Optional[npt.ArrayLike] = None,
    degree: int = 3,
    do_segments: bool = False,
    breaks: Optional[List[int]] = None,
    n_knots: int = 100,
) -> np.ndarray:
    """
    Applies a spline smoothing to a curve.

    Parameters
    ----------
    y : numpy.ndarray or list of numpy.ndarray
        Arrays to be smoothen in the last axis
    x : numpy.ndarray
        Optional. x array, as `y = f(x)`` used to find discontinuities in `f(x)`. If x
        is given then splits will be computed, if not `breaks` argument as to be provided.
    degree : int
        Degree of the spline fit, default is 3.
    do_segments : boolean
        Do the splines per segments with splits computed from data `x` or given in `breaks`.
    breaks : list of ints
        List of break indexes in `y`.
    nknots : int
        Number of knots for the B-Spline. If `do_segments` is True, knots will be
        distributed in each segment.

    Returns
    -------
    y_smooth : numpy.ndarray
        Smooth array.
    """
    if isinstance(y, list):
        y = np.asarray(y)
    else:
        y = np.atleast_2d(y)

    if do_segments:
        if breaks is None and x is None:
            raise ValueError("Please provide `x` or `breaks` to have splits.")
        elif breaks is None and x is not None:
            splits = get_breaks(x)
        else:
            splits = np.array(breaks)
        # find discontinuity in y according to x if provided
        if x is not None:
            grads = np.gradient(y, x, axis=1)
            # the 7-sigma here is hardcoded and found to work ok
            splits = np.unique(
                np.concatenate(
                    [splits, np.hstack([np.where(g > 7 * g.std())[0] for g in grads])]
                )
            )
    else:
        splits = [0, y.shape[-1]]

    y_smooth = []
    v = np.arange(y.shape[-1])
    DM = spline1d(
        v, knots=np.linspace(v.min(), v.max(), n_knots), degree=degree
    ).toarray()
    # do segments
    arr_splits = np.array_split(np.arange(len(v)), splits)
    masks = np.asarray(
        [np.in1d(np.arange(len(v)), x1).astype(float) for x1 in arr_splits]
    ).T
    DM = np.hstack([DM[:, idx][:, None] * masks for idx in range(DM.shape[1])])

    prior_mu = np.zeros(DM.shape[1])
    prior_sigma = np.ones(DM.shape[1]) * 1e5
    # iterate over vectors in y
    for v in range(y.shape[0]):
        weights = solve_linear_model(
            DM,
            y[v],
            prior_mu=prior_mu,
            prior_sigma=prior_sigma,
        )
        y_smooth.append(DM.dot(weights))
    return np.array(y_smooth)


def _find_uncontaminated_pixels(mask: sparse.spmatrix) -> sparse.spmatrix:
    """
    creates a mask of shape nsources x npixels where targets are not contaminated.
    This mask is used to select pixels to build the PSF model.
    """

    new_mask = mask.multiply(np.asarray(mask.sum(axis=0) == 1)[0]).tocsr()
    new_mask.eliminate_zeros()
    return new_mask


def to_fits(
    data: dict, path: Optional[str] = None, overwrite: bool = False, **extra_data: Any
) -> "fits.HDUList":
    """Converts the light curve to a FITS file in the Kepler/TESS file format.

    The FITS file will be returned as a `~astropy.io.fits.HDUList` object.
    If a `path` is specified then the file will also be written to disk.

    Parameters
    ----------
    data : dict
        Lightcurve data, time, flux, and flux_err
    path : str or None
        Location where the FITS file will be written, which is optional.
    overwrite : bool
        Whether or not to overwrite the file, if `path` is set.
    extra_data : dict
        Extra keywords or columns to include in the FITS file.
        Arguments of type str, int, float, or bool will be stored as
        keywords in the primary header.
        Arguments of type np.array or list will be stored as columns
        in the first extension.

    Returns
    -------
    hdu : `~astropy.io.fits.HDUList`
        Returns an `~astropy.io.fits.HDUList` object.
    """
    typedir = {
        int: "J",
        str: "A",
        float: "D",
        bool: "L",
        np.int16: "J",
        np.int32: "K",
        np.float32: "E",
        np.float64: "D",
    }

    def _header_template(extension):
        """Returns a template `fits.Header` object for a given extension."""
        template_fn = os.path.join(
            os.path.dirname(os.path.dirname(PACKAGEDIR)),
            "data",
            "templates",
            f"lc-ext{extension}-header.txt",
        )
        return fits.Header.fromtextfile(template_fn)

    def _make_primary_hdu(extra_data=None):
        """Returns the primary extension (#0)."""
        if extra_data is None:
            extra_data = {}
        hdu = fits.PrimaryHDU()
        # Copy the default keywords from a template file from the MAST archive
        tmpl = _header_template(0)
        for kw in tmpl:
            hdu.header[kw] = (tmpl[kw], tmpl.comments[kw])

        # Override the defaults where necessary
        default = {
            "ORIGIN": "Unofficial data product",
            "DATE": datetime.datetime.now().strftime("%Y-%m-%d"),
            "CREATOR": "trexs-roman-lcs.to_fits()",
            "PROCVER": str(__version__),
        }

        for kw in default:
            hdu.header["{}".format(kw).upper()] = default[kw]
            if default[kw] is None:
                log.info("Value for {} is None.".format(kw))

        for kw in extra_data:
            if isinstance(extra_data[kw], (str, float, int, bool, type(None))):
                hdu.header["{}".format(kw).upper()] = extra_data[kw]
                if extra_data[kw] is None:
                    log.info("Value for {} is None.".format(kw))
        return hdu

    def _make_lightcurve_extension(data, extra_data=None):
        """Create the 'LIGHTCURVE' extension (i.e. extension #1)."""
        # Turn the data arrays into fits columns and initialize the HDU
        if extra_data is None:
            extra_data = {}
        cols = []
        if "time" in data.keys():
            cols.append(
                fits.Column(
                    name="TIME",
                    format="D",
                    unit=u.day.to_string(),
                    array=data["time"],
                )
            )
        if "flux" in data.keys():
            cols.append(
                fits.Column(
                    name="FLUX",
                    format="E",
                    unit=(u.electron / u.second).to_string(),
                    array=data["flux"],
                )
            )
        if "flux_err" in data.keys():
            cols.append(
                fits.Column(
                    name="FLUX_ERR",
                    format="E",
                    unit=(u.electron / u.second).to_string(),
                    array=data["flux_err"],
                )
            )
        if "cadenceno" in data.keys():
            cols.append(
                fits.Column(name="CADENCENO", format="J", array=data["cadenceno"])
            )
        if "quality" in data.keys():
            cols.append(fits.Column(name="QUALITY", format="J", array=data["quality"]))
        for kw in extra_data:
            if isinstance(extra_data[kw], (np.ndarray, list)):
                cols.append(
                    fits.Column(
                        name="{}".format(kw).upper(),
                        format=typedir[extra_data[kw].dtype.type],
                        array=extra_data[kw],
                    )
                )

        coldefs = fits.ColDefs(cols)
        hdu = fits.BinTableHDU.from_columns(coldefs)
        hdu.header["EXTNAME"] = "LIGHTCURVE"
        return hdu

    def _hdulist(data, **extra_data):
        """Returns an astropy.io.fits.HDUList object."""
        list_out = fits.HDUList(
            [
                _make_primary_hdu(extra_data=extra_data),
                _make_lightcurve_extension(data, extra_data=extra_data),
            ]
        )
        return list_out

    hdu = _hdulist(data, **extra_data)
    if path is not None:
        hdu.writeto(path, overwrite=overwrite, checksum=True)
    return hdu


def clean_blends_in_catalog(
    catalog: pd.DataFrame,
    blend_limit: float,
    filter: str = "F146",
) -> pd.DataFrame:
    """
    Cleans the catalog by removing sources withing `blend_limit`.

    Parameters
    ----------
    catalog : pd.DataFrame
        The input catalog DataFrame containing 'ra' and 'dec' columns.
    blend_limit : float
        The distance limit in arcseconds to consider a source as a blend.
    remove : str
        The type of sources to remove. Options are 'faint' or 'bright'.

    Returns
    -------
    pd.DataFrame
        A cleaned DataFrame with rows containing NaN in 'ra' or 'dec' removed.
    """
    log.info(f"Limiting blended sources to > {blend_limit} arcsec")
    cat = SkyCoord(ra=catalog.ra.values * u.degree, dec=catalog.dec.values * u.degree)
    idxc, idxcat, d2d, _ = cat.search_around_sky(cat, blend_limit * u.arcsec)
    idxc = idxc[d2d > 0]
    idxcat = idxcat[d2d > 0]
    d2d = d2d[d2d > 0]
    dropfaint = []
    for ls, rs in zip(idxc, idxcat):
        if catalog.loc[ls, filter] > catalog.loc[rs, filter]:
            dropfaint.append(ls)
        else:
            dropfaint.append(rs)
    dropfaint = np.unique(dropfaint)
    log.info(f"Dropping {len(dropfaint)} faint blended catalog")
    catalog.drop(dropfaint, axis=0, inplace=True)
    catalog.reset_index(drop=True, inplace=True)

    return catalog


def matrix_solve(model, data, data_err=None, power=2.0):
    A = model.T
    # A = np.array(model)[:,None].T
    x = data.ravel()[:, None]

    if data_err is not None:
        x_err = data_err.ravel()[:, None]
        A = 1.0 / x_err**power * A
        x = 1.0 / x_err**power * x

    w = np.linalg.solve(A.T.dot(A), A.T.dot(x))

    return w
