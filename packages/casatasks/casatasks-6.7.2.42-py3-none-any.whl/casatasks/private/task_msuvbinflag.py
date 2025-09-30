
from casatasks.private.imagerhelpers.input_parameters import saveparams2last
from casatasks.private.imagerhelpers.msuvbinflag_algorithms import UVGridFlag

from casatasks import casalog
import time

@saveparams2last(multibackup=True)
def msuvbinflag(
        binnedvis, # input binned vis name (output of msuvbin)
        method, #= 'radial_mean_annular', 'radial_per_plane'
        nsigma, #=5
        doplot=False) -> None:

    flagger=UVGridFlag(binnedvis, doplot)
    if method == 'radial_mean_annular':
        tic = time.time()
        flagger.flagViaBin_radial(sigma=nsigma)
        toc = time.time()
        casalog.post("msuvbinflag running time : %.2f " % (toc - tic),
                     'DEBUG',
                     'task_msuvbinflag')

    elif method == 'radial_per_plane':
        tic = time.time()
        flagger.flag_radial_per_plane(sigma=nsigma)
        toc = time.time()

        casalog.post("msuvbinflag running time : %.2f " % (toc - tic),
                     'DEBUG',
                     'task_msuvbinflag')
    else:
        print("At this time only 'radial_mean_annular' and 'radial_per_plane' are supported")

    return

    #elif method == 'regionalMean':
    #    print("No bueno")
    #    #tic = time.time()
    #    #flagViaBin_regionalMean(binnedvis=binnedvis, sizeRegion=20, sigma=5,ignorPoint=True)
    #    #toc = time.time()
    #    #print("MSuvbinflag other method Running time:", toc - tic)
    #elif method == 'gradient':
    #    print("No bueno")
    #    #tic = time.time()
    #    #flagViaBin_gradient(binnedvis=binnedvis,  radius=1, sigma=0.3)
    #    #toc = time.time()
    #    #print("MSuvbinflag pead method Running time:", toc - tic)
    #elif method == 'median':
    #    print("No bueno")
    #    #tic = time.time()
    #    #flagViaBin_median(binnedvis=binnedvis,  sigma=5)
    #    #toc = time.time()
    #    #print("MSuvbinflag median method Running time:", toc - tic)
    #else:
    #    print("No bueno")
