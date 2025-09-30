from scipy import fftpack
import numpy as np
import shutil
import os
import time
import random

from casatools import quanta, table, image, componentlist, regionmanager, imager
from casatasks import casalog, feather

_ia = image()
_qa = quanta()

class SDINT_helper:

    def __init__(self, tmpFileNumber=0):
      if type(tmpFileNumber) != int or tmpFileNumber<=0:    
          casalog.post('No valid tmp file tag provided. Will use a random number.', 'DEBUG')
          tmpFileNumber = random.randint(100000,999999)
          
      self.tmpFileTag = str(tmpFileNumber)
      casalog.post('Initializing SDINT Helper instance with tmp file tag '+self.tmpFileTag)

      # define tmp file names
      self.tmpintplane = 'tmp_'+self.tmpFileTag+'_intplane'
      self.tmpsdplane = 'tmp_'+self.tmpFileTag+'_sdplane'
      self.tmpjointplane = 'tmp_'+self.tmpFileTag+'_jointplane'
      self.tmpallplanes = 'tmp_'+self.tmpFileTag+'_*plane'
      
    def getTmpFileTag(self):
        return self.tmpFileTag

    def getAllTmpFileRegex(self):
        return self.tmpallplanes

    def deleteTmpFiles(self):
        casalog.post('Deleting '+self.tmpallplanes)
        os.system('rm -rf '+self.tmpallplanes)

      
################################################
    def getFreqAxisIndex(self, myia):
        try:
            mysummary = myia.summary(list=False)
            freqaxis_index = list(mysummary['axisnames']).index('Frequency')
        except(ValueError):
            myia.close()
            casalog.post('The image '+myia.name()+' has no frequency axis. Try adding one with ia.adddegaxis() .', 'SEVERE')

        return freqaxis_index
            
    def getFreqList(self,imname=''):
        """ Get the list of frequencies for the given image, one for each channel.

            Returns:
            list[float] The frequencies for each channel in the image, in Hz.
        """

        _ia.open(imname)
        csys =_ia.coordsys()
        shp = _ia.shape()
        freqaxis_index = self.getFreqAxisIndex(_ia)
        _ia.close()

        if(csys.axiscoordinatetypes()[freqaxis_index] == 'Spectral'):
            restfreq = csys.referencevalue()['numeric'][freqaxis_index]
            freqincrement = csys.increment()['numeric'][freqaxis_index]
            freqlist = [];
            for chan in range(0,shp[freqaxis_index]):
                freqlist.append(restfreq + chan * freqincrement);
        elif(csys.axiscoordinatetypes()[freqaxis_index] == 'Tabular'):
            freqlist = (csys.torecord()['tabular2']['worldvalues'])
        else:
            casalog.post('Unknown frequency axis. Exiting.','SEVERE');
            return False;

        csys.done()
        return freqlist

################################################

    def copy_restoringbeam(self,fromthis='',tothis=''):

        ia2 = image()
        
        freqlist = self.getFreqList(fromthis)
        casalog.post('Copying restoring beam(s) for '+str(len(freqlist))+' channel(s) from '+fromthis+' to '+tothis)
        ia2.open(tothis)
        try:
            ia2.setrestoringbeam(imagename=fromthis)
        except Exception as e:
            casalog.post('Error while copying restoringbeam: '+str(e), 'WARN')
        finally:
            ia2.close()


################################################

    def feather_residual(self, int_cube, sd_cube, joint_cube, applypb, inparm):

        if applypb==True:
            ## Take initial INT_dirty image to flat-sky. 
            self.modify_with_pb(inpcube=int_cube+'.residual',
                                pbcube=int_cube+'.pb',
                                cubewt=int_cube+'.sumwt',
                                chanwt=inparm['chanwt'],
                                action='div',
                                pblimit=inparm['pblimit'],
                                freqdep=True)
            
        ## Feather flat-sky INT dirty image with SD image
        self.feather_int_sd(sdcube=sd_cube+'.residual',
                            intcube=int_cube+'.residual',
                            jointcube=joint_cube+'.residual', ## output
                            sdgain=inparm['sdgain'],
                            dishdia=inparm['dishdia'],
                            usedata=inparm['usedata'],
                            chanwt = inparm['chanwt'])

        if applypb==True:
            if inparm['specmode'].count('cube')>0:
                ## Multiply the new JOINT dirty image by the frequency-dependent PB. 
                fdep_pb = True
            else:
                ## Multiply new JOINT dirty image by a common PB to get the effect of conjbeams. 
                fdep_pb = False
            self.modify_with_pb(inpcube=joint_cube+'.residual',
                                pbcube=int_cube+'.pb',
                                cubewt=int_cube+'.sumwt',
                                chanwt=inparm['chanwt'],
                                action='mult',
                                pblimit=inparm['pblimit'],
                                freqdep=fdep_pb)

            
