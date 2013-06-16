'''A short script for factoring integers that illustrates:

Function definition
Recustion
Looping
Command line arguments
Modules

From a command line try:
->python factor.py test
->python factor.py 255
->ipython
In [1]: import factor
In [2]: factor.factor(42)

'''
def factor(n):
    if n == 1:
        return []
    for i in range(2,n/2+2):
        if n%i == 0:
            return [i] + factor(n/i)
    return [n]
if __name__ == "__main__":
    import sys
    if sys.argv[1] == 'test':
        for n in (1,2,3,4,5,12,16,25,29,27,35):
            print('prime factors of %d are %s'%(n,factor(n)))
    else:
        n = int(sys.argv[1])
        print('prime factors of %d are %s'%(n,factor(n)))
