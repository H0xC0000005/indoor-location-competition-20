import numpy as np
from main import _glimpse_dict

a1 = np.array([1, 2, 3, 0])
a2 = np.array(["1", "2", "3", ])
a3 = np.array([True, False, True, ])

dt = {1: a1, 2: {"a": a2, "b": a3}}

_glimpse_dict(dt, "dt")