################################################

    def feather_int_sd(self, sdcube='', intcube='', jointcube='',sdgain=1.0, dishdia=-1, usedata='sdint', chanwt=''): 
        """
        Run the feather task to combine the SD and INT Cubes. 
        
        There's a bug in feather for cubes. Hence, do each channel separately.
        FIX feather and then change this. CAS-5883 is the JIRA ticket that contains a fix for this issue.... 

        TODO : Add the effdishdia  usage to get freq-indep feathering.

        """
         
        ### Do the feathering.
        if usedata=='sdint':
            ## Feather runs in a loop on chans internally, but there are issues with open tablecache images
            ## Also, no way to set effective dish dia separately for each channel.
            #feather(imagename = jointcube, highres = intcube, lowres = sdcube, sdfactor = sdgain, effdishdiam=-1)

            freqlist = self.getFreqList(sdcube)
            
            os.system('rm -rf '+jointcube)
            os.system('cp -r ' + intcube + ' ' + jointcube)
            
            _ib = image()
            
            _ia.open(jointcube)
            _ia.set(0.0) ## Initialize this to zero for all planes

            for i in range(len(freqlist)):	
                if chanwt[i] != 0.0 : ## process only the nonzero channels
                    if(dishdia <=0):
                        casalog.post('Parameter dishdia (SD dish diameter in meters) must be > 0.', 'SEVERE')

                    freqdishdia = dishdia ## * (freqlist[0] / freqlist[i]) # * 0.5
                
                    self.deleteTmpFiles()
                    self.createplaneimage(imagename=sdcube, outfile=self.tmpsdplane, chanid = str(i));
                    self.createplaneimage(imagename=intcube, outfile=self.tmpintplane, chanid = str(i));

                    #feather(imagename = self.tmpjointplane, highres = self.tmpintplane, lowres = self.tmpsdplane, sdfactor = sdgain, effdishdiam=freqdishdia)
                    # feathering via toolkit
                    try: 
                        casalog.post("start Feathering.....")
                        imFea=imager( )
                        imFea.setvp(dovp=True)
                        imFea.setsdoptions(scale=sdgain)
                        imFea.feather(image=self.tmpjointplane, highres=self.tmpintplane, lowres=self.tmpsdplane, effdishdiam=freqdishdia)
                        imFea.done( )
                        del imFea
                    except Exception as instance:
                        casalog.post('*** Error *** %s' % instance, 'ERROR')
                        raise 

                    _ib.open(self.tmpjointplane)
                    pixjoint = _ib.getchunk()
                    _ib.close()
                    _ia.putchunk(pixjoint, blc=[0,0,0,i])
            
            _ia.close()

        if usedata=='sd': ## Copy sdcube to joint.
            os.system('rm -rf '+jointcube)
            os.system('cp -r ' + sdcube + ' ' + jointcube)
        elif usedata=='int': ## Copy intcube to joint
            os.system('rm -rf '+jointcube)
            os.system('cp -r ' + intcube + ' ' + jointcube)

################################################
    def calc_renorm(self, intname='', jointname=''):
        """
        Calculate a new .sumwt spectrum containing the peak of the feathered PSF.
        The PSF and each residual image calculation will be re-normalized by this.
        This will keep the PSFs in all channels at a peak of 1.
        """
        psfname = jointname+'.psf'
        os.system('cp -r '+intname+'.sumwt ' + jointname + '.sumwt')
        _ia.open(jointname+'.sumwt')
        vals = _ia.getchunk()
        shp = _ia.shape()
        freqaxis_index = self.getFreqAxisIndex(_ia)
        _ia.close()

        if shp[0]>1:
            casalog.post("WARNING : Cannot use this task with faceting", 'WARN')

        _ia.open(jointname+'.psf')
        for i in range(0, shp[freqaxis_index]):
            onepsf = _ia.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])
            vals[0,0,0,i] = np.max(onepsf)
        _ia.close()

        _ia.open(jointname+'.sumwt')
        _ia.putchunk(vals)
        _ia.close()

        casalog.post("********************Re-norm with "+str(vals))


################################################

    def apply_renorm(self, imname='', sumwtname=''):
        """
        Divide each plane of the input image by the sumwt value for that channel
        """
        _ia.open(sumwtname)
        shp = _ia.shape()
        freqaxis_index = self.getFreqAxisIndex(_ia)
        vals = _ia.getchunk()   ## This is one pixel per channel.
        _ia.close()
        
        casalog.post("******************** Re-norm with "+str(vals))

        _ia.open(imname)
        for i in range(0, shp[freqaxis_index]):
            oneplane = _ia.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])
            if vals[0,0,0,i]>0.0:
                normplane = oneplane/vals[0,0,0,i]
            else:
                normplane = oneplane.copy()
                normplane.fill(0.0)
            _ia.putchunk( normplane , blc=[0,0,0,i] )
        _ia.close()
        


