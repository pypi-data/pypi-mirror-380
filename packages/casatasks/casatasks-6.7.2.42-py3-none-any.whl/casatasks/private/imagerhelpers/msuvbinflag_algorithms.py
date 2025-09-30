import os
import numpy as np

# import numba as nb
import casatools
import time
from scipy.optimize import curve_fit
from typing import Tuple, List, Union, Optional

from casatasks import casalog

import matplotlib.pyplot as pl

ms = casatools.ms()
tb = casatools.table()
me = casatools.measures()
qa = casatools.quanta()
ia = casatools.image()
im = casatools.imager()


class UVGridFlag:
    def __init__(self, binnedvis: str, doplot: bool = False) -> None:
        self.binnedvis = binnedvis
        self.doplot = doplot
        ## parameter when debugging to test algorithm but not change grid.
        self.dryrun = False
        if self.doplot:
            pl.ion()

    # @nb.njit(cache=True)
    def populate_grid(
        self,
        uvw: np.array,
        stokesI: np.array,
        uvgrid: np.array,
        uvgrid_npt: np.array,
        deltau: float,
        deltav: float,
        npix: int,
    ):
        for ii in range(len(uvw[0])):
            uidx = int(np.round(uvw[0][ii] // deltau + npix // 2))
            vidx = int(np.round(uvw[1][ii] // deltav + npix // 2))

            uvgrid[uidx, vidx] += stokesI[ii]
            uvgrid_npt[uidx, vidx] += 1

        return uvgrid, uvgrid_npt

    def mad(self, inpdat: np.array) -> float:
        """
        Calculate the STD via MAD for the input data

        Inputs:
        inpdat      Input numpy array

        Returns:
        std         Calculate the std via mad
        """

        med = np.median(inpdat)
        mad = np.median(np.abs(inpdat - med))

        # 1.4826 is the scaling factor for a normal distribution
        # to convert MAD to STD
        return 1.4826 * mad

    def msuvbin_to_uvgrid(
        self, ms: str, npix: int, deltau: float, deltav: float
    ) -> Tuple[np.array, np.array]:
        tb.open(ms)
        uvw = tb.getcol("UVW")
        data = tb.getcol("DATA")
        tb.close()

        umin, umax = np.min(uvw[0]), np.max(uvw[0])
        vmin, vmax = np.min(uvw[1]), np.max(uvw[1])
        wmin, wmax = np.min(uvw[2]), np.max(uvw[2])

        uvals = np.linspace(umin, umax, npix)
        vvals = np.linspace(vmin, vmax, npix)

        uvgrid = np.zeros((npix, npix), dtype=np.complex128)
        uvgrid_npt = np.zeros((npix, npix), dtype=int)

        stokesI = 0.5 * (data[0] + data[1])
        stokesI = np.squeeze(stokesI)

        uvgrid, uvgrid_npt = self.populate_grid(
            uvw, stokesI, uvgrid, uvgrid_npt, deltau, deltav, npix
        )
        # Average per uv cell
        idx = np.where(uvgrid_npt != 0)
        uvgrid[idx] = uvgrid[idx] / uvgrid_npt[idx]

        return uvgrid, uvgrid_npt

    def resid_cube(
        self, x: float, a: float, b: float, c: float, d: float
    ) -> float:
        return a * x**3 + b * x**2 + c * x + d

    def resid_cinco(
        self,
        x: np.ndarray,
        a: float,
        b: float,
        c: float,
        d: float,
        e: float,
        f: float,
    ) -> np.ndarray:
        return a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f

    def fit_radial_profile(
        self,
        xvals: np.ndarray,
        yvals: np.ndarray,
        ystd: np.ndarray,
        deg: int = 3,
        clip_sigma: float = 3,
    ) -> np.ndarray:
        """
        Fit the radial profile with a polynomial
        """

        # print(f"deg {deg}, clip_sigma {clip_sigma}")
        # print(f"xvals shape {xvals.shape}, yvals shape {yvals.shape}")
        # print(f"non-zero x {np.count_nonzero(xvals)}, non-zero y {np.count_nonzero(yvals)}")

        idx = np.where(yvals != 0)
        xvals = xvals[idx]
        yvals = yvals[idx]
        ystd = ystd[idx]

        # print(f"xvals {xvals}, yvals {yvals}")

        # Fit the radial profile with a polynomial
        # pfit, pcov = curve_fit(resid_function, xvals, yvals, sigma=ystd, p0=[1, 1, 1, 1])

        pfit = np.polyfit(xvals, yvals, deg=2)
        yfit = np.polyval(pfit, np.linspace(xvals.min(), xvals.max(), 100))

        has_converged = False
        while not has_converged:
            # Outlier rejection while fitting
            resid = yvals - np.polyval(pfit, xvals)
            resid_mad = self.mad(resid)
            resid_med = np.median(resid)
            idx = np.where(
                (resid > resid_med - clip_sigma * resid_mad)
                & (resid < resid_med + clip_sigma * resid_mad)
            )

            if len(idx[0]) == len(xvals):
                has_converged = True
                continue

            xvals = xvals[idx]
            yvals = yvals[idx]
            ystd = ystd[idx]

            # pfit = np.polyfit(xvals, yvals, deg=deg)

            pfit, pcov = curve_fit(
                self.resid_cube, xvals, yvals, sigma=ystd, p0=[1, 1, 1, 1]
            )
            yfit = np.polyval(pfit, np.linspace(xvals.min(), xvals.max(), 100))

        # import matplotlib.pyplot as plt

        # fig, ax = plt.subplots()
        # ax.plot(xvals, yvals, '-o', label='Data')
        # ax.plot(np.linspace(xvals.min(), xvals.max(), 100), yfit, '--', label='Fit')
        # ax.set_xlabel('Radius')
        # ax.set_ylabel('Intensity')
        # ax.legend()
        # plt.tight_layout()
        # plt.show()

        return pfit

    def calc_radial_profile_ann(
        self, uvgrid: np.ndarray, uvlen_m: np.ndarray
    ) -> Tuple[np.array, np.array, np.array]:
        """
        Calculate the annular average of the uvgrid for every radius,
        and fit the 1D radial profile with a polynomial.
        """

        nbin = 30

        npixx, npixy = uvgrid.shape[0], uvgrid.shape[1]
        cx, cy = npixx // 2, npixy // 2

        uvlen_m_grid = uvlen_m.reshape([npixx, npixy])

        # Generate grid of radii
        x = np.arange(npixx) - cx
        y = np.arange(npixy) - cy
        # rad = np.sqrt(x**2 + y**2).astype(int)

        yy, xx = np.meshgrid(x, y)
        # radgrid = np.sqrt(xx**2 + yy**2).astype(int)

        # Create log-spaced annuli to account for reducing UV coverage with radius
        # Minimum annulus is 5px
        annuli = np.logspace(0, np.log10(uvlen_m_grid.max()), nbin)
        annuli = np.round(annuli).astype(int)

        radial_mean = np.zeros(nbin)
        radial_mad = np.zeros(nbin)

        ann_min = 0
        for idx, ann in enumerate(annuli):
            ridx = np.where((uvlen_m_grid >= ann_min) & (uvlen_m_grid < ann))
            uvgrid_sel = uvgrid[ridx]
            uvgrid_sel = uvgrid_sel[np.abs(uvgrid_sel) != 0]

            if len(uvgrid_sel) == 0:
                radial_mean[idx] = 0
                radial_mad[idx] = 0.0
            else:
                radial_mean[idx] = np.mean(np.abs(uvgrid_sel))
                radial_mad[idx] = self.mad(np.abs(uvgrid_sel))

            ann_min = ann

        return radial_mean, radial_mad, annuli

    def calc_radial_profile_pix(
        self, uvgrid: np.ndarray, deltau: float, deltav: float
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Calculate the radial per-pixel average of the uvgrid for every radius,
        and fit the 1D radial profile with a polynomial.
        """

        npixx, npixy = uvgrid.shape[0], uvgrid.shape[1]
        cx, cy = npixx // 2, npixy // 2

        # Generate radial values from 0 to max
        x = np.arange(cx)
        y = np.arange(cy)
        rad = np.sqrt(x**2 + y**2).astype(int)

        # Generate grid of radii
        x = np.arange(npixx) - cx
        y = np.arange(npixy) - cy
        yy, xx = np.meshgrid(x, y)
        radgrid = np.sqrt(xx**2 + yy**2).astype(int)

        radial_mean = np.zeros(np.max([cx, cy]))
        radial_mad = np.zeros(np.max([cx, cy]))

        for idx, rr in enumerate(rad):
            if idx == len(rad) - 1:
                ridx = np.where((radgrid >= rad[idx]))
            else:
                ridx = np.where(
                    (radgrid > rad[idx]) & (radgrid <= rad[idx + 1])
                )

            uvgrid_sel = uvgrid[ridx]
            uvgrid_sel = uvgrid_sel[np.abs(uvgrid_sel) != 0]

            if len(uvgrid_sel) == 0:
                radial_mean[idx] = 0
                radial_mad[idx] = 0.0
            else:
                radial_mean[idx] = np.mean(uvgrid_sel)
                radial_mad[idx] = self.mad(uvgrid_sel)

        return uvgrid, radial_mean, radial_mad, rad * deltau

    #############################################################3
    def calc_radial_profile_and_fit(
        self,
        uvgrid: np.ndarray,
        wgtgrid: np.ndarray,
        flggrid: np.ndarray,
        nsigma: float,
    ) -> None:
        """
        Does a weighted radial mean profile and fit it and determines flag for point that is nsigma
        above fitted radial profile.
        flggrid gets modifies
        Right now the wgtgrid and uvgrid are zeroed at the flagged cells...but this is not necessary
        """
        npixx, npixy = uvgrid.shape[0], uvgrid.shape[1]
        cx, cy = npixx // 2, npixy // 2
        # print(f"npixx {npixx}, npixy {npixy}, centerx {cx} centery {cy}")

        # Generate radial values from 0 to max
        x = np.arange(cx)
        y = np.arange(cy)
        rad = np.sqrt(x**2 + y**2).astype(int)
        npoints = int(np.max(rad)) + 1
        radamp = np.zeros(npoints)
        radamp2 = np.zeros(npoints)
        radwght = np.zeros(npoints)
        xval = np.array(range(npoints), dtype="float")
        for j in range(1, npixy):
            yval2 = (j - cy) * (j - cy)
            for k in range(1, npixx):
                rval = int(np.sqrt((k - cx) * (k - cx) + yval2))
                if wgtgrid[k, j] > 0.0:
                    absval = np.abs(uvgrid[k, j])
                    radamp[rval] += absval * wgtgrid[k, j]
                    radamp2[rval] += absval * absval * wgtgrid[k, j]
                    radwght[rval] += wgtgrid[k, j]
        if np.max(radwght) == 0.0:
            # empty channel
            return
        radamp[radwght != 0] = radamp[radwght != 0] / radwght[radwght != 0]
        radamp2[radwght != 0] = radamp2[radwght != 0] / radwght[radwght != 0]
        maxsenspos = np.argmax(radwght)
        # normalize radweight
        # normrdwght=radwght/np.max(radwght)
        sig = np.sqrt(np.abs(radamp2 - radamp * radamp))
        # nescale relative sigmas by number of weights att the point
        # medsig=np.median(sig[sig !=0])
        sigtouse = sig[maxsenspos]
        # sig[normrdwght!=0]=sig[normrdwght!=0]/normrdwght[normrdwght!=0]
        xvalnz = xval[(sig != 0.0) & (radamp != 0)]
        radampnz = radamp[(sig != 0) & (radamp != 0)]
        try:
            fitnz = curve_fit(self.resid_cinco, xvalnz, radampnz)
        except:
            # print("failed to curve_fit")
            return
        ###
        # print('min max of sig and max sens one', np.min(sig), np.max(sig), sigtouse)
        signz = sig[sig != 0.0]
        sig = np.interp(xval, xvalnz, signz)
        # print( 'corvar ', fitnz[1])
        radfit = self.resid_cinco(xval, *fitnz[0])
        # radamp=np.ma.array(radamp, mask=(radwght == 0))
        # radfit=np.ma.array(radfit, mask=(radwght == 0))
        max_rad_idx = np.where(xval == np.max(xvalnz))[0][0]
        if self.doplot:
            # pl.figure()
            ax1 = pl.subplot(211)

            # pl.plot(xval, radfit+sig,'+')
            ax1.errorbar(
                xval[0:max_rad_idx],
                radfit[0:max_rad_idx],
                yerr=sig[0:max_rad_idx],
                ecolor="lime",
                fmt="none",
                label="sigma",
            )
            ax1.plot(
                xval[0:max_rad_idx],
                radamp[0:max_rad_idx],
                "o",
                color="magenta",
                label="mean radial value",
            )
            ax1.plot(
                xval[0:max_rad_idx],
                radfit[0:max_rad_idx],
                "k",
                label="fitted radial value",
            )
            ax1.set_ylabel("Amplitude")
            ax1.set_xlabel("uvdist in pix")
            ax1.legend()
        if self.doplot:
            ax2 = pl.subplot(212)
        for j in range(npixy):
            for k in range(npixx):
                # sweep over all points
                # if points are not already flagged
                yval2 = (j - cy) * (j - cy)
                if not flggrid[k, j]:
                    r = int(np.sqrt(yval2 + (k - cx) * (k - cx)))
                    # if(r < npoints and np.abs(uvgrid[k,j]) > (radfit[r]+nsigma*max(medsig, sig[r]))):
                    if r < npoints and (
                        np.abs(uvgrid[k, j]) > (radfit[r] + nsigma * sigtouse)
                    ):
                        if self.doplot:
                            ax2.plot(r, np.abs(uvgrid[k, j]), "go")
                        uvgrid[k, j] = 0
                        wgtgrid[k, j] = 0
                        flggrid[k, j] = True
                    else:
                        if self.doplot:
                            ax2.plot(r, np.abs(uvgrid[k, j]), "b+")

    ######################################################################################################
    # Bonus joke : The Dalai Lama walks into a pizza shop and says "Can you make me one with everything?"
    #              The cashier hands him the pizza and says "That'll be $12.50." The Dalai Lama hands him a
    #              $20 bill and waits. After a few moments, he asks "Where's my change?" The cashier replies
    #              "Change comes from within."

    # This needs to be a static method, otherwise numba cannot compile it because it does not understand self
    @staticmethod
    # @nb.njit(cache=True)
    def apply_flags(
        dat: np.ndarray,
        flg: np.ndarray,
        uvlen: np.ndarray,
        radial_mean: np.ndarray,
        radial_mad: np.ndarray,
        annuli: np.ndarray,
        nsigma: float = 5.0,
    ) -> np.ndarray:
        """
        Apply flags based on the radial profile to the input data column
        """

        nrow = uvlen.shape[0]

        for rr in range(nrow):

            # feature of searchsorted will return N if above max(annuli)
            annidx = annuli.size - 1
            if uvlen[rr] < annuli[-1]:
                annidx = np.searchsorted(annuli, uvlen[rr])
            if (
                np.abs(dat[..., rr])
                > radial_mean[annidx] + nsigma * radial_mad[annidx]
            ):
                flg[..., rr] = True

        return flg

    ###########################################################################################
    def accumulate_continuum_grid(
        self,
        tb: casatools.table,
        npol: int,
        nchan: int,
        npoints: int,
        deltau: float,
        deltav: float,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        If the input msuvbin has multiple channels, loop over them to
        accumulate on a single grid. This allows for a better estimate of the
        radial profile from a "fuller" UV grid before flagging outliers
        per-plane.

        Inputs:
        tb          Table object - must be open
        npol        Number of polarizations'
        nchan       Number of channels
        npoints     Number of points in the grid
        deltau      U spacing in lambda
        deltav      V spacing in lambda

        Returns:
        uvgrid      Accumulated UV grid
        uvnpt       Number of points per UV cell
        """

        uvgrid_cont = np.zeros((npoints, npoints), dtype=np.complex128)
        wgtgrid_cont = np.zeros((npoints, npoints), dtype=np.float64)

        for pol in range(npol):
            for chan in range(nchan):
                dat = tb.getcolslice("DATA", [pol, chan], [pol, chan], [1, 1])
                flg = tb.getcolslice("FLAG", [pol, chan], [pol, chan], [1, 1])
                wgt = tb.getcolslice(
                    "WEIGHT_SPECTRUM", [pol, chan], [pol, chan], [1, 1]
                )

                if dat.size == 0 or flg.size == 0 or wgt.size == 0:
                    casalog.post(
                        "Zero size array read. Skipping.",
                        "WARN",
                        "task_msuvbinflag",
                    )
                    continue

                dat_grid = dat[0, 0, :].reshape([npoints, npoints])
                flg_grid = flg[0, 0, :].reshape([npoints, npoints])
                wgt_grid = wgt[0, 0, :].reshape([npoints, npoints])

                # Flag the data as necessary
                dat_grid = dat_grid * ~flg_grid

                uvgrid_cont += dat_grid  # should not this respect the flagged data i.e not add the data which are flagged ?
                wgtgrid_cont += wgt_grid

        return uvgrid_cont, wgtgrid_cont

    ##########################################################
    def flagViaBin_radial(self, sigma: float = 5):

        tb.open(self.binnedvis, nomodify=False)
        msuvbinkey = tb.getkeyword("MSUVBIN")

        # msuvbinkey.keys()
        # Out[5]: dict_keys(['csys', 'nchan', 'npol', 'numvis', 'nx', 'ny', 'sumweight'])

        # in radian
        dra = msuvbinkey["csys"]["direction0"]["cdelt"][0]
        ddec = msuvbinkey["csys"]["direction0"]["cdelt"][1]

        nx = msuvbinkey["nx"]
        ny = msuvbinkey["ny"]

        # in radian
        ra_extent = dra * nx
        dec_extent = ddec * ny

        # in Lambda
        deltau = 1.0 / ra_extent
        deltav = 1.0 / dec_extent

        npol = msuvbinkey["npol"]
        nchan = msuvbinkey["nchan"]

        npoints = min(nx, ny)

        uvw = tb.getcol("UVW")
        uvlen_m = np.sqrt(uvw[0] ** 2 + uvw[1] ** 2)

        # Accumulate all channels in a single grid
        uvgrid_cont, wgtgrid_cont = self.accumulate_continuum_grid(
            tb, npol, nchan, npoints, deltau, deltav
        )
        # Calculate the radial profile
        radial_mean, radial_mad, annuli = self.calc_radial_profile_ann(
            uvgrid_cont, uvlen_m
        )
        # radial_fit = fit_radial_profile(annuli,  np.abs(radial_mean), radial_mad, deg=2)

        if self.doplot:
            import matplotlib.pyplot as plt
            from matplotlib.colors import LogNorm

            fig, ax = plt.subplots()
            ax.plot(annuli[2:], np.abs(radial_mean)[2:], "-o", label="data")
            # ax.plot(np.linspace(annuli.min(), annuli.max(), 100), np.polyval(radial_fit, np.linspace(annuli.min(), annuli.max(), 100)), label='fit')
            ax.fill_between(
                annuli,
                np.abs(radial_mean) - radial_mad,
                np.abs(radial_mean) + radial_mad,
                alpha=0.5,
            )
            ax.set_xlabel("Radius")
            ax.set_ylabel("Intensity (Jy)")
            ax.set_title("Radial Mean")
            # ax.set_yscale('symlog', linthresh=1e-9)
            ax.legend()
            plt.tight_layout()

            plt.savefig("radprof.jpg", bbox_inches="tight")

            fig, ax = plt.subplots(1, 1)
            uvgrid_shape = uvgrid_cont.shape
            ax.imshow(
                np.abs(uvgrid_cont),
                origin="lower",
                norm=LogNorm(vmin=1e-12, vmax=1),
                extent=[
                    -uvgrid_shape[0] // 2,
                    uvgrid_shape[0] // 2,
                    -uvgrid_shape[1] // 2,
                    uvgrid_shape[1] // 2,
                ],
            )
            ax.set_title("UV grid")
            plt.tight_layout()
            # plt.savefig('uvgrid.jpg', bbox_inches='tight')
            plt.show()

        for pol in range(npol):
            for chan in range(nchan):
                dat = np.asarray(
                    tb.getcolslice("DATA", [pol, chan], [pol, chan], [1, 1])
                )
                flg = np.asarray(
                    tb.getcolslice("FLAG", [pol, chan], [pol, chan], [1, 1])
                )
                wgt = np.asarray(
                    tb.getcolslice(
                        "WEIGHT_SPECTRUM", [pol, chan], [pol, chan], [1, 1]
                    )
                )

                if dat.size == 0 or flg.size == 0 or wgt.size == 0:
                    casalog.post(
                        "Zero size array read. Skipping.",
                        "WARN",
                        "task_msuvbinflag",
                    )
                    continue

                # Do the flagging and write back
                flg_new = self.apply_flags(
                    dat,
                    flg,
                    uvlen_m,
                    radial_mean,
                    radial_mad,
                    annuli,
                    nsigma=sigma,
                )

                tb.putcolslice("DATA", dat, [pol, chan], [pol, chan])
                tb.putcolslice("FLAG", flg_new, [pol, chan], [pol, chan])
                tb.putcolslice(
                    "WEIGHT_SPECTRUM", wgt, [pol, chan], [pol, chan]
                )

        tb.clearlocks()
        tb.close()
        tb.done()

    ###################################################################
    def flag_radial_per_plane(self, sigma=5) -> None:
        tb.open(self.binnedvis, nomodify=False)
        msuvbinkey = tb.getkeyword("MSUVBIN")
        nx = msuvbinkey["nx"]
        ny = msuvbinkey["ny"]
        if nx != ny:
            raise Exception("Do not deal with non square gridded vis")
        npol = msuvbinkey["npol"]
        nchan = msuvbinkey["nchan"]

        for c in range(nchan):
            dat = tb.getcolslice("DATA", [0, c], [npol - 1, c], [1, 1])
            flg = tb.getcolslice("FLAG", [0, c], [npol - 1, c], [1, 1])
            wgt = tb.getcolslice(
                "WEIGHT_SPECTRUM", [0, c], [npol - 1, c], [1, 1]
            )
            #########
            of = np.sum(flg[:, 0, :])
            casalog.post(
                "BEFORE chan %d number of unflagged points: %d max: %f"
                % (
                    c,
                    nx * nx * npol - of,
                    np.max(np.abs(dat[:, 0, :])),
                ),
                "DEBUG",
                "task_msuvbinflag",
            )
            # print (f'BEFORE chan {c} number of unflagged points:  {nx*nx*npol-of} max:  {np.max(np.abs(dat[:,0,:]))}')
            ########
            for k in range(npol):
                if self.doplot:
                    pl.clf()
                    ax1 = pl.subplot(211)
                    ax1.set_title(
                        f"radial mean Amp and fit for chan {c} and pol {k} "
                    )
                a = dat[k, 0, :].reshape([nx, nx])
                f = flg[k, 0, :].reshape([nx, nx])
                w = wgt[k, 0, :].reshape([nx, nx])
                self.calc_radial_profile_and_fit(a, w, f, sigma)
                if self.doplot:
                    # pl.show()
                    pl.savefig(f"rad_{self.binnedvis}_c{c}_p{k}.jpg")
                # input("Press Enter to continue...")
            #########
            of = np.sum(flg[:, 0, :])
            casalog.post(
                "AFTER chan %d number of unflagged points: %d max: %f"
                % (
                    c,
                    nx * nx * npol - of,
                    np.max(np.abs(dat[:, 0, :])),
                ),
                "DEBUG",
                "task_msuvbinflag",
            )
            # print (f'AFTER chan {c} number of unflagged points:  {nx*nx*npol-of} max:  {np.max(np.abs(dat[:,0,:]))}')
            # print ('=======================================================================')
            ########
            if not self.dryrun:
                tb.putcolslice("FLAG", flg, [0, c], [npol - 1, c], [1, 1])
                tb.putcolslice("DATA", dat, [0, c], [npol - 1, c], [1, 1])
                tb.putcolslice(
                    "WEIGHT_SPECTRUM", wgt, [0, c], [npol - 1, c], [1, 1]
                )

        tb.done()

    #########################################################################################
    def flag_gradient(self) -> None:
        # temporary till  pykrige is installed by default
        ###############################################
        import pdb
        import pip

        try:
            from pykrige.ok import OrdinaryKriging
        except:
            pip.main(["install", "pykrige"])
            from pykrige.ok import OrdinaryKriging
        ###############################################
        factor = 5.0
        tb.open(self.binnedvis, nomodify=False)
        msuvbinkey = tb.getkeyword("MSUVBIN")
        nx = msuvbinkey["nx"]
        ny = msuvbinkey["ny"]
        if nx != ny:
            raise Exception("Do not deal with non square gridded vis")
        npol = msuvbinkey["npol"]
        nchan = msuvbinkey["nchan"]
        # pdb.set_trace()
        for c in range(nchan):
            dat = tb.getcolslice("DATA", [0, c], [npol - 1, c], [1, 1])
            flg = tb.getcolslice("FLAG", [0, c], [npol - 1, c], [1, 1])
            wgt = tb.getcolslice(
                "WEIGHT_SPECTRUM", [0, c], [npol - 1, c], [1, 1]
            )
            #########
            of = np.sum(flg[:, 0, :])
            print(
                f"BEFORE chan {c} number of unflagged points:  {nx*nx*npol-of} max:  {np.max(np.abs(dat[:,0,:]))}"
            )
            ########
            for k in range(npol):
                a = dat[k, 0, :].reshape([nx, nx])
                f = flg[k, 0, :].reshape([nx, nx])
                w = wgt[k, 0, :].reshape([nx, nx])
                f[w == 0.0] = True

                if self.doplot:
                    pl.clf()
                    pl.ion()
                    af = np.ma.array(np.abs(a), mask=f)
                    med = np.ma.median(af)
                    rms = np.ma.std(af)
                    ax1 = pl.subplot(121)
                    pl.imshow(np.abs(a), vmin=med - rms, vmax=med + 4 * rms)
                    pl.title(f"BEFORE chan {c} and pol{k}")
                    # ax1.set_title(f'gradient stuff for chan {c} and pol {k} ')
                self.locateViaKrige(a, f, factor)
                if self.doplot:

                    print(f"chan{c}, pol{k}")

                    pl.subplot(122)
                    pl.imshow(np.abs(a), vmin=med - rms, vmax=med + 4 * rms)
                    pl.title("AFTER")
                    pl.show()
                    pl.savefig(f"rad_{self.binnedvis}_c{c}_p{k}.jpg")
                # input("Press Enter to continue...")
                time.sleep(10)
            #########
            of = np.sum(flg[:, 0, :])
            print(
                f"AFTER chan {c} number of unflagged points:  {nx*nx*npol-of} max:  {np.max(np.abs(dat[:,0,:]))}"
            )
            print(
                "======================================================================="
            )
            ########
            if not self.dryrun:
                tb.putcolslice("FLAG", flg, [0, c], [npol - 1, c], [1, 1])
            #    tb.putcolslice('DATA', dat, [0,c], [npol-1,c], [1,1])
            #    tb.putcolslice('WEIGHT_SPECTRUM', wgt, [0, c], [npol-1, c], [1, 1])

        tb.done()

    @staticmethod
    def locate_von(grid, radius=1, scale=0.3):

        flagpoints = []
        gridpoints = []
        npoints = len(grid)
        gradients = np.gradient(grid)
        du = gradients[0]
        dv = gradients[1]
        th = np.sqrt(
            np.ma.max(du) * np.ma.max(du) + np.ma.max(dv) * np.ma.max(dv)
        )
        print("Max grad", th, np.ma.max(du), np.ma.max(dv))
        scale = th * scale

        for i in range(int(radius), int(npoints - radius)):
            for j in range(int(radius), int(npoints - radius)):
                if grid.mask[i, j] == False:
                    du_up = du[i + radius][j]
                    du_down = du[i - radius][j]
                    dv_up = dv[i][j + radius]
                    dv_down = dv[i][j - radius]

                    if (
                        (np.abs(du_up) > scale)
                        or (np.abs(du_down) > scale)
                        or (np.abs(dv_up) > scale)
                        or (np.abs(dv_down) > scale)
                    ):
                        if (np.sign(du_up) == -1 * np.sign(du_down)) or (
                            np.sign(dv_up) == -1 * np.sign(dv_down)
                        ):
                            flagpoints.append(grid[i][j])
                            gridpoints.append((i, j))

        return flagpoints, gridpoints

    @staticmethod
    def locateViaKrige(grid: np.array, flag: np.array, factor=5):
        from pykrige.ok import OrdinaryKriging

        b = np.abs(grid[flag == False])
        ou = np.where(flag == False)
        print(f"number of uv points {len(ou[1])}")
        OK = OrdinaryKriging(
            ou[1], ou[0], b, variogram_model="linear", exact_values=False
        )
        gridpoints = np.array(np.arange(0, len(grid)), dtype=np.float64)
        z, ss = OK.execute("grid", gridpoints, gridpoints)
        diffmap = np.ma.array(np.abs(np.abs(grid) - z), mask=flag)
        med = np.ma.median(diffmap)
        for k in range(len(ou[1])):
            # difference with average around point
            # diff=(9*z[ou[0][k], ou[1][k]]-(np.sum(z[ou[0][k]-1:ou[0][k]+2, ou[1][k]-1:ou[1][k]+2])))/8.0
            diff = diffmap[ou[0][k], ou[1][k]]
            # frac=np.abs(diff)/grid[ou[0][k], ou[1][k]]
            if diff > factor * med:
                flag[ou[0][k], ou[1][k]] = True
                grid[ou[0][k], ou[1][k]] = 0.0
