"""plot.py makes plots.  It imports stuff to do most of the
calculations.

"""
import sys
import matplotlib as mpl
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

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
    parser.add_argument('--debug', action='store_true')
    # Plot requests
    parser.add_argument('--dots', type=argparse.FileType('w'),
                       help='Write figure to this file')
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
    if args.debug:
        DEBUG = True
        mpl.rcParams['text.usetex'] = False
    else:
        mpl.use('PDF')
    import matplotlib.pyplot as plt  # must be after mpl.use

    # Make requested plots
    for key in args.__dict__:
        if key not in plot_dict:
            continue
        if args.__dict__[key] == None:
            continue
        print('work on %s'%(key,))
        fig = plot_dict[key](plt, args)
        if not DEBUG:
            fig.savefig(args.__dict__[key], format='pdf')
    return 0

def dots(plt, args):
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