################################################

    def modify_with_pb(self, inpcube='', pbcube='',cubewt='', chanwt='', action='mult',pblimit=0.2, freqdep=True):
        """
        Multiply or divide by the PB

        Args:
          inpcube: The cube to be modified. For example: "try.int.cube.model"
          pbcube: The primary beam to multiply/divide by. For example: "try.int.cube.pb"
          cubewt: The per-channel weight of the inpcube. For example: "try.int.cube.sumwt"
          chanwt: List of 0s and 1s, one per channel, to effectively disable the effect of a channel on the resulting images.
          action: 'mult' or 'div', to multiply by the PB or divide by it.
          pblimit: For pixels less than this value in the PB, set those same pixels in the inpcube to zero.
          freqdep: True for channel by channel, False to use a freq-independent PB from the middle of the list before/after deconvolution
        """
        casalog.post('Modify with PB : ' + action + ' with frequency dependence ' + str(freqdep))

        freqlist = self.getFreqList(inpcube)

        _ia.open(inpcube)
        shp=_ia.shape()
        freqaxis_index = self.getFreqAxisIndex(_ia)
        _ia.close()

        if(freqaxis_index!=3):
            casalog.post('The Frequency axis index of '+inpcube+' is '+str(freqaxis_index)+' but modify_with_pb requires index 3.', 'SEVERE')
        
        ##############
        ### Calculate a reference Primary Beam
        ### Weighted sum of pb cube

        ##midchan = int(len(freqlist)/2)
        ##refchan = len(freqlist)-1   ## This assumes ascending frequency ordering in chans.
        refchan=0
        _ia.open(pbcube)
        pbplane = _ia.getchunk(blc=[0,0,0,refchan],trc=[shp[0],shp[1],0,refchan])
        _ia.close()
        pbplane.fill(0.0)

#        pbplane = np.zeros( (shp[0],shp[1]), 'float')

        if freqdep==False:
            _ia.open(cubewt) # .sumwt
            cwt = _ia.getchunk()[0,0,0,:]
            _ia.close()

            if shp[3] != len(cwt) or len(freqlist) != len(cwt):
                raise Exception("Modify with PB : Nchan shape mismatch between cube and sumwt.")

            cwt = cwt * chanwt  ## Merge the weights and flags

            sumchanwt = np.sum(cwt)

            if sumchanwt==0:
                raise Exception("Weights are all zero ! ")
                
            _ia.open(pbcube)
            for i in range(len(freqlist)):
                ## Read the pb per plane
                pbplane = pbplane + cwt[i] * _ia.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])
            _ia.close()
                
            pbplane = pbplane / sumchanwt

        ##############


        ## Special-case for setting the PBmask to be same for all freqs
        if freqdep==False:
            shutil.copytree(pbcube, pbcube+'_tmpcopy')

        for i in range(len(freqlist)):

            ## Read the pb per plane
            if freqdep==True:
                _ia.open(pbcube)
                pbplane = _ia.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])
                _ia.close()

            ## Make a tmp pbcube with the same pb in all planes. This is for the mask.
            if freqdep==False:
                _ia.open(pbcube+'_tmpcopy')
                _ia.putchunk(pbplane, blc=[0,0,0,i])
                _ia.close()

            _ia.open(inpcube)
            implane = _ia.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])

            outplane = pbplane.copy()
            outplane.fill(0.0)

            if action=='mult':
                pbplane[pbplane<pblimit]=0.0
                outplane = implane * pbplane
            else:
                implane[pbplane<pblimit]=0.0
                pbplane[pbplane<pblimit]=1.0
                outplane = implane / pbplane

            _ia.putchunk(outplane, blc=[0,0,0,i])
            _ia.close()

#        if freqdep==True:
#            ## Set a mask based on frequency-dependent PB
#            self.addmask(inpcube,pbcube,pblimit)
#        else:
        if freqdep==False:
            ## Set a mask based on the PB in refchan
            self.addmask(inpcube,pbcube+'_tmpcopy',pblimit)
            shutil.rmtree(pbcube+'_tmpcopy')
            

################################################
    def addmask(self, inpimage='',pbimage='',pblimit=0.2, mode='replace'):
    #def addmask(self, inpimage='',pbimage='',pblimit=0.2, mode='add'):
    #def addmask(self, inpimage='',pbimage='',pblimit=0.2, mode='old'):
        """
        add pb mask: create a new mask called 'pbmask' and set it as a defualt mask 
        mode: "replace" or "add"
              relpalce: create a pbmask based on pblimit without account for the exist mask
              add: create a pbmask based on pblimit and merge with existing default mask 
        """
        _ia.open(inpimage)
        defaultmaskname=_ia.maskhandler('default')[0]
        allmasknames = _ia.maskhandler('get')
        # casalog.post("defaultmaskname=",defaultmaskname)
        if mode=='replace':
            if defaultmaskname!='' and defaultmaskname!='mask0':
                _ia.calcmask(mask='"'+pbimage+'"'+'>'+str(pblimit), name=defaultmaskname);

            elif defaultmaskname=='mask0':
                if 'pbmask' in allmasknames:
                    _ia.maskhandler('delete','pbmask')
                _ia.calcmask(mask='"'+pbimage+'"'+'>'+str(pblimit), name='pbmask');

        #elif mode=='add':
        # After deleting a pixel mask it sometimes leaves it in cache 
        #  
        #    _ia.open(inpimage)
        #    if defaultmaskname=='pbmask':
        #        _ia.maskhandler('delete',defaultmaskname)
        #        _ia.close()
        #        _ia.open(inpimage)

        #    _ia.calcmask(mask='mask("'+inpimage+'")||'+'"'+pbimage+'"'+'>'+str(pblimit), name='pbmask');
        elif mode=='old':
            # this one create a new mask every time this function is called!
            #_ia.open(inpimage)
            _ia.calcmask(mask='mask("'+inpimage+'")||'+'"'+pbimage+'"'+'>'+str(pblimit));
        else:
            raise Exception("Unrecongnized value for mode: ",mode)
        _ia.close()
        _ia.done() 

