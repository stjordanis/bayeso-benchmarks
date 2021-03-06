import numpy as np
import pytest

from benchmarks.two_dim_beale import *

class_fun = Beale

TEST_EPSILON = 1e-3


def test_init():
    obj_fun = class_fun()

def test_validate_properties():
    obj_fun = class_fun()
    obj_fun.validate_properties()

def test_output():
    obj_fun = class_fun()
    bounds = obj_fun.get_bounds()

    grids = obj_fun.get_grids(3)
    truths_grids = np.array([
        [1.81853613e+05],
        [1.42031250e+01],
        [1.78131832e+05],
        [1.32328125e+02],
        [1.42031250e+01],
        [1.75781250e+01],
        [1.69680832e+05],
        [1.42031250e+01],
        [1.74813363e+05],
    ])
    
    print(grids)
    print(obj_fun.output(grids))
    print(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)
    assert np.all(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)

