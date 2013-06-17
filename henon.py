'''henon.py Code for studying the Henon system.  See
http://en.wikipedia.org/wiki/H%C3%A9non_map

Tools and ideas:

doctest http://docs.python.org/2/library/doctest.html

'''
import numpy as np
def map(z,       # A sequence of 2 numbers
        a=1.4,   # Parameter of the Henon system
        b=0.3    # Parameter of the Henon system
        ):
    ''' Apply the Henon map to z and return the result as a numpy
    array.  Example:
    
    >>> print(map((1,1)))
    [ 0.6  0.3]
    '''
    x,y = z
    return np.array([y+1-a*x**2, b*x])
def iterate(z, n, a=1.4, b=0.3):
    ''' Return a sequence of n x,y pairs.  Because this is implmented
    as an iterator.  It returns the sequential values as they are
    used, n may be larger than the memory of the computer.
    
    The following test passes on my system.  Since trajectories of the
    Henon system are unstable, ie, chaotic, the test will not pass on
    a system that does not implment floating point calculations
    exactly like mine.
    
    >>> L = list(iterate((1,1),20))
    >>> print('%7.3f %7.3f'%L[-1])
     -0.553   0.302
    '''
    for i in xrange(n):
        x,y = z
        z = y+1-a*x**2, b*x
        yield z

def bins(z, dx, dy, n, a=1.4, b=0.3):
    import math
    for i in xrange(n):
        x,y = z
        z = y+1-a*x**2, b*x
        math.ceil(z[0]/dx)
        yield int(math.ceil(z[0]/dx)), int(math.ceil(z[1]/dy))

def count_array(dx, dy, n, count_type=np.int):
    '''Make bins in x,y and count the number of iterations that fall
    in each bin
    '''
    import math
    x_range = (-1.5, 1.5)
    y_range = (-0.5, 0.5)
    INT = lambda z, dz: int(math.ceil(z/dz))
    ranges = np.array(list((INT(z_min,dz), INT(z_max,dz)) for z_min,z_max,dz
        in ((x_range + (dx,)), (y_range + (dy,)))))
    offset = ranges[:,0]             # Mins
    shape = ranges[:,1] - offset + 1 # Maxs - Mins + 1
    count = np.zeros(shape, count_type)
    for z in iterate((1,1), 100): pass # Relax to attractor
    for xy in bins(z, dx, dy, n):
        x,y = np.array(xy) - offset
        count[x,y] += 1
    return count

def log_log(log_step, n_steps, n_samples):
    '''Calculate and return two 1-d arrays:
    log_d    The log of the box size (both dx and dy)
    log_n    The log of the number of occupied boxes
    '''
    log_d = np.arange(0, -n_steps*log_step, -log_step)
    log_n = np.empty(n_steps)
    assert log_n.shape == log_d.shape
    for i in xrange(n_steps):
        d = 10**log_d[i]
        c = count_array(d, d, n_samples, np.bool)
        log_n[i] = np.log10(c.sum())
    return log_d, log_n

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
