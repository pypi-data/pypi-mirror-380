import numpy as np
import itertools


class HypersphereSampler:
    """
    Hypersphere / Hyperellipsoid sampler.

    Authors: Andreas Nygaard and Thomas Tram (2024)
    """

    def __init__(self, d, sample_surface=False, centers=None, limits=None, covmat=None, buffer_size=100000, seed=None):
        """
        d: Dimensionality of the parameter space
        sample_surface: If True, sample on the surface of the hypersphere.
                        If False, sample inside the hypersphere.
        centers: Centers for the ellipsoid transformation. Must be provided with limits or covmat.
        limits: (d,2) array of parameter limits defining the bounding box. Must contain centers if provided.
        covmat: Covariance matrix for the ellipsoid transformation or 1D array of stddevs.
        buffer_size: Number of points to sample in each iteration.
        seed: Random seed for reproducibility.
        """
        self.d = d
        self.surface = sample_surface
        self.buffer_size = buffer_size

        if centers is not None and limits is None and covmat is None:
            raise ValueError("If centers are provided, limits or covmat must also be provided.")

        if limits is not None:
            limits = np.float64(limits)
            assert limits.shape == (d, 2), "Limits must be of shape (d, 2)"
            # if centers is also provided, check that the centers are within limits
            if centers is not None:
                centers = np.float64(centers)
                assert np.all(centers >= limits[:, 0]) and np.all(centers <= limits[:, 1]), "Centers must be within limits"
        else:
            if covmat is not None and centers is not None:
                covmat = np.float64(covmat)
                if covmat.shape == (d,):
                    stddevs = covmat
                    limits = np.array([centers - 3. * stddevs, centers + 3. * stddevs]).T
                elif covmat.shape == (d, d):
                    stddevs = np.sqrt(np.diag(covmat))
                    limits = np.array([centers - 3. * stddevs, centers + 3. * stddevs]).T
            elif covmat is not None and centers is None:
                covmat = np.float64(covmat)
                if covmat.shape == (d,):
                    stddevs = covmat
                    limits = np.array([-3. * stddevs, 3. * stddevs]).T
                elif covmat.shape == (d, d):
                    stddevs = np.sqrt(np.diag(covmat))
                    limits = np.array([-3. * stddevs, 3. * stddevs]).T
            else:
                limits = np.array([[-1.0, 1.0]] * d)

        if centers is not None:
            assert len(centers) == d, "Length of centers must match dimensionality d"
            centers = np.float64(centers)
        elif limits is not None:
            centers = 0.5 * (limits[:, 0] + limits[:, 1])
        else:
            centers = np.zeros(d)


        # RNG
        if seed is None:
            self.rng = np.random.default_rng()
        else:
            self.rng = np.random.default_rng(seed=seed)

        # Covariance matrix (for ellipsoid transformation)
        if covmat is not None:
            cov = np.float64(covmat)
            if cov.shape == (d,):
                cov = np.diag(cov**2)
            self.L = np.linalg.cholesky(cov)
        else:
            self.L = None
        
        # Bounds and bounding box
        self.bounds = np.insert(limits, 1, centers, axis=1)
        self.bbox = np.empty((self.bounds.shape[0], 2))
        self.bbox[:, 0] = self.bounds[:, 0] - self.bounds[:, 1]
        self.bbox[:, 1] = self.bounds[:, 2] - self.bounds[:, 1]

    def points_in_bbox(self, A, B):
        """Filter points inside bounding box."""
        assert A.shape[0] == B.shape[0], "Dimensions of A and B must match"
        mask = np.all((A.T >= B[:, 0]) & (A.T <= B[:, 1]), axis=1)
        return A[:, mask]

    def gaussian_hypersphere(self, M):
        """Sample points on (or inside) a hypersphere."""
        samples = self.rng.normal(loc=0.0, scale=1.0, size=M * self.d).reshape(
            (self.d, M)
        )
        radii = np.sqrt(np.sum(samples * samples, axis=0))
        samples = samples / radii

        if self.surface:
            return samples
        new_radii = self.rng.uniform(low=0.0, high=1.0, size=M) ** (1.0 / self.d)
        return samples * new_radii

    def get_transformed_hypersphere_vector_with_bbox(self):
        """Yield transformed vectors inside bounding box."""
        while True:
            buffer = self.gaussian_hypersphere(self.buffer_size)
            if self.L is not None:
                buffer = self.L @ buffer
            else:
                scale = np.max([self.bbox], axis=2).T
                buffer *= scale
            selected_points = self.points_in_bbox(buffer, self.bbox).T
            for c in selected_points:
                yield c

    def sample(self, N):
        """Run the sampler and return N samples."""
        data = np.array(
            list(
                itertools.islice(
                    self.get_transformed_hypersphere_vector_with_bbox(), N
                )
            )
        )
        data += self.bounds[:, 1]
        return data
