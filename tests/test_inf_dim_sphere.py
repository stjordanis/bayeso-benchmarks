import numpy as np
import pytest

from benchmarks.inf_dim_sphere import *

class_fun = Sphere

TEST_EPSILON = 1e-5


def test_init():
    obj_fun = class_fun(2)

    with pytest.raises(TypeError) as error:
        class_fun()
    with pytest.raises(AssertionError) as error:
        class_fun('abc')
    with pytest.raises(AssertionError) as error:
        class_fun(2.1)

def test_validate_properties():
    obj_fun = class_fun(5)
    obj_fun.validate_properties()

def test_output():
    obj_fun = class_fun(3)
    bounds = obj_fun.get_bounds()

    grids = obj_fun.get_grids(3)
    truths_grids = np.array([
        [78.6432],
        [52.4288],
        [78.6432],
        [52.4288],
        [26.2144],
        [52.4288],
        [78.6432],
        [52.4288],
        [78.6432],
        [52.4288],
        [26.2144],
        [52.4288],
        [26.2144],
        [0.],
        [26.2144],
        [52.4288],
        [26.2144],
        [52.4288],
        [78.6432],
        [52.4288],
        [78.6432],
        [52.4288],
        [26.2144],
        [52.4288],
        [78.6432],
        [52.4288],
        [78.6432],
    ])
    
    print(grids)
    print(obj_fun.output(grids))
    print(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)
    assert np.all(np.abs(obj_fun.output(grids) - truths_grids) < TEST_EPSILON)

