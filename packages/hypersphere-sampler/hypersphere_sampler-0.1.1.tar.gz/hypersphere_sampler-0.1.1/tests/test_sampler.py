import numpy as np
from hypersphere_sampler import HypersphereSampler


def test_sampler_runs():
    sampler = HypersphereSampler(6, centers=[1,2,3,4,5,6], limits=[[0,4],[0,4],[2.5,6],[1,4.01],[5,6],[0,7]])
    data = sampler.sample(1000)
    assert isinstance(data, np.ndarray)
    assert data.shape[0] == N

    