################################################
    def cube_to_taylor_sum(self, cubename='', cubewt='', chanwt='', mtname='',reffreq='1.5GHz',nterms=2,dopsf=False):
        """
        Convert Cubes (output of major cycle) to Taylor weighted averages (inputs to the minor cycle)
        Input : Cube image <cubename>, with channels weighted by image <cubewt>
        Output : Set of images : <mtname>.tt0, <mtname>.tt1, etc...
        Algorithm: I_ttN = sum([   I_v * ((f-ref)/ref)**N   for f in freqs   ])

        Args:
          cubename: Name of a cube image to interpret into a set of taylor term .ttN images, eg "try.residual", "joint.cube.psf".
          cubewt: Name of a .sumwt image that contains the per-channel weighting for the interferometer image.
          chanwt: List of 0s and 1s, one per channel, to effectively disable the effect of a channel on the resulting images.
          mtname: The prefix output name, to be concatenated with ".ttN" strings, eg "try_mt.residual", "joint.multiterm.psf"
                  These images should already exist by the time this function is called.
                  It's suggested that this have same suffix as cubename.
          dopsf: Signals that cubename represents a point source function, should be true if cubename ends with ".psf".
                 If true, then output 2*nterms-1 ttN images.
        """

        refnu = _qa.convert( _qa.quantity(reffreq) ,'Hz' )['value']

        # casalog.post("&&&&&&&&& REF FREQ : " + str(refnu))

        pix=[]

        num_terms=nterms

        if dopsf==True:
            num_terms=2*nterms-1
 
        for tt in range(0,num_terms):
            _ia.open(mtname+'.tt'+str(tt))
            pix.append( _ia.getchunk() )
            _ia.close()
            pix[tt].fill(0.0)

        _ia.open(cubename)
        shp = _ia.shape()
        freqaxis_index = self.getFreqAxisIndex(_ia)
        _ia.close()

        if(freqaxis_index!=3):
            casalog.post('The Frequency axis index of '+cubename+' is '+str(freqaxis_index)+' but cube_to_taylor_sum requires index 3.', 'SEVERE')
        
        _ia.open(cubewt)
        cwt = _ia.getchunk()[0,0,0,:]
        _ia.close()


        freqlist = self.getFreqList(cubename)

        if shp[3] != len(cwt) or len(freqlist) != len(cwt):
            raise Exception("Nchan shape mismatch between cube and sumwt.")

        cwt = cwt * chanwt  ## Merge the weights and flags. 

        sumchanwt = np.sum(cwt)  ## This is a weight

        if sumchanwt==0:
            raise Exception("Weights are all zero ! ")
        else:

            _ia.open(cubename)
            for i in range(len(freqlist)):
                wt = (freqlist[i] - refnu)/refnu
                implane = _ia.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])
                for tt in range(0,num_terms):
                    pix[tt] = pix[tt] + (wt**tt) * implane * cwt[i]
            _ia.close()
            
            for tt in range(0,num_terms):
                pix[tt] = pix[tt]/sumchanwt
#        ia.close()

        for tt in range(0,num_terms):
            _ia.open(mtname+'.tt'+str(tt))
            _ia.putchunk(pix[tt])
            _ia.close()

################################################
    def taylor_model_to_cube(self, cubename='', mtname='',reffreq='1.5GHz',nterms=2):
        """
        Convert Taylor coefficients (output of minor cycle) to cube (input to major cycle)
        Input : Set of images with suffix : .tt0, .tt1, etc...
        Output : Cube
        """

        if not os.path.exists(cubename+'.model'):
            shutil.copytree(cubename+'.psf', cubename+'.model')
            _ia.open(cubename+'.model')
            _ia.set(0.0)
            _ia.setrestoringbeam(remove=True)
            _ia.setbrightnessunit('Jy/pixel')
            _ia.close()


        refnu = _qa.convert( _qa.quantity(reffreq) ,'Hz' )['value']

        pix=[]

        for tt in range(0,nterms):
            _ia.open(mtname+'.model.tt'+str(tt))
            pix.append( _ia.getchunk() )
            _ia.close()

        _ia.open(cubename+'.model')
        shp = _ia.shape()
        _ia.close()

        implane = pix[0].copy()

        freqlist = self.getFreqList(cubename+'.psf')
        _ia.open(cubename+'.model')
        for i in range(len(freqlist)):
            wt = (freqlist[i] - refnu)/refnu
            implane.fill(0.0)
            for tt in range(0,nterms):
                implane = implane + (wt**tt) * pix[tt]
            _ia.putchunk(implane, blc=[0,0,0,i])
        _ia.close()

