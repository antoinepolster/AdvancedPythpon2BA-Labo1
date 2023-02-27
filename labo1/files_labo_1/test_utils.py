# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        utils.fact(5) ==120
        pass
    
    def test_roots(self):
        utils.roots(1,2,1)==-1
        pass
    
    def test_integrate(self):
        utils.integrate('x ** 2 - 1', -1, 1) == 2/3
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
