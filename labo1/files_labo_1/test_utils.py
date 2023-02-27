# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018
import unittest
import utils
import pytest
import math

def test_fact():
    assert utils.fact(0) == 1 
    assert utils.fact(4) == 24
    with pytest.raises(ValueError):
        utils.fact(-1)
    
def test_roots():
    assert isinstance(utils.roots(2, 0, 0), tuple)
    assert utils.roots(2, 0 ,0) == pytest.approx((0.0,))
    assert utils.roots(2, 0 ,-2) == pytest.approx((-1.0, 1.0))
    assert utils.roots(2, 1 ,-2) == pytest.approx((-1.2807640, 0.78077640))
    
def test_integrate():
    assert utils.integrate('x ** 2 - 1', -1, 1) == 2/3

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