##################################################


    def calc_sd_residual(self,origcube='', modelcube = '', residualcube = '', psfcube=''):

        """
        Residual = Original - ( PSF * Model )
        """

        ia_orig = image()
        ia_model = image()
        ia_psf = image()
        ia_res = image()

        ia_orig.open(origcube)

        shp = ia_orig.shape()
        freqaxis_index = self.getFreqAxisIndex(ia_orig)

        if(freqaxis_index!=3):
            ia_orig.close()
            casalog.post('The Frequency axis index of '+origcube+' is '+str(freqaxis_index)+' but calc_sd_residual requires index 3.', 'SEVERE')

        ia_model.open(modelcube)
        ia_psf.open(psfcube)
        ia_res.open(residualcube)

        for i in range(0,shp[freqaxis_index]): # loop over all channels

            im_orig = ia_orig.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])

            im_model = ia_model.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])

            im_psf = ia_psf.getchunk(blc=[0,0,0,i],trc=[shp[0],shp[1],0,i])

            smoothedim = self.myconvolve(im_model[:,:,0,0], im_psf[:,:,0,0])

            if( np.nansum(im_orig)==0.0):
                smoothedim.fill(0.0)

            im_residual=im_psf.copy() ## Just to init the shape of this thing
            im_residual[:,:,0,0] = im_orig[:,:,0,0] - smoothedim

            ia_res.putchunk(im_residual, blc=[0,0,0,i])

        ia_orig.close()
        ia_model.close()
        ia_psf.close()
        ia_res.close()

