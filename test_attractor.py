from attractor import Attractor
from nose import with_setup
import numpy as np

###
# Test Suite for specified Attractor interface
#
# Run with the command: "nosetests attractor.py"
###

def test_dt():
    """ Our first test will be to ensure that our time increment, dt, is being properly calculated.
    If this test fails we will be warned that there was a calculation error."""
    a = Attractor()
    assert a.end == a.dt * a.points, "\n There was a problem calculating the time increment! \n"
    
def test_euler():
    """ This test case is to ensure proper size of the value returned by our euler method.
    If this test fails it will indicate that there aren't the correct number of items being passed
    to the method."""
    a = Attractor()
    xyz = np.array([0.0,0.0,0.0])
    assert a.euler(xyz).shape == (3, ), "\n The array given to the euler method did not contain 3 items!\n"
    
def test_evolve():
    """ This test case is to ensure proper number of parameters are being passed to the evolve method. As
    above, this test also check for proper passing of paramters."""
    a = Attractor()
    assert a.evolve().shape == (a.points, 4), "\n The array given to the evolve method was improper!\n"