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

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