##################################################

    def myconvolve(self,im1,im2):
        
        t3 = time.time()
        
        shp = im1.shape
        pshp = (shp[0]*2, shp[1]*2)
        pim1 = np.zeros(pshp,'float')
        pim2 = np.zeros(pshp,'float')
        
        pim1[shp[0]-shp[0]//2 : shp[0]+shp[0]//2, shp[1]-shp[1]//2 : shp[1]+shp[1]//2] = im1
        pim2[shp[0]-shp[0]//2 : shp[0]+shp[0]//2, shp[1]-shp[1]//2 : shp[1]+shp[1]//2] = im2
        
        fftim1 = fftpack.fftshift( fftpack.fft2( fftpack.ifftshift( pim1 ) ) )
        fftim2 = fftpack.fftshift( fftpack.fft2( fftpack.ifftshift( pim2 ) ) )
        fftprod = fftim1*fftim2
        psmoothedim = np.real(fftpack.fftshift( fftpack.ifft2( fftpack.ifftshift( fftprod ) ) ) )
        
        smoothedim = psmoothedim[shp[0]-shp[0]//2 : shp[0]+shp[0]//2, shp[1]-shp[1]//2 : shp[1]+shp[1]//2]
        
        return smoothedim

##########################################

    def regridimage(self, imagename, template, outfile):
        outia = None
        _myia = image()
        _myia.open(template)
        csys = _myia.coordsys()
        shape = _myia.shape()
        _myia.done()

        _myia.open(imagename)
        myshape = _myia.shape()
        if len(myshape)!=len(shape):
            raise Exception("Image "+imagename+" and template image "+template+" have different number of axes: "
                            +str(len(myshape))+" and "+str(len(shape))+" .")

        mysummary = _myia.summary(list=False)
        extractStokes = False

        for i in [2,3]:
            if len(myshape)>i:
                if myshape[i]!=shape[i]:
                    casalog.post("Image "+imagename+" and template image "+template+" have different shape in axis "
                                 +str(i)+" ("+mysummary['axisnames'][i]+"): "+str(myshape[i])+" and "+str(shape[i])+" .", 'WARN')
                    if mysummary['axisnames'][i] == 'Stokes' and myshape[i]>1 and shape[i]==1:
                        extractStokes = True
        try:
            if extractStokes:
                casalog.post("Will try to continue by extracting Stokes I from "+imagename+" ...", 'WARN')
                tmpimage = 'tmp_'+self.tmpFileTag+'_'+imagename+'_StokesIOnly'
                tmp_csys = _myia.coordsys()
                myrg = regionmanager()
                xregion = myrg.frombcs(csys=tmp_csys.torecord(), shape=myshape, stokes='I', stokescontrol="a")
                tmp_csys.done()                
                _myia.subimage(outfile=tmpimage, region=xregion, dropdeg=False, overwrite=True, stretch=False, keepaxes=[])
                _myia.close()
                casalog.post("Success. Created "+tmpimage, 'INFO')
                _myia.open(tmpimage)
                
            outia=_myia.regrid(outfile=outfile, 
                   shape=shape,
                   csys=csys.torecord(),
                               axes=[0,1],
                   overwrite=True,
                   asvelocity=False)
            
        except Exception as instance:
            casalog.post("Error while regridding image \'"+imagename+"\':", 'WARN')
            casalog.post("*** \'%s\'" % (instance), 'WARN')
            raise

        finally:
            csys.done()
            if outia != None and outia.isopen():
                outia.done()
            _myia.done()

 
##########################################

    def createplaneimage(self,imagename, outfile, chanid):
        """
        extract a channel plane image 
        """
        _tmpia=image()
        _tmprg=regionmanager()
        outia=None

        _tmpia.open(imagename)
        theregion = _tmprg.frombcs(csys=_tmpia.coordsys().torecord(), shape=_tmpia.shape(), chans=chanid) 
        try:
            outia=_tmpia.subimage(outfile=outfile, region=theregion)
        except Exception as instance:
            casalog.post("*** Error \'%s\' in creating subimage" % (instance), 'WARN')

        _tmpia.close()
        _tmpia.done()
        _tmprg.done()
        if outia != None and outia.isopen():
            outia.done()
     
    def pbcor(self, imagename, pbimage, cutoff, outfile):
        """
        pb-correction 
        """  
        outia=None
        _myia=image()
        _myia.open(imagename)

        try:
            outia = _myia.pbcor(pbimage=pbimage, outfile=outfile, overwrite=True,
                          mode='divide', cutoff=cutoff)
        except Exception as instance:
            casalog.post("*** Error \'%s\' in creating pb-corrected image" % (instance), 'WARN')

        finally:
            _myia.done()
            if outia != None and outia.isopen():
                outia.done()

 
    def checkpsf(self, inpsf, refpsf):
        """
        check the center of psf if diffent for 
        refpsf center and (shift to refpsf position)
        in returned psf
        """    
        tol=0.001
        allowshift=True
        _ia.open(inpsf)
        incsys  = _ia.coordsys().torecord()
        _ia.close()
        #_ia.done()
        _tmpia = image()
        _tmpia.open(refpsf)
        refcsys = _tmpia.coordsys().torecord()
        _tmpia.close() 
        #_tmpia.done() 
        # check the field center
        ramismatch = False
        decmismatch = False

        indir = incsys['direction0']
        refdir = refcsys['direction0']

        diff_ra = indir['crval'][0] - refdir['crval'][0]
        diff_dec = indir['crval'][1] - refdir['crval'][1]

        if diff_ra/refdir['crval'][0] > tol:
            ramismatch = True
        if diff_dec/refdir['crval'][1] > tol:
            decmismatch = True
        if ramismatch or decmismatch:
            casalog.post("The position of SD psf is different from the the psf by (diffRA,diffDec)=( %s, %s)." % (diff_ra, diff_dec)
,'WARN')    
            if allowshift:
                modsdpsf=inpsf+'_mod'
                casalog.post("Modifying the input SD psf, "+inpsf+" by shifting the field center of sd psf to that of int psf. Modified SD psf image:"+modsdpsf)
                shutil.copytree(inpsf, inpsf+'_mod')
                _ia.open(modsdpsf)
                thecsys = _ia.coordsys()
                themodcsysrec = thecsys.torecord()
                #repalcing ra, dec of the sd psf to those of the int psf
                themodcsysrec['direction0']['crval'][0] = refdir['crval'][0]
                themodcsysrec['direction0']['crval'][1] = refdir['crval'][1]
                thecsys.fromrecord(themodcsysrec)
                _ia.setcoordsys(thecsys)
                _ia.close()
                #_ia.done()
            else:
                raise Exception("the center of the psf different from the int psf by (diffRA, diffDec)=(%s,%s)" % (diff_ra, diff_dec))

        else:
            casalog.post(" The center of psf coincides with int psf: (diffRA,diffDec)=( %s, %s)" % (diff_ra, diff_dec))            

        #### check for frequency axis
        _ia.open(inpsf)
        sdshape = _ia.shape()
        freqaxis_index1 = self.getFreqAxisIndex(_ia)
        _ia.close()
        _ia.open(refpsf)
        tshape = _ia.shape()
        freqaxis_index2 = self.getFreqAxisIndex(_ia)
        _ia.close()
        if freqaxis_index1 != freqaxis_index2 or sdshape[freqaxis_index1] != tshape[freqaxis_index1]:
            raise Exception("The frequency axis of the input SD image and the interferometer template do not match and cannot be regridded. This is because when there are per-plane restoring beams, a regrid along the frequency axis cannot be defined at optimal accuracy. Please re-evaluate the SD image and psf onto a frequency grid that matches the interferometer frequency grid, and then retry.")

        #return modpsf 

    def create_sd_psf(self, sdimage, sdpsfname ):
        """
        If sdpsf="", create an SD_PSF cube using restoringbeam information from the sd image. 
        Start from the regridded SD_IMAGE cube
        """
        sdintlib = SDINT_helper()
             
        ia2 = image()
        _cl = componentlist()
        _rg = regionmanager()

        ## Get restoringbeam info for all channels
        ia2.open(sdimage)
        restbeams = ia2.restoringbeam()
        shp = ia2.shape()
        try:
            mysummary = ia2.summary(list=False)
            freqaxis_index = list(mysummary['axisnames']).index('Frequency')
        except(ValueError):
            ia2.close()
            casalog.post('The SD image has no frequency axis. Try adding one with ia.adddegaxis() .', 'SEVERE') 
        try:
            stokesaxis_index = list(mysummary['axisnames']).index('Stokes')
            nstokes = shp[stokesaxis_index]
        except(ValueError):
            casalog.post('The SD image has no Stokes axis.', 'WARN') 
            nstokes = 1
            
        csys = ia2.coordsys()
        ia2.close()

        # Handle images without per-plane restoring beams
        if not 'nChannels' in restbeams or restbeams['nChannels'] != shp[freqaxis_index]:
            casalog.post("The input SD image does not have per-plane-restoring beams. Working around that ...", 'WARN')

            if shp[freqaxis_index] == 1: # If there is only one channel, just use the one beam we have
                mybeams = {'beams': {'*0': {'*0': restbeams.copy()}}, 'nChannels':1, 'nStokes': nstokes}
                restbeams = mybeams
            elif shp[freqaxis_index] > 1: # create a copy of the SD image with per-plane restoring beams
                casalog.post("Constructing per-plane restoring beams based on "+sdimage, 'WARN')
                ia2.open(sdimage)
                ia2.setrestoringbeam(remove=True)
                ia2.setrestoringbeam(beam=restbeams, channel=0, polarization=-1)
                restbeams =  ia2.restoringbeam()
                ia2.close()
            else:
                casalog.post('The SD image has a frequency axis of length < 1. Cannot proceed.', 'SEVERE')
                
        cdir = csys.torecord()['direction0']
        compdir = [cdir['system'] , str(cdir['crval'][0])+cdir['units'][0] , str(cdir['crval'][1])+cdir['units'][1] ]

        ## Make empty SD psf cube from SD image cube
        os.system('rm -rf '+sdpsfname)
        os.system('cp -R '+sdimage+' '+sdpsfname)
        
        ## Iterate through PSF cube and replace pixels with Gaussians matched to restoringbeam info

        ia2.open(sdpsfname)
        for ch in range(0,shp[freqaxis_index]):
            os.system('rm -rf '+self.tmpsdplane)
            rbeam = restbeams['beams']['*'+str(ch)]['*0']
            
            _cl.close()
            _cl.addcomponent(flux=1.0, fluxunit='Jy',polarization='Stokes', dir=compdir, 
                            shape='Gaussian', majoraxis=rbeam['major'], 
                        minoraxis=rbeam['minor'], positionangle=rbeam['positionangle'],
                        spectrumtype='constant') #, freq=str(freqs[ch])+'Hz')


            implane = ia2.getchunk(blc=[0,0,0,ch],trc=[shp[0],shp[1],0,ch])
            implane.fill(0.0)
            ia2.putchunk(implane, blc=[0,0,0,ch])
            ia2.modify(model=_cl.torecord(), subtract=False, region=_rg.box(blc=[0,0,0,ch],trc=[shp[0],shp[1],0,ch]))
            ## Now, normalize it.
            implane = ia2.getchunk(blc=[0,0,0,ch],trc=[shp[0],shp[1],0,ch])
            pmax = np.max(implane)
            #print(pmax)
            if pmax>0.0:
                implane = implane/pmax
            else:
                implane.fill(0.0)
            ia2.putchunk(implane, blc=[0,0,0,ch])

        ia2.close()
            

    def check_coords(self, intres='', intpsf='', intwt = '', sdres='', sdpsf='',sdwt = '', pars=None):
        """
        ### (1) Frequency range of cube, data selection range. mtmfs reffreq.
        ### (2) nchan too small or too large
        ### (3) sumwt : flagged channels in int cubes
        ### (4) sd cube empty channels ? Weight image ? 
        """
        validity=True

        freqlist = self.getFreqList(intres)
        chanwt = np.ones( len(freqlist), 'float')
        if pars['usedata']=='int':
            pars['chanwt'] = chanwt
            return validity, pars
        
        ## get shapes and gather stats
        _ia.open(intres)
        int_shp = _ia.shape()
        int_stat = _ia.statistics(axes=[0,1])
        _ia.close()

        _ia.open(sdres)
        sd_shp = _ia.shape()
        sd_stat = _ia.statistics(axes=[0,1])
        _ia.close()

        _ia.open(intwt)
        sumwt = _ia.getchunk()
        _ia.close()

            
        ### For mtmfs minor cycle only
        if pars['specmode'] in ['mfs','cont'] and pars['deconvolver']=='mtmfs':
            ##casalog.post('DOING EXTRA CHECKS##############','WARN')
            #(1) # Check reference frequency w.r.to cube freq range. 
            if pars['reffreq']=='':
                reffreq =str( ( freqlist[0] + freqlist[ len(freqlist)-1 ] )/2.0 ) + 'Hz'
                casalog.post('The reference frequency for MFS is calculated as the middle of the cube frequency range, irrespective of flagged channels : '+reffreq,'INFO', "task_sdintimaging")
                ## Modified parameters : 
                pars['reffreq'] = reffreq
            else:
                refval = _qa.convert(_qa.quantity( pars['reffreq'] ), 'Hz') ['value']
                if refval < freqlist[0] or refval >  freqlist[ len(freqlist)-1 ] :
                    if len(freqlist)>1:
                        casalog.post('The specified reffreq for MFS imaging ('+str(refval)+' Hz) is outside the frequency range of the specified Cube image for the major cycle ('+str(freqlist[0])+' Hz - '+str(freqlist[ len(freqlist)-1 ])+' Hz).\n Please specify a reffreq within the cube frequency range or leave it as an empty string to auto-calculate the middle of the range.','WARN', "task_sdintimaging")
                        validity=False
                    else:
                        casalog.post('The specified reffreq for MFS imaging ('+str(refval)+' Hz) is not exactly the same as the frequency of the selected interferometric data for the major cycle ('+str(freqlist[0])+' Hz).\n We will ignore this for now.', 'WARN')
                        

            #(2.1)# Too many channels
            if len(freqlist) > 50:
                casalog.post('The cube for major cycles has '+str(len(freqlist))+' channels.  For wideband continuum imaging, it may be possible to reduce the number of channels to (say) one per spectral window to preserve frequency dependent intensity and weight information but also minimize the number of channels in the image cubes. MFS imaging will be performed within each channel. This will reduce the sizes of the image cubes as well as the compute time used for feathering each plane separately. Note that a minimum of nterms=' + str(pars['nterms']) + ' channels is required for an accurate polynomial fit, but where possible at least 5 to 10 channels that span the frequency range are prefered in order to properly encode frequency dependent intensity and weights.', "WARN", "task_sdintimaging")

            #(2.2)# Too few channels        
            if len(freqlist) < 5 and pars['nterms'] > 1 :
                casalog.post('The cube for the major cycle has only '+str(len(freqlist))+' channels. A minimum of nterms = ' + str(pars['nterms']) + ' channels is required for an accurate polynomial fit, but where possible at least 5 to 10 channels that span the frequency range are prefered in order to properly encode frequency dependent intensity and weights.','WARN', "task_sdintimaging")
                if len(freqlist) < pars['nterms']:
                    validity=False

        ### For both cube and mtmfs 
        #(3) ## If there are channels filled with zeros.... create a chanflag to use during 'cube_to_taylor' and 'feathering' 

        ## INT : If some chans are zero, check that sumwt reflects it too. 
        zerochans =  np.count_nonzero( int_stat['sum']==0.0 )
        if zerochans>0:
            casalog.post('There are '+str(zerochans)+' empty channels in the interferometer cube. These channels will be excluded from the feathering step.')
            chanwt[ int_stat['sum']==0.0 ] = 0.0

        ## SD : If some chans are zero. 
        ## Set the wt to zero and use the logical AND of int_wt and sd_wt for feathering?
        zerochans =  np.count_nonzero( sd_stat['sum']==0.0 )
        if zerochans>0:
            casalog.post('There are '+str(zerochans)+' empty channels in the single dish image cube. These channels will be excluded from the feathering step. NOTE : We do not yet use SD weights. ')
            chanwt[ sd_stat['sum']==0.0 ] = 0.0

        ### If there are channels to flag.... list them. 
        if np.count_nonzero( chanwt==0.0 ):
            casalog.post('The following channel weights/flags will be used in the feather step and minor cycle. Zero indicates channels that are empty in either the INT or SD input cubes and which will be excluded from the joint reconstruction. : ' + str(chanwt), 'INFO') 
            casalog.post('There are channels that are filled with zeros either in the INT cube or the SD cube or both, and they will be ignored from the joint reconstruction. Please search the log file for the string "channel weights/flags" to find a listing of channels that are being used','WARN')


        if np.count_nonzero( chanwt != 0.0 ) == 0:
            casalog.post("There are no channels with data in both the INT and the SD cubes. Cannot proceed","WARN")
            validity=False

        pars['chanwt'] = chanwt
        return validity, pars


    def setup_cube_params(self,sdcube=''):
        """
        Read coordinate system from the SD cube
        Decide parameters to input into sdintimaging for the INT cube to match. 

        This is a helper method, not currently used in the sdintimaging task.
        We will add this later (after 6.1), and also remove some parameters from the task level.
        """
        _ia.open(sdcube)
        csys = _ia.coordsys()
        shp = _ia.shape()
        ctypes = csys.axiscoordinatetypes()
        casalog.post("Shape of SD cube : "+str(shp))
        casalog.post("Coordinate ordering : "+str(ctypes))
        if len(ctypes) !=4 or ctypes[3] != 'Spectral':
            casalog.post("The SD cube needs to have 4 axes, in the RA/DEC/Stokes/Spectral order", 'ERROR')
            _ia.close()
            return False
        nchan = shp[3]
        start = str( csys.referencevalue()['numeric'][3] ) + csys.units()[3]
        width = str( csys.increment()['numeric'][3]) + csys.units()[3] 
        ## Number of channels
        casalog.post("nchan = "+str(nchan))
        ## Start Frequency
        casalog.post("start = " + start  )
        ## Width
        casalog.post("width = " + width  )
        ## Test for restoringbeams
        rbeams = _ia.restoringbeam()
        #if not rbeams.has_key('nChannels') or rbeams['nChannels']!= shp[3]:
        if not 'nChannels' in rbeams or rbeams['nChannels']!= shp[3]:
            casalog.post("The SD Cube needs to have per-plane restoringbeams", 'ERROR')
            _ia.close()
            return False
        else:
            casalog.post("Found " + str(rbeams['nChannels']) + " per-plane restoring beams")
        casalog.post("\n(For specmode='mfs' in sdintimaging, please remember to set 'reffreq' to a value within the freq range of the cube)\n")
        _ia.close()
        return {'nchan':nchan, 'start':start, 'width':width}



    
### Using Old Imager. Does not work for cubes ? 
#    def fit_psf_beam(self,msname = '', psfname =''):
#        _im.open(msname)  
#        _ia.open(psfname)
#        csys = _ia.coordsys()
#        rbeam_old = _ia.restoringbeam()
#        print(rbeam_old)
#        shp = _ia.shape()
#        _ia.close()
#        cellx = csys.increment()['numeric'][0];
#        celly = csys.increment()['numeric'][1];
#        _im.defineimage(nx=shp[0],ny=shp[1],cellx=str(cellx)+'rad',celly=str(celly)+'rad',nchan=3)  
#        params =_im.fitpsf(psfname)
#        print(params)
#        _im.close() 
#
