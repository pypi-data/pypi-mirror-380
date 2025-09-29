import logging
import warnings
from typing import Union

import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from numba import njit

log = logging.getLogger(__name__)


class Checkerboarder:
    def __init__(self, n: Union[int, list] = None, dim=2, checkerboard_type="CheckPi"):  # noqa: E501
        """
        Initialize a Checkerboarder instance.

        Parameters
        ----------
        n : int or list, optional
            Number of grid partitions per dimension. If an integer is provided,
            the same number of partitions is used for each dimension.
            If None, defaults to 20 partitions per dimension.
        dim : int, optional
            The number of dimensions for the checkerboard grid.
            Defaults to 2.
        checkerboard_type : str, optional
            Specifies which checkerboard-based copula class to return.
            Possible values include:
              - "CheckPi", "BivCheckPi"
              - "CheckMin", "BivCheckMin"
              - "CheckW", "BivCheckW"
              - "Bernstein", "BernsteinCopula"
        """
        if n is None:
            n = 20
        if isinstance(n, (int, np.int_)):
            n = [n] * dim
        self.n = n
        self.d = len(self.n)
        self._checkerboard_type = checkerboard_type
        # Pre-compute common grid points for each dimension.
        self._precalculate_grid_points()

    def _precalculate_grid_points(self):
        """Pre-calculate grid points for each dimension, linearly spaced in [0,1]."""
        self.grid_points = []
        for n_i in self.n:
            points = np.linspace(0, 1, n_i + 1)
            self.grid_points.append(points)

    def get_checkerboard_copula(self, copula, n_jobs=None):
        """
        Compute the checkerboard representation of a copula's CDF.
        """
        log.debug("Computing checkerboard copula with grid sizes: %s", self.n)

        # If 2D and copula has a 'cdf_vectorized' method, do vectorized approach
        if hasattr(copula, "cdf_vectorized") and self.d == 2:
            return self._compute_checkerboard_vectorized(copula)

        # Otherwise, decide on serial vs parallel
        if n_jobs is None:
            total_cells = np.prod(self.n)
            n_jobs = max(1, min(8, total_cells // 1000))

        if n_jobs > 1 and np.prod(self.n) > 100:
            return self._compute_checkerboard_parallel(copula, n_jobs)
        return self._compute_checkerboard_serial(copula)

    def _compute_checkerboard_vectorized(self, copula, tol=1e-12):
        """
        Computes the checkerboard copula mass matrix in a highly optimized, vectorized manner.

        This method calculates the probability mass for each cell in the grid by first
        evaluating the copula's CDF at all grid intersection points in a single call.
        It then uses 2D finite differences on the resulting CDF grid to find the mass
        of each rectangular cell. This avoids redundant computations and is significantly
        faster than calculating the CDF for each cell's corners separately.
        """
        if self.d != 2:
            warnings.warn("Vectorized computation is only supported for the 2D case.")
            return self._compute_checkerboard_serial(copula)

        # 1. Get the unique grid points for each dimension.
        u_pts = self.grid_points[0]
        v_pts = self.grid_points[1]

        # 2. Create a meshgrid of all grid points.
        # This prepares the input for a single, comprehensive CDF evaluation.
        U, V = np.meshgrid(u_pts, v_pts, indexing="ij")

        # 3. Call the vectorized CDF function ONCE on the entire grid of points.
        # This is the core optimization, replacing four separate, expensive calls.
        cdf_grid = copula.cdf_vectorized(U, V)

        # 4. Compute the probability mass of each cell using fast 2D finite differences.
        # This is equivalent to the inclusion-exclusion principle for rectangles:
        # P(u_i<U<u_{i+1}, v_j<V<v_{j+1}) = C(u_{i+1},v_{j+1}) - C(u_{i+1},v_j) - C(u_i,v_{j+1}) + C(u_i,v_j)
        cmatr = (
            cdf_grid[1:, 1:]  # Upper-right corners of all cells
            - cdf_grid[1:, :-1]  # Upper-left corners
            - cdf_grid[:-1, 1:]  # Lower-right corners
            + cdf_grid[:-1, :-1]  # Lower-left corners
        )

        # 5. Handle potential floating-point inaccuracies.
        # The logic here remains the same as your original implementation.
        neg_mask = cmatr < 0
        if np.any(neg_mask):
            min_val = cmatr[neg_mask].min()
            if min_val < -tol:
                log.warning(
                    f"cmatr has {np.sum(neg_mask)} entries < -{tol:.1e}; "
                    f"most extreme = {min_val:.3e}"
                )
            cmatr[neg_mask] = 0.0  # Zero out any negative probabilities

        # Ensure the probabilities are clipped between 0 and 1.
        cmatr = np.clip(cmatr, 0, 1)

        return self._get_checkerboard_copula_for(cmatr)

    def _compute_checkerboard_parallel(self, copula, n_jobs):
        indices = list(np.ndindex(*self.n))
        results = Parallel(n_jobs=n_jobs)(
            delayed(self._process_cell)(idx, copula) for idx in indices
        )
        cmatr = np.zeros(self.n)
        for idx, value in zip(indices, results):
            cmatr[idx] = value
        return self._get_checkerboard_copula_for(cmatr)

    def _compute_checkerboard_serial(self, copula):
        cdf_cache = {}
        cmatr = np.zeros(self.n)
        indices = np.ndindex(*self.n)

        def get_cached_cdf(point):
            pt_tuple = tuple(point)
            if pt_tuple not in cdf_cache:
                val = copula.cdf(*point)
                if not isinstance(val, (float, int)):
                    val = float(val)
                cdf_cache[pt_tuple] = val
            return cdf_cache[pt_tuple]

        for idx in indices:
            u_lower = [self.grid_points[k][i] for k, i in enumerate(idx)]
            u_upper = [self.grid_points[k][i + 1] for k, i in enumerate(idx)]
            ie_sum = 0.0
            for corner in range(1 << self.d):
                corner_point = [
                    (u_upper[dim_idx] if corner & (1 << dim_idx) else u_lower[dim_idx])
                    for dim_idx in range(self.d)
                ]
                sign = (-1) ** (bin(corner).count("1") + self.d)
                ie_sum += sign * get_cached_cdf(corner_point)
            cmatr[idx] = ie_sum
        cmatr = np.clip(cmatr, 0, 1)
        return self._get_checkerboard_copula_for(cmatr)

    def _process_cell(self, idx, copula):
        u_lower = [self.grid_points[k][i] for k, i in enumerate(idx)]
        u_upper = [self.grid_points[k][i + 1] for k, i in enumerate(idx)]
        inclusion_exclusion_sum = 0.0
        for corner in range(1 << self.d):
            corner_point = [
                (u_upper[dim] if corner & (1 << dim) else u_lower[dim])
                for dim in range(self.d)
            ]
            sign = (-1) ** (bin(corner).count("1") + self.d)
            try:
                cdf_val = copula.cdf(*corner_point)
                cdf_val = float(cdf_val)
                inclusion_exclusion_sum += sign * cdf_val
            except Exception as e:
                log.warning(f"Error computing CDF at {corner_point}: {e}")
        return inclusion_exclusion_sum

    def _get_checkerboard_copula_for(self, cmatr):
        """
        Lazily import and return the appropriate checkerboard-like copula.
        """
        if self._checkerboard_type in ["CheckPi", "BivCheckPi"]:
            from copul.checkerboard.check_pi import CheckPi

            return CheckPi(cmatr)
        elif self._checkerboard_type in ["CheckMin", "BivCheckMin"]:
            from copul.checkerboard.check_min import CheckMin

            return CheckMin(cmatr)
        elif self._checkerboard_type in ["BivCheckW", "CheckW"]:
            from copul.checkerboard.biv_check_w import BivCheckW

            return BivCheckW(cmatr)
        elif self._checkerboard_type in ["Bernstein", "BernsteinCopula"]:
            from copul.checkerboard.bernstein import BernsteinCopula

            return BernsteinCopula(cmatr, check_theta=False)
        else:
            raise ValueError(f"Unknown checkerboard type: {self._checkerboard_type}")

    def from_data(self, data: Union[pd.DataFrame, np.ndarray, list]):  # noqa: E501
        # Normalize input to DataFrame
        if isinstance(data, (list, np.ndarray)):
            data = pd.DataFrame(data)

        n_obs = len(data)

        # Rank -> pseudo-observations in (0,1]; one column at a time for speed (numba)
        rank_data = np.empty_like(data.values, dtype=float)
        for i, col in enumerate(data.columns):
            rank_data[:, i] = _fast_rank(data[col].values)

        # Use existing fast path for 2D
        if self.d == 2:
            rank_df = pd.DataFrame(rank_data, columns=data.columns)
            return self._from_data_bivariate(rank_df, n_obs)

        # General d-dimensional case (d > 2): histogram on the unit cube
        # Guard against any tiny floating overshoots by nudging 1.0 to the next lower float.
        right_inclusive = np.nextafter(1.0, 0.0)
        rank_data = np.clip(rank_data, 0.0, right_inclusive)

        # Build d-D histogram with per-dimension bins self.n and range [0,1] in each dim
        hist, _ = np.histogramdd(rank_data, bins=self.n, range=[(0.0, 1.0)] * self.d)

        # Convert counts to probabilities
        cmatr = hist / n_obs

        return self._get_checkerboard_copula_for(cmatr)

    def _from_data_bivariate(self, data, n_obs):
        x = data.iloc[:, 0].values
        y = data.iloc[:, 1].values
        hist, _, _ = np.histogram2d(
            x, y, bins=[self.n[0], self.n[1]], range=[[0, 1], [0, 1]]
        )
        cmatr = hist / n_obs
        return self._get_checkerboard_copula_for(cmatr)


@njit
def _fast_rank(x):
    n = len(x)
    ranks = np.empty(n, dtype=np.float64)
    idx = np.argsort(x)
    for i in range(n):
        ranks[idx[i]] = (i + 1) / n
    return ranks


def from_data(data, checkerboard_size=None, checkerboard_type="CheckPi"):  # noqa: E501
    if checkerboard_size is None:
        n_samples = len(data)
        checkerboard_size = min(max(10, int(np.sqrt(n_samples) / 5)), 50)
    if isinstance(data, (list, np.ndarray)):
        data = pd.DataFrame(data)
    dimensions = data.shape[1]
    cb = Checkerboarder(
        n=checkerboard_size, dim=dimensions, checkerboard_type=checkerboard_type
    )
    return cb.from_data(data)


def from_samples(samples, checkerboard_size=None, checkerboard_type="CheckPi"):  # noqa: E501
    return from_data(samples, checkerboard_size, checkerboard_type)


def from_matrix(matrix, checkerboard_size=None, checkerboard_type="CheckPi"):  # noqa: E501
    return from_data(matrix, checkerboard_size, checkerboard_type)
