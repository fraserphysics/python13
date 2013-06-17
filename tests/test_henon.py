# run from ../.. directory
# export PYTHONPATH=./
# python python13/tests/test_hennon.py
import numpy as np
from numpy.testing import assert_, run_module_suite
from python13 import henon

def test_count_array():
    C = henon.count_array(5, 5, 10)
    assert_(C.shape == (2,2))
    C = henon.count_array(.1, .1, 1000)
    assert_(C.shape == (31,11))
if __name__ == "__main__":
    run_module_suite()

#--------------------------------
# Local Variables:
# mode: python
# End:
