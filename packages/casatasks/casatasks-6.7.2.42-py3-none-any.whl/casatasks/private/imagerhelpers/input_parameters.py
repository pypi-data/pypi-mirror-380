import os
import math
import shutil
import string
import time
import re
import copy
import pprint
import functools
import inspect
from collections import OrderedDict
import numpy as np
from typing import Tuple
import filecmp


from casatools import synthesisutils
from casatools import table, ms, synthesisutils, quanta
from casatools import calibrater
from casatasks import casalog
from casatasks.private.mslisthelper import check_mslist
from casatasks.private.mslisthelper import sort_mslist


"""
A set of helper functions for the tasks  tclean

Summary...
    
"""


######################################################
######################################################
######################################################


class ImagerParameters:
    def __init__(
        self,
        # Input Data: what gets in
        msname="",
        # Output Data: what goes out
        imagename="",
        # The remaining parameters are Control Parameters:
        # they control How what gets in goes out
        # Data Selection
        field="",
        spw="",
        timestr="",
        uvdist="",
        antenna="",
        scan="",
        obs="",
        state="",
        datacolumn="corrected",
        # Image Definition
        imsize=[1, 1],
        cell=[10.0, 10.0],
        phasecenter="",
        stokes="I",
        projection="SIN",
        startmodel="",
        # Spectral Parameters
        specmode="mfs",
        reffreq="",
        nchan=1,
        start="",
        width="",
        outframe="LSRK",
        veltype="radio",
        restfreq=[""],
        sysvel="",
        sysvelframe="",
        interpolation="nearest",
        perchanweightdensity=False,
        gridder="standard",
        # ftmachine='gridft',
        facets=1,
        chanchunks=1,
        wprojplanes=1,
        vptable="",
        usepointing=False,
        mosweight=False,
        aterm=True,
        psterm=True,
        mterm=True,
        wbawp=True,
        cfcache="",
        dopbcorr=True,
        conjbeams=True,
        computepastep=360.0,
        rotatepastep=360.0,
        pointingoffsetsigdev=[30.0, 30.0],
        # Normalizer group
        pblimit=0.01,
        normtype="flatnoise",
        psfcutoff=0.35,
        makesingledishnormalizer=False,
        outlierfile="",
        restart=True,
        weighting="natural",
        robust=0.5,
        noise="0.0Jy",
        npixels=0,
        uvtaper=[],
        niter=0,
        cycleniter=0,
        loopgain=0.1,
        threshold="0.0Jy",
        nsigma=0.0,
        cyclefactor=1.0,
        minpsffraction=0.1,
        maxpsffraction=0.8,
        interactive=False,
        fullsummary=False,
        nmajor=-1,
        deconvolver="hogbom",
        scales=[],
        nterms=1,
        scalebias=0.0,
        restoringbeam=[],
        # mtype='default',
        usemask="user",
        mask="",
        pbmask=0.0,
        maskthreshold="",
        maskresolution="",
        nmask=0,
        # autoadjust=False,
        sidelobethreshold=5.0,
        noisethreshold=3.0,
        lownoisethreshold=3.0,
        negativethreshold=0.0,
        smoothfactor=1.0,
        minbeamfrac=0.3,
        cutthreshold=0.01,
        growiterations=100,
        dogrowprune=True,
        minpercentchange=0.0,
        verbose=False,
        fastnoise=True,
        fusedthreshold=0.0,
        largestscale=-1,
        # usescratch=True,
        # readonly=True,
        calcres=True,
        calcpsf=True,
        savemodel="none",
        parallel=False,
        workdir="",
        # CFCache params
        cflist=[],
        # single-dish imaging params
        gridfunction="SF",
        convsupport=-1,
        truncate="-1",
        gwidth="-1",
        jwidth="-1",
        pointingcolumntouse="direction",
        convertfirst="never",
        minweight=0.0,
        clipminmax=False,
    ):

        self.allparameters = dict(locals())
        del self.allparameters["self"]

        self.defaultKey = "0"
        # ---- Selection params. For multiple MSs, all are lists.
        # For multiple nodes, the selection parameters are modified inside
        # PySynthesisImager
        self.allselpars = {
            "msname": msname,
            "field": field,
            "spw": spw,
            "scan": scan,
            "timestr": timestr,
            "uvdist": uvdist,
            "antenna": antenna,
            "obs": obs,
            "state": state,
            "datacolumn": datacolumn,
            "savemodel": savemodel,
        }
        # ---- Imaging/deconvolution parameters
        # The outermost dictionary index is image field.
        # The '0' or main field's parameters come from the task parameters
        # The outlier '1', '2', ....  parameters come from the outlier file
        self.outlierfile = outlierfile
        # Initialize the parameter lists with the 'main' or '0' field's
        # parameters
        # ---- Image definition
        self.allimpars = {
            self.defaultKey: {
                # Image
                "imagename": imagename,
                "nchan": nchan,
                "imsize": imsize,
                "cell": cell,
                "phasecenter": phasecenter,
                "stokes": stokes,
                # Frequency axis
                "specmode": specmode,
                "start": start,
                "width": width,
                "veltype": veltype,
                "nterms": nterms,
                "restfreq": restfreq,
                # Output frame
                "outframe": outframe,
                "reffreq": reffreq,
                "sysvel": sysvel,
                "sysvelframe": sysvelframe,
                # Projection
                "projection": projection,
                # Deconvolution
                "restart": restart,
                "startmodel": startmodel,
                "deconvolver": deconvolver,
            }
        }
        # ---- Gridding
        self.allgridpars = {
            self.defaultKey: {
                "gridder": gridder,
                # aterm group
                "aterm": aterm,
                "psterm": psterm,
                "mterm": mterm,
                "wbawp": wbawp,
                # cfcache group
                "cfcache": cfcache,
                "usepointing": usepointing,
                "dopbcorr": dopbcorr,
                # conjbeams group
                "conjbeams": conjbeams,
                "computepastep": computepastep,
                #
                "rotatepastep": rotatepastep,  #'mtype':mtype, # 'weightlimit':weightlimit,
                "pointingoffsetsigdev": pointingoffsetsigdev,
                # facets group
                "facets": facets,
                "chanchunks": chanchunks,
                # interpolation group
                "interpolation": interpolation,
                "wprojplanes": wprojplanes,
                # deconvolver group
                "deconvolver": deconvolver,
                "vptable": vptable,
                "imagename": imagename,
                # single-dish specific parameters
                # ---- spatial coordinates
                "pointingcolumntouse": pointingcolumntouse,
                "convertfirst": convertfirst,
                # ---- convolution function
                "convfunc": gridfunction,
                "convsupport": convsupport,
                # ---- truncate group
                "truncate": truncate,
                "gwidth": gwidth,
                "jwidth": jwidth,
                # ---- minweight group
                "minweight": minweight,
                "clipminmax": clipminmax,
            }
        }
        # ---- Weighting
        if True:  # Compute rmode and self.weightpars
            rmode = "none"
            if weighting == "briggsabs":
                rmode = "abs"
                weighting = "briggs"
            elif weighting == "briggs":
                rmode = "norm"
            elif weighting == "briggsbwtaper":
                rmode = "bwtaper"
                weighting = "briggs"

            self.weightpars = {
                "type": weighting,
                "rmode": rmode,
                "robust": robust,
                "noise": noise,
                "npixels": npixels,
                "uvtaper": uvtaper,
                "multifield": mosweight,
                "usecubebriggs": perchanweightdensity,
            }
        # ---- Normalizers ( this is where flat noise, flat sky rules will go... )
        self.allnormpars = {
            self.defaultKey: {
                # pblimit group
                "pblimit": pblimit,
                "nterms": nterms,
                "facets": facets,
                # normtype group
                "normtype": normtype,
                "workdir": workdir,
                # deconvolver group
                "deconvolver": deconvolver,
                "imagename": imagename,
                "restoringbeam": restoringbeam,
                "psfcutoff": psfcutoff,
                "makesingledishnormalizer": makesingledishnormalizer,
                "calcres": calcres,
                "calcpsf": calcpsf,
            }
        }
        # ---- Deconvolution
        self.alldecpars = {
            self.defaultKey: {
                "id": 0,
                "deconvolver": deconvolver,
                "nterms": nterms,
                "scales": scales,
                "scalebias": scalebias,
                "restoringbeam": restoringbeam,
                "usemask": usemask,
                "mask": mask,
                "pbmask": pbmask,
                "maskthreshold": maskthreshold,
                "maskresolution": maskresolution,
                "nmask": nmask,
                #'maskresolution':maskresolution, 'nmask':nmask,'autoadjust':autoadjust,
                "sidelobethreshold": sidelobethreshold,
                "noisethreshold": noisethreshold,
                "lownoisethreshold": lownoisethreshold,
                "negativethreshold": negativethreshold,
                "smoothfactor": smoothfactor,
                "fusedthreshold": fusedthreshold,
                "specmode": specmode,
                "largestscale": largestscale,
                "minbeamfrac": minbeamfrac,
                "cutthreshold": cutthreshold,
                "growiterations": growiterations,
                "dogrowprune": dogrowprune,
                "minpercentchange": minpercentchange,
                "verbose": verbose,
                "fastnoise": fastnoise,
                "interactive": interactive,
                "startmodel": startmodel,
                "nsigma": nsigma,
                "imagename": imagename,
                "fullsummary": fullsummary,
            }
        }
        # ---- Iteration control
        self.iterpars = {
            "niter": niter,
            "cycleniter": cycleniter,
            "threshold": threshold,
            "loopgain": loopgain,
            "interactive": interactive,
            "cyclefactor": cyclefactor,
            "minpsffraction": minpsffraction,
            "maxpsffraction": maxpsffraction,
            "savemodel": savemodel,
            "nsigma": nsigma,
            "nmajor": nmajor,
            "fullsummary": fullsummary,
        }
        # ---- CFCache params
        self.cfcachepars = {"cflist": cflist}
        # ---- Parameters that may be internally modified for savemodel behavior
        self.inpars = {
            "savemodel": savemodel,
            "interactive": interactive,
            "nsigma": nsigma,
            "usemask": usemask,
        }
        # ---- List of supported parameters in outlier files.
        # All other parameters will default to the global values.
        self.outimparlist = [
            "imagename",
            "nchan",
            "imsize",
            "cell",
            "phasecenter",
            "startmodel",
            "start",
            "width",
            "nterms",
            "reffreq",
            "specmode",
        ]
        self.outgridparlist = ["gridder", "deconvolver", "wprojplanes"]
        self.outweightparlist = []
        self.outdecparlist = [
            "deconvolver",
            "startmodel",
            "nterms",
            "usemask",
            "mask",
        ]
        self.outnormparlist = ["deconvolver", "weightlimit", "nterms"]

        ret = self.checkParameters(parallel)
        if ret == False:
            casalog.post(
                "Found errors in input parameters. Please check.", "WARN"
            )

        self.printParameters()

    def resetParameters(self):
        """reset parameters to the original settting for interactive, nsigma, auto-multithresh when savemodel!='none'"""
        if self.inpars["savemodel"] != "none" and (
            self.inpars["interactive"] == True
            or self.inpars["usemask"] == "auto-multithresh"
            or self.inpars["nsigma"] > 0.0
        ):
            # in checkAndFixIterationPars(), when saving model is on, the internal params, readonly and usescrath are set to True and False,
            # respectively. So this needs to be undone before calling predictModel.
            self.iterpars["savemodel"] = self.inpars["savemodel"]
            if self.inpars["savemodel"] == "modelcolumn":
                for key in self.allselpars:  # for all MSes
                    self.allselpars[key]["readonly"] = False
                    self.allselpars[key]["usescratch"] = True

            elif self.inpars["savemodel"] == "virtual":
                for key in self.allselpars:  # for all MSes
                    self.allselpars[key]["readonly"] = False
                    self.allselpars[key]["usescratch"] = False

    def getAllPars(self):
        """Return the state of all parameters"""
        return self.allparameters

    def getSelPars(self):
        return self.allselpars

    def getImagePars(self):
        return self.allimpars

    def getGridPars(self):
        return self.allgridpars

    def getWeightPars(self):
        return self.weightpars

    def getDecPars(self):
        return self.alldecpars

    def getIterPars(self):
        return self.iterpars

    def getNormPars(self):
        return self.allnormpars

    def getCFCachePars(self):
        return self.cfcachepars

    def setSelPars(self, selpars):
        for key in selpars.keys():
            self.allselpars[key] = selpars[key]

    def setImagePars(self, impars):
        for key in impars.keys():
            self.allimpars[key] = impars[key]

    def setGridPars(self, gridpars):
        for key in gridpars.keys():
            self.allgridpars[key] = gridpars[key]

    def setWeightPars(self, weightpars):
        for key in weightpars.keys():
            self.weightpars[key] = weightpars[key]

    def setDecPars(self, decpars):
        for key in decpars.keys():
            self.alldecpars[key] = decpars[key]

    def setIterPars(self, iterpars):
        for key in iterpars.keys():
            self.iterpars[key] = iterpars[key]

    def setNormPars(self, normpars):
        for key in normpars.keys():
            self.allnormpars[key] = normpars[key]

    def checkParameters(self, parallel=False):
        # casalog.origin('refimagerhelper.checkParameters')
        casalog.post("Verifying Input Parameters")
        # Init the error-string
        errs = ""
        try:
            errs += self.checkAndFixSelectionPars()
            errs += self.makeImagingParamLists(parallel)
            errs += self.checkAndFixIterationPars()
            errs += self.checkAndFixNormPars()

            for mss in sorted(self.allselpars.keys()):
                if self.allimpars["0"]["specmode"] == "cubedata":
                    self.allselpars[mss]["outframe"] = "Undefined"
                if self.allimpars["0"]["specmode"] == "cubesource":
                    self.allselpars[mss]["outframe"] = "REST"
            ### MOVE this segment of code to the constructor so that it's clear which parameters go where !
            ### Copy them from 'impars' to 'normpars' and 'decpars'
            self.iterpars["allimages"] = {}
            for immod in self.allimpars.keys():
                self.allnormpars[immod]["imagename"] = self.allimpars[immod][
                    "imagename"
                ]
                self.alldecpars[immod]["imagename"] = self.allimpars[immod][
                    "imagename"
                ]
                self.allgridpars[immod]["imagename"] = self.allimpars[immod][
                    "imagename"
                ]
                self.iterpars["allimages"][immod] = {
                    "imagename": self.allimpars[immod]["imagename"],
                    "multiterm": (
                        self.alldecpars[immod]["deconvolver"] == "mtmfs"
                    ),
                }

            ## Integers need to be NOT numpy versions.
            self.fixIntParam(self.allimpars, "imsize")
            self.fixIntParam(self.allimpars, "nchan")
            self.fixIntParam(self.allimpars, "nterms")
            self.fixIntParam(self.allnormpars, "nterms")
            self.fixIntParam(self.alldecpars, "nterms")
            self.fixIntParam(self.allgridpars, "facets")
            self.fixIntParam(self.allgridpars, "chanchunks")
        except Exception as exc:
            if len(errs) > 0:
                # errs string indicates that maybe this exception was our fault, indicate as such and provide the errs string to the user
                raise Exception(
                    "Parameter Errors : \n{}\nThese errors may have caused the '{}'".format(
                        errs, type(exc)
                    )
                )
            else:
                # something unforseen happened, just re-throw the exception
                raise

        ## If there are errors, print a message and exit.
        if len(errs) > 0:
            #            casalog.post('Parameter Errors : \n' + errs,'WARN')
            raise Exception("Parameter Errors : \n" + errs)
        return True

    ###### Start : Parameter-checking functions ##################

    def checkAndFixSelectionPars(self):
        errs = ""

        # If it's already a dict with ms0,ms1,etc...leave it be.
        ok = True
        for kk in self.allselpars.keys():
            if kk.find("ms") != 0:
                ok = False

        if ok == True:
            # casalog.post("Already in correct format")
            return errs

        # print("allselpars=",self.allselpars)
        # msname, field, spw, etc must all be equal-length lists of strings, or all except msname must be of length 1.
        if not "msname" in self.allselpars:
            errs = errs + "MS name(s) not specified"
        else:
            if type(self.allselpars["msname"]) == list:
                # (timesortedvislist, times) = sort_mslist(self.allselpars['msname'])
                (timesortedvislist, times, newindex) = self.mslist_timesorting(
                    self.allselpars["msname"]
                )
                if timesortedvislist != self.allselpars["msname"]:
                    self.allselpars["msname"] = timesortedvislist
                    casalog.post(
                        "Sorting the vis list by time. The new vis list:"
                        + str(self.allselpars["msname"])
                    )
                    for selp in [
                        "spw",
                        "field",
                        "timestr",
                        "uvdist",
                        "antenna",
                        "scan",
                        "obs",
                        "state",
                    ]:
                        if type(self.allselpars[selp]) == list and len(
                            self.allselpars[selp]
                        ) == len(newindex):
                            self.allselpars[selp] = [
                                self.allselpars[selp][i] for i in newindex
                            ]

                # msdiff = check_mslist(self.allselpars['msname'], ignore_tables=['SORTED_TABLE', 'ASDM*'])
                msdiff = check_mslist(
                    self.allselpars["msname"],
                    ignore_tables=["SORTED_TABLE", "ASDM*"],
                    testcontent=False,
                )

                # Only call this if vis == list and there is mismatch in wtspec columns
                # Maybe expanded for other checks later...
                if msdiff != {}:
                    # print("MS diff===",msdiff)
                    noWtspecmslist = []
                    for msfile, diff_info in msdiff.items():
                        # check Main
                        if "Main" in diff_info:
                            for diffkey in diff_info["Main"]:
                                if (
                                    diffkey == "missingcol_a"
                                    or diffkey == "missingcol_b"
                                ):
                                    if (
                                        "WEIGHT_SPECTRUM"
                                        in diff_info["Main"]["missingcol_a"]
                                        and self.allselpars["msname"][0]
                                        not in noWtspecmslist
                                    ):
                                        noWtspecmslist.append(
                                            self.allselpars["msname"][0]
                                        )
                                    if (
                                        "WEIGHT_SPECTRUM"
                                        in diff_info["Main"]["missingcol_b"]
                                        and msfile not in noWtspecmslist
                                    ):
                                        noWtspecmslist.append(msfile)
                                        # repalce this by addwtspec(list_of_ms_withoutWtSpec)
                                        # self.checkmsforwtspec`
                    if noWtspecmslist != []:
                        # print ("OK addwtspec to "+str(noWtspecmslist))
                        self.addwtspec(noWtspecmslist)

            selkeys = self.allselpars.keys()

            # Convert all non-list parameters into lists.
            for par in selkeys:
                if type(self.allselpars[par]) != list:
                    self.allselpars[par] = [self.allselpars[par]]

            # Check that all are the same length as nvis
            # If not, and if they're single, replicate them nvis times
            nvis = len(self.allselpars["msname"])

            if nvis == 0:
                errs = errs + "Input MS list is empty"
                return errs

            for par in selkeys:
                if (
                    len(self.allselpars[par]) > 1
                    and len(self.allselpars[par]) != nvis
                ):
                    errs = (
                        errs
                        + str(par)
                        + " must have a single entry, or "
                        + str(nvis)
                        + " entries to match vis list \n"
                    )
                    return errs
                else:  # Replicate them nvis times if needed.
                    if len(self.allselpars[par]) == 1:
                        for ms in range(1, nvis):
                            self.allselpars[par].append(
                                self.allselpars[par][0]
                            )

            # Now, all parameters are lists of strings each of length 'nvis'.
            # Put them into separate dicts per MS.
            selparlist = {}
            for ms in range(0, nvis):
                selparlist["ms" + str(ms)] = {}
                for par in selkeys:
                    selparlist["ms" + str(ms)][par] = self.allselpars[par][ms]

                synu = synthesisutils()
                selparlist["ms" + str(ms)] = synu.checkselectionparams(
                    selparlist["ms" + str(ms)]
                )
                synu.done()

            # casalog.post(selparlist)
            self.allselpars = selparlist

        return errs

    def makeImagingParamLists(self, parallel):
        errs = ""
        # casalog.post("specmode=",self.allimpars['0']['specmode'], " parallel=",parallel)
        ## Multiple images have been specified.
        ## (1) Parse the outlier file and fill a list of imagedefinitions
        ## OR (2) Parse lists per input parameter into a list of parameter-sets (imagedefinitions)
        ### The code below implements (1)
        outlierpars = []
        parseerrors = ""
        if len(self.outlierfile) > 0:
            outlierpars, parseerrors = self.parseOutlierFile(self.outlierfile)
            if parallel:
                casalog.post("CALLING checkParallelMFMixModes...")
                errs = self.checkParallelMFMixedModes(
                    self.allimpars, outlierpars
                )
                if len(errs):
                    return errs

        if len(parseerrors) > 0:
            errs = errs + "Errors in parsing outlier file : " + parseerrors
            return errs

        # Initialize outlier parameters with defaults
        # Update outlier parameters with modifications from outlier files
        for immod in range(0, len(outlierpars)):
            modelid = str(immod + 1)
            self.allimpars[modelid] = copy.deepcopy(self.allimpars["0"])
            self.allimpars[modelid].update(outlierpars[immod]["impars"])
            self.allgridpars[modelid] = copy.deepcopy(self.allgridpars["0"])
            self.allgridpars[modelid].update(outlierpars[immod]["gridpars"])
            self.alldecpars[modelid] = copy.deepcopy(self.alldecpars["0"])
            self.alldecpars[modelid].update(outlierpars[immod]["decpars"])
            self.allnormpars[modelid] = copy.deepcopy(self.allnormpars["0"])
            self.allnormpars[modelid].update(outlierpars[immod]["normpars"])
            self.alldecpars[modelid]["id"] = immod + 1  ## Try to eliminate.

        # casalog.post(self.allimpars)

        #
        #        casalog.post("REMOVING CHECKS to check...")
        #### This does not handle the conversions of the csys correctly.....
        ####
        #        for immod in self.allimpars.keys() :
        #            tempcsys = {}
        #            if 'csys' in self.allimpars[immod]:
        #                tempcsys = self.allimpars[immod]['csys']
        #
        #            synu = synthesisutils()
        #            self.allimpars[immod] = synu.checkimageparams( self.allimpars[immod] )
        #            synu.done()
        #
        #            if len(tempcsys.keys())==0:
        #                self.allimpars[immod]['csys'] = tempcsys

        ## Check for name increments, and copy from impars to decpars and normpars.
        self.handleImageNames()

        return errs

    def handleImageNames(self):

        for immod in self.allimpars.keys():
            inpname = self.allimpars[immod]["imagename"]

            ### If a directory name is embedded in the image name, check that the dir exists.
            if inpname.count("/"):
                splitname = inpname.split("/")
                prefix = splitname[len(splitname) - 1]
                dirname = inpname[
                    0 : len(inpname) - len(prefix)
                ]  # has '/' at end
                if not os.path.exists(dirname):
                    casalog.post("Making directory : " + dirname, "INFO")
                    os.mkdir(dirname)

        ### Check for name increments
        # if self.reusename == False:

        if (
            self.allimpars["0"]["restart"] == False
        ):  # Later, can change this to be field dependent too.
            ## Get a list of image names for all fields (to sync name increment ids across fields)
            inpnamelist = {}
            for immod in self.allimpars.keys():
                inpnamelist[immod] = self.allimpars[immod]["imagename"]

            newnamelist = self.incrementImageNameList(inpnamelist)

            if len(newnamelist) != len(self.allimpars.keys()):
                casalog.post(
                    "Internal Error : Non matching list lengths in refimagerhelper::handleImageNames. Not updating image names",
                    "WARN",
                )
            else:
                for immod in self.allimpars.keys():
                    self.allimpars[immod]["imagename"] = newnamelist[immod]

    def checkAndFixIterationPars(self):
        errs = ""

        # Bother checking only if deconvolution iterations are requested
        if self.iterpars["niter"] > 0:
            # Make sure cycleniter is less than or equal to niter.
            if (
                self.iterpars["cycleniter"] <= 0
                or self.iterpars["cycleniter"] > self.iterpars["niter"]
            ):
                if self.iterpars["interactive"] == False:
                    self.iterpars["cycleniter"] = self.iterpars["niter"]
                else:
                    self.iterpars["cycleniter"] = min(
                        self.iterpars["niter"], 100
                    )

            # saving model is done separately outside of iter. control for interactive clean and or automasking cases

            if self.iterpars["savemodel"] != "none":
                if (
                    self.iterpars["interactive"] == True
                    or self.alldecpars["0"]["usemask"] == "auto-multithresh"
                    or self.alldecpars["0"]["nsigma"] > 0.0
                ):
                    self.iterpars["savemodel"] = "none"
                    for visid in self.allselpars:
                        self.allselpars[visid]["readonly"] = True
                        self.allselpars[visid]["usescratch"] = False

        return errs

    def checkAndFixNormPars(self):
        errs = ""

        #        for modelid in self.allnormpars.keys():
        #            if len(self.allnormpars[modelid]['workdir'])==0:
        #                self.allnormpars[modelid]['workdir'] = self.allnormpars['0']['imagename'] + '.workdir'

        return errs

    ###### End : Parameter-checking functions ##################

    ## Parse outlier file and construct a list of imagedefinitions (dictionaries).
    def parseOutlierFile(self, outlierfilename=""):
        returnlist = []
        errs = ""  #  must be empty for no error

        if len(outlierfilename) > 0 and not os.path.exists(outlierfilename):
            errs += "Cannot find outlier file : " + outlierfilename + "\n"
            return returnlist, errs

        fp = open(outlierfilename, "r")
        thelines = fp.readlines()
        tempimpar = {}
        tempgridpar = {}
        tempweightpar = {}
        tempdecpar = {}
        tempnormpar = {}
        for oneline in thelines:
            aline = oneline.replace("\n", "")
            #            aline = oneline.replace(' ','').replace('\n','')
            if len(aline) > 0 and aline.find("#") != 0:
                parpair = aline.split("=")
                parpair[0] = parpair[0].replace(" ", "")
                # casalog.post(parpair)
                if len(parpair) != 2:
                    errs += "Error in line containing : " + oneline + "\n"
                if parpair[0] == "imagename" and tempimpar != {}:
                    # returnlist.append({'impars':tempimpar, 'gridpars':tempgridpar, 'weightpars':tempweightpar, 'decpars':tempdecpar} )
                    returnlist.append(
                        {
                            "impars": tempimpar,
                            "gridpars": tempgridpar,
                            "weightpars": tempweightpar,
                            "decpars": tempdecpar,
                            "normpars": tempnormpar,
                        }
                    )
                    tempimpar = {}
                    tempgridpar = {}
                    tempweightpar = {}
                    tempdecpar = {}
                    tempnormpar = {}
                usepar = False
                if parpair[0] in self.outimparlist:
                    tempimpar[parpair[0]] = parpair[1]
                    usepar = True
                if parpair[0] in self.outgridparlist:
                    tempgridpar[parpair[0]] = parpair[1]
                    usepar = True
                if parpair[0] in self.outweightparlist:
                    tempweightpar[parpair[0]] = parpair[1]
                    usepar = True
                if parpair[0] in self.outdecparlist:
                    tempdecpar[parpair[0]] = parpair[1]
                    usepar = True
                if parpair[0] in self.outnormparlist:
                    tempnormpar[parpair[0]] = parpair[1]
                    usepar = True
                if usepar == False:
                    casalog.post(
                        "Ignoring unknown parameter pair : " + oneline
                    )

        if len(errs) == 0:
            returnlist.append(
                {
                    "impars": tempimpar,
                    "gridpars": tempgridpar,
                    "weightpars": tempweightpar,
                    "decpars": tempdecpar,
                    "normpars": tempnormpar,
                }
            )

        ## Extra parsing for a few parameters.
        returnlist = self.evalToTarget(
            returnlist, "impars", "imsize", "intvec"
        )
        returnlist = self.evalToTarget(returnlist, "impars", "nchan", "int")
        returnlist = self.evalToTarget(returnlist, "impars", "cell", "strvec")
        returnlist = self.evalToTarget(returnlist, "impars", "nterms", "int")
        returnlist = self.evalToTarget(returnlist, "decpars", "nterms", "int")
        returnlist = self.evalToTarget(returnlist, "normpars", "nterms", "int")
        returnlist = self.evalToTarget(
            returnlist, "gridpars", "wprojplanes", "int"
        )
        #        returnlist = self.evalToTarget( returnlist, 'impars', 'reffreq', 'strvec' )

        # casalog.post(returnlist)
        return returnlist, errs

    def evalToTarget(self, globalpars, subparkey, parname, dtype="int"):
        try:
            for fld in range(0, len(globalpars)):
                if parname in globalpars[fld][subparkey]:
                    if dtype == "int" or dtype == "intvec":
                        val_e = eval(globalpars[fld][subparkey][parname])
                    if dtype == "strvec":
                        tcell = globalpars[fld][subparkey][parname]
                        tcell = (
                            tcell.replace(" ", "")
                            .replace("[", "")
                            .replace("]", "")
                            .replace("'", "")
                        )
                        tcells = tcell.split(",")
                        val_e = []
                        for cell in tcells:
                            val_e.append(cell)

                    globalpars[fld][subparkey][parname] = val_e
        except:
            casalog.post(
                'Cannot evaluate outlier field parameter "' + parname + '"',
                "ERROR",
            )

        return globalpars

    def printParameters(self):
        casalog.post("SelPars : " + str(self.allselpars), "INFO2")
        casalog.post("ImagePars : " + str(self.allimpars), "INFO2")
        casalog.post("GridPars : " + str(self.allgridpars), "INFO2")
        casalog.post("NormPars : " + str(self.allnormpars), "INFO2")
        casalog.post("Weightpars : " + str(self.weightpars), "INFO2")
        casalog.post("DecPars : " + str(self.alldecpars), "INFO2")
        casalog.post("IterPars : " + str(self.iterpars), "INFO2")

    def incrementImageName(self, imagename):
        dirname = "."
        prefix = imagename

        if imagename.count("/"):
            splitname = imagename.split("/")
            prefix = splitname[len(splitname) - 1]
            ### if it has a leading / then absolute path is assumed
            dirname = (
                (imagename[0 : len(imagename) - len(prefix)])
                if (imagename[0] == "/")
                else ("./" + imagename[0 : len(imagename) - len(prefix)])
            )  # has '/' at end

        inamelist = [
            fn for fn in os.listdir(dirname) if any([fn.startswith(prefix)])
        ]

        if len(inamelist) == 0:
            newimagename = dirname[2:] + prefix
        else:
            nlen = len(prefix)
            maxid = 1
            for iname in inamelist:
                startind = iname.find(prefix + "_")
                if startind == 0:
                    idstr = (iname[nlen + 1 : len(iname)]).split(".")[0]
                    if idstr.isdigit():
                        val = eval(idstr)
                        if val > maxid:
                            maxid = val
            newimagename = dirname[2:] + prefix + "_" + str(maxid + 1)

        casalog.post("Using : {}".format(newimagename))
        return newimagename

    def incrementImageNameList(self, inpnamelist):

        dirnames = {}
        prefixes = {}

        for immod in inpnamelist.keys():
            imagename = inpnamelist[immod]
            dirname = "."
            prefix = imagename

            if imagename.count("/"):
                splitname = imagename.split("/")
                prefix = splitname[len(splitname) - 1]
                dirname = (
                    (imagename[0 : len(imagename) - len(prefix)])
                    if (imagename[0] == "/")
                    else ("./" + imagename[0 : len(imagename) - len(prefix)])
                )  # has '/' at end

            dirnames[immod] = dirname
            prefixes[immod] = prefix

        maxid = 0
        for immod in inpnamelist.keys():
            prefix = prefixes[immod]
            inamelist = [
                fn
                for fn in os.listdir(dirnames[immod])
                if any([fn.startswith(prefix)])
            ]
            nlen = len(prefix)

            if len(inamelist) == 0:
                locmax = 0
            else:
                locmax = 1

            cleanext = [
                ".image",
                ".residual",
                ".model",
                ".psf",
                ".sumwt",
                ".tt0",
            ]
            incremented = False
            for iname in inamelist:
                rootname, ext = os.path.splitext(iname)
                if ext in cleanext:
                    startind = iname.find(prefix + "_")
                    if startind == 0:
                        idstr = (iname[nlen + 1 : len(iname)]).split(".")[0]
                        if idstr.isdigit():
                            val = eval(idstr)
                            incremented = True
                            if val > locmax:
                                locmax = val
                    elif startind == -1:
                        if ext == ".tt0":
                            # need one more pass to extract rootname
                            rootname, ext = os.path.splitext(rootname)
                        if rootname == prefix:
                            # the file name with root file name only
                            incremented = True

            if not incremented:
                locmax = 0
            if locmax > maxid:
                maxid = locmax

        newimagenamelist = {}
        for immod in inpnamelist.keys():
            if maxid == 0:
                newimagenamelist[immod] = inpnamelist[immod]
            else:
                newimagenamelist[immod] = (
                    dirnames[immod][2:]
                    + prefixes[immod]
                    + "_"
                    + str(maxid + 1)
                )

        #        casalog.post('Input : ',  inpnamelist)
        #        casalog.post('Dirs : ', dirnames)
        #        casalog.post('Pre : ', prefixes)
        #        casalog.post('Max id : ', maxid)
        #        casalog.post('Using : ',  newimagenamelist)
        return newimagenamelist

    ## Guard against numpy int32,int64 types which don't convert well across tool boundary.
    ## For CAS-8250. Remove when CAS-6682 is done.
    def fixIntParam(self, allpars, parname):
        for immod in allpars.keys():
            if parname in allpars[immod]:
                ims = allpars[immod][parname]
                if type(ims) != list:
                    ims = int(ims)
                else:
                    for el in range(0, len(ims)):
                        ims[el] = int(ims[el])
                allpars[immod][parname] = ims

    # check for non-supported multifield in mixed modes in parallel
    #  (e.g. combination cube and continuum for main and outlier fields)
    def checkParallelMFMixedModes(self, allimpars, outlierpars):
        errmsg = ""
        casalog.post("outlierpars=={}".format(outlierpars))
        mainspecmode = allimpars["0"]["specmode"]
        mainnchan = allimpars["0"]["nchan"]
        casalog.post(
            "mainspecmode={} mainnchan={}".format(mainspecmode, mainnchan)
        )
        cubeoutlier = False
        contoutlier = False
        isnchanmatch = True
        for immod in range(0, len(outlierpars)):
            if "impars" in outlierpars[immod]:
                if "nchan" in outlierpars[immod]["impars"]:
                    if outlierpars[immod]["impars"]["nchan"] > 1:
                        cubeoutlier = True
                        if outlierpars[immod]["impars"]["nchan"] != mainnchan:
                            isnchanmatch = False
                    else:
                        contoutlier = True
                else:
                    if "specmode" in outlierpars[immod]["impars"]:
                        if outlierpars[immod]["impars"]["specmode"] == "mfs":
                            contoutlier = True
        if mainspecmode.find("cube") == 0:
            if contoutlier:
                errmsg = "Mixed cube and continuum mode for multifields is currently not supported for parallel mode"
            else:  # all cube modes, but need to check if the nchans are the same
                if not isnchanmatch:
                    errmsg = "Cubes for multifields with different nchans are currently not supported for parallel mode "
        else:  # mfs
            if cubeoutlier:
                errmsg = "Mixed continuum and cube mode for multifields is currently not supported for parallel mode"
        errs = errmsg
        return errs

    def checkmsforwtspec(self):
        """check if WEIGHT_SPECTRUM column exist when
        a list of vis is given. Add the column for an MS
        which does not have one if other MSs have the column.
        This is a workaround for the issue probably in Vi/VB2
        not handling the state change for the optional column
        when dealing with multiples MSs
        """
        mycb = calibrater()
        mytb = table()
        haswtspec = False
        mswithnowtspec = []
        nms = 1
        if type(self.allselpars["msname"]) == list:
            nms = len(self.allselpars["msname"])

        if nms > 1:
            for inms in self.allselpars["msname"]:
                mytb.open(inms)
                cols = mytb.colnames()
                mytb.close()
                if "WEIGHT_SPECTRUM" in cols:
                    haswtspec = True
                else:
                    mswithnowtspec.append(inms)
            if haswtspec and len(mswithnowtspec) > 0:
                casalog.post(
                    "Some of the MSes donot have WEIGHT_SPECTRUM while some other do."
                    + " Automatically adding the column and initialize for those don't to avoid a process failure.",
                    "WARN",
                )
                for inms in mswithnowtspec:
                    mycb.open(inms, addcorr=False, addmodel=False)
                    mycb.initweights(wtmode="weight", dowtsp=True)
                    mycb.close()
        # noOp for nms==1

    def mslist_timesorting(self, mslist):
        """
        wrapper for mslisthelper.sort_mslist to get a sorting order w.r.t the original
        """
        (thenewmslist, times) = sort_mslist(mslist)
        theindex = []
        for vnew in thenewmslist:
            for vold in mslist:
                if vnew == vold:
                    theindex.append(mslist.index(vnew))
        return (thenewmslist, times, theindex)

    def addwtspec(self, mslist):
        """
        Add the column for an MS which does not have one if other MSs have the column.
        This is a workaround for the issue probably in Vi/VB2
        not handling the state change for the optional column
        when dealing with multiples MSs
        """
        mycb = calibrater()

        if len(mslist) > 0:
            casalog.post(
                "Some of the MSes donot have WEIGHT_SPECTRUM while some other do."
                + " Automatically adding the column and initialize using the existing WEIGHT column for those don't to avoid a process failure.",
                "WARN",
            )
            casalog.post(
                "Adding WEIGHT_SPECTRUM in the following MS(s): "
                + str(mslist),
                "WARN",
            )
            for inms in mslist:
                mycb.open(inms, addcorr=False, addmodel=False)
                mycb.initweights(wtmode="weight", dowtsp=True)
                mycb.close()
        mycb.done()
        # noOp for len(mlist) ==0

    ############################


#################################################################################################
def backupoldfile(thefile=""):
    import copy
    import shutil

    if thefile == "" or (not os.path.exists(thefile)):
        return
    outpathdir = os.path.realpath(os.path.dirname(thefile))
    outpathfile = outpathdir + os.path.sep + os.path.basename(thefile)
    k = 0
    backupfile = outpathfile + "." + str(k)
    prevfile = "--------"
    while os.path.exists(backupfile):
        k = k + 1
        prevfile = copy.copy(backupfile)
        if os.path.exists(prevfile) and filecmp.cmp(outpathfile, prevfile):
            ##avoid making multiple copies of the same file
            return
        backupfile = outpathfile + "." + str(k)
    shutil.copy2(outpathfile, backupfile)


def saveparams2last(func=None, multibackup=True):
    """This function is a decorator function that allows for
    task.last to be saved even if calling without casashell. Also
    saves unique revisions ...just like the vax/vms style of revision saving
    by default. set multibackup=False to no not have old revisions kept
    """
    if not func:
        return functools.partial(saveparams2last, multibackup=multibackup)

    @functools.wraps(func)
    def wrapper_saveparams(*args, **kwargs):
        #        multibackup=True
        outfile = func.__name__ + ".last"
        # print('args {} and kwargs {}'.format(args, kwargs))
        # print('length of args {}, and kwargs {}'.format(len(args), len(kwargs)))
        params = {}
        byIndex = list()
        if len(kwargs) == 0:
            paramsname = list(inspect.signature(func).parameters)
            # params={paramsname[i]: args[i] for i in range(len(args))}
            params = OrderedDict(zip(paramsname, args))
            byIndex = list(params)
        else:
            params = kwargs
            byIndex = list(params)
            ###for some reason the dictionary is in reverse
            byIndex.reverse()
        # print('@@@@MULTIBACKUP {},  params {}'.format(multibackup, params))
        if multibackup:
            backupoldfile(outfile)
        with open(outfile, "w") as _f:
            for _i in range(len(byIndex)):
                _f.write(
                    "%-20s = %s\n" % (byIndex[_i], repr(params[byIndex[_i]]))
                )
            _f.write("#" + func.__name__ + "( ")
            for _i in range(len(byIndex)):
                _f.write("%s=%s" % (byIndex[_i], repr(params[byIndex[_i]])))
                if _i < len(params) - 1:
                    _f.write(",")
            _f.write(" )\n")
        ###End of stuff before task is called
        retval = func(*args, **kwargs)
        ###we could do something here post task
        return retval

    return wrapper_saveparams


######################################################


def determineFreqRange(
    vis: str = "", fieldid: int = 0, spw: str = "*"
) -> Tuple[np.double, np.double]:
    _tb = table()
    _ms = ms()
    _su = synthesisutils()
    _qa = quanta()
    minFreq = 1.0e20
    maxFreq = 0.0
    _tb.open(vis)
    fieldids = _tb.getcol("FIELD_ID")
    _tb.done()
    # advisechansel does not work on fieldids not in main
    if fieldid not in fieldids:
        fieldid = fieldids[0]
    frange = _su.advisechansel(
        msname=vis, getfreqrange=True, fieldid=fieldid, spwselection=spw
    )
    if minFreq > _qa.convert(frange["freqstart"], "Hz")["value"]:
        minFreq = _qa.convert(frange["freqstart"], "Hz")["value"]
    if maxFreq < _qa.convert(frange["freqend"], "Hz")["value"]:
        maxFreq = _qa.convert(frange["freqend"], "Hz")["value"]

    if minFreq > maxFreq:
        raise Exception(f"Failed to determine frequency range in ms {vis}")
    freqwidth = maxFreq - minFreq
    return (minFreq, freqwidth)



def sanitize_tclean_inputs(inpparams):
    """

    Translate param names that are different between tclean input and the
    layers underneath (pySynthesisImager etc.).

    """
    ###now deal with parameters which are not the same name
    inpparams['msname']= inpparams.pop('vis')
    inpparams['timestr']= inpparams.pop('timerange')
    inpparams['uvdist']= inpparams.pop('uvrange')
    inpparams['obs']= inpparams.pop('observation')
    inpparams['state']= inpparams.pop('intent')
    inpparams['loopgain']=inpparams.pop('gain')
    inpparams['scalebias']=inpparams.pop('smallscalebias')
    #
    # Force chanchunks=1 always now (CAS-13400)
    inpparams['chanchunks']=1


    # Put all parameters into dictionaries and check them.
    ##make a dictionary of parameters that ImagerParameters take

    defparm = dict(
        list(
            zip(
                ImagerParameters.__init__.__code__.co_varnames[1:],
                ImagerParameters.__init__.__defaults__,
            )
        )
    )

    return inpparams, defparm



