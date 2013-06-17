"""plot.py makes plots.  It imports stuff to do most of the
calculations.

"""
import sys
import matplotlib as mpl
import numpy as np
from numpy import random

DEBUG = False
plot_dict = {} # Keys are those keys in args.__dict__ that ask for
               # plots.  Values are the functions that make those
               # plots.
def main(argv=None):
    import argparse
    global DEBUG

    if argv is None:                    # Usual case
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Make plots')
    parser.add_argument('--N', type=int, default=5000,
                       help='Number of Henon points')
    parser.add_argument('--N_relax', type=int, default=100,
                       help='Discard N_relax iterations first')
    parser.add_argument('--dx', type=float, default=0.03,
                       help='Size of bins in x direction')
    parser.add_argument('--dy', type=float, default=0.01,
                       help='Size of bins in y direction')
    parser.add_argument('--dim_pars', type=float, nargs=2, default=[.2, 20],
                       help='log_step and n_steps for dimension plot')
    parser.add_argument('--debug', action='store_true')
    # Plot requests
    parser.add_argument('--dots', type=argparse.FileType('w'),
                       help='Put pdf plot of interations here')
    parser.add_argument('--colors', type=argparse.FileType('w'),
                       help='Color coded plot of counts in boxes')
    parser.add_argument('--dim', type=argparse.FileType('w'),
                       help='Dimension calculation plot')
    parser.add_argument('--count', type=argparse.FileType('w'),
                       help='Plot sorted log occupation')
    args = parser.parse_args(argv)
    
    params = {'axes.labelsize': 18,     # Plotting parameters for latex
              'text.fontsize': 15,
              'legend.fontsize': 15,
              'text.usetex': True,
              'font.family':'serif',
              'font.serif':'Computer Modern Roman',
              'xtick.labelsize': 15,
              'ytick.labelsize': 15}
    mpl.rcParams.update(params)
    if args.debug: # Enable display to screen
        DEBUG = True
        mpl.rcParams['text.usetex'] = False
    else:          # Write pdf plot files
        mpl.use('PDF')
    import matplotlib.pyplot as plt  # must be after mpl.use

    # Make requested plots
    for key in args.__dict__:
        if key not in plot_dict:
            continue
        if args.__dict__[key] == None:
            continue
        fig = plot_dict[key](plt, args)
        if not DEBUG:  # Write pdf plot files
            fig.savefig(args.__dict__[key], format='pdf')
    return 0

def dots(plt, args):
    '''Plot a little dot for each iteration of the map.
    '''
    import henon
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(1,1,1)
    xy = np.empty((2,args.N))
    i = -args.N_relax
    for _xy_ in henon.iterate((1,1),args.N_relax+args.N):
        if i >= 0:
            xy[:,i] = _xy_
        i += 1
    ax.plot(xy[0], xy[1],'b,')
    ax.set_ylim(-.5,.5)
    ax.set_yticks(np.arange(-.4, .41, .2),minor=False)
    ax.set_xticks(np.arange(-1.0, 1.1, 1.0),minor=False)
    return fig
plot_dict['dots'] = dots

def colors(plt, args):
    '''Use hennon.count to make bins in x,y and count the number of
    iterations that fall in each bin.  Then plot the bins as an image.
    '''
    import henon
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(1,1,1)
    c = henon.count_array(args.dx, args.dy, args.N)
    ax.imshow(c.T[::-1,:], interpolation='none', aspect='equal')
    return fig
plot_dict['colors'] = colors

def count(plt, args):
    '''Use hennon.count to make bins in x,y and count the number of
    iterations that fall in each bin.  Then plot the bins as an image.
    '''
    import henon
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(1,1,1)
    c = henon.count_array(args.dx, args.dy, args.N).reshape(-1)
    c.sort()
    c_ = []
    i_ = []
    for i in range(len(c)):
        j = len(c) - i - 1
        if c[j] < 1:
            break
        c_.append(np.log10(c[j]))
        i_.append(np.log(i+1))
    ax.plot(i_, c_)
    ax.set_ylabel(r'log$_{10}(N_i)$')
    ax.set_xlabel(r'log$_{10}(i+1)$')
    return fig
plot_dict['count'] = count

def dim(plt, args):
    '''Plot the log of the number of occupied boxes against the log of
    the box edge.
    '''
    import henon
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(1,1,1)
    log_step, n_steps = args.dim_pars
    log_d, log_n = henon.log_log(log_step, int(n_steps), args.N)
    ax.plot(log_d, log_n)
    ax.set_ylabel(r'log$_{10}(N)$')
    ax.set_xlabel(r'log$_{10}(\Delta_x)$')
    fig.subplots_adjust(bottom=0.15) # Make more space for label
    return fig
plot_dict['dim'] = dim

if __name__ == "__main__":
    rv = main()
    if DEBUG:
        import matplotlib.pyplot as plt
        plt.show()
    sys.exit(rv)

#---------------
# Local Variables:
# eval: (python-mode)
# End:
