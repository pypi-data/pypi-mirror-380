import os
import shutil
import string
import copy
import math
import numpy
from typing import Optional, List, Union

from .mstools import write_history
from casatools import table, ms, mstransformer
from casatasks import casalog
from .parallel.parallel_data_helper import ParallelDataHelper

_tb = table()

def hanningsmooth(vis=None, 
                   outputvis=None,
                   keepmms=None,
                   field=None,
                   spw=None, 
                   scan=None, 
                   antenna=None, 
                   correlation=None,
                   timerange=None, 
                   intent=None,
                   array=None,
                   uvrange=None,
                   observation=None,
                   feed=None,
                   smooth_spw : Optional[Union[str,List[int], int]] = None,
                   datacolumn=None, 
                   ):

    """Hanning smooth frequency channel data to remove Gibbs ringing

    """

    casalog.origin('hanningsmooth')
    
    
    # Initiate the helper class    
    pdh = ParallelDataHelper("hanningsmooth", locals()) 

    # Validate input and output parameters
    pdh.setupIO()

    # Input vis is an MMS
    if pdh.isMMSAndNotServer(vis) and keepmms:
        
        if not pdh.validateInputParams():        
            raise Exception('Unable to continue with MMS processing')
                        
        pdh.setupCluster('hanningsmooth')

        # Execute the jobs
        pdh.go()
        return

    mslocal = ms()

    # Actual task code starts here
    try:    
        mtlocal = mstransformer()

        # Gather all the parameters in a dictionary.        
        config = {}
        
        config = pdh.setupParameters(inputms=vis, outputms=outputvis, field=field, 
                    spw=spw, array=array, scan=scan, antenna=antenna, correlation=correlation,
                    uvrange=uvrange,timerange=timerange, intent=intent, observation=observation,
                    feed=feed)
        
        
        # Check if CORRECTED column exists, when requested
        datacolumn = datacolumn.upper()
        if datacolumn == 'CORRECTED':
            _tb.open(vis)
            if 'CORRECTED_DATA' not in _tb.colnames():
                casalog.post('Input CORRECTED_DATA does not exist. Will use DATA','WARN')
                datacolumn = 'DATA'
            _tb.close()
             
        casalog.post('Will use datacolumn = %s'%datacolumn, 'DEBUG')
        config['datacolumn'] = datacolumn
        
        # Call MSTransform framework with hanning=True
        config['hanning'] = True
        # Parse smooth_spw
        smooth_spw_config = []
        if isinstance(smooth_spw, str) :
            if(smooth_spw != '') :
                spw_ranges = smooth_spw.split(',')
                for range in spw_ranges:
                    if range.strip().isdigit() :
                        smooth_spw_config.append(int(range))
                    else :
                        range_str = range.split('~')
                        if (len(range_str) != 2):
                            raise ValueError("smooth_spw must be a list of single SPWs, a str\
ing with comma separated SPWs or SPWs ranges with ~. Cannot parse string as a SPW range: ",range_str)
                        spw_init=range_str[0]
                        spw_end=range_str[1]
                        if(not spw_init.isdigit() or not spw_end.isdigit() ) :
                            raise ValueError("smooth_spw must be a list of single SPWs, a str\
ing with comma separated SPWs or SPWs ranges with ~. Cannot parse range start or end: ",range_str)
                        for i in numpy.arange(int(spw_init), int(spw_end)+1) :
                            smooth_spw_config.append(i)
        else :
            smooth_spw_config.append(smooth_spw)

        if(len(smooth_spw_config) == 0 ) :
            smooth_spw_config = None
        config['smooth_spw'] = smooth_spw_config
        config['reindex'] = False

        # Configure the tool 
        casalog.post('%s'%config, 'DEBUG1')
        mtlocal.config(config)
        
        # Open the MS, select the data and configure the output
        mtlocal.open()
        
        # Run the tool
        casalog.post('Apply Hanning smoothing on data')
        mtlocal.run()        
            
    finally:
        mtlocal.done()

    # Write history to output MS, not the input ms.
    try:
        param_names = hanningsmooth.__code__.co_varnames[:hanningsmooth.__code__.co_argcount]
        local_vars = locals()
        param_vals = [local_vars[p] for p in param_names]
        
        casalog.post('Updating the history in the output', 'DEBUG1')
        write_history(mslocal, outputvis, 'hanningsmooth', param_names,
                      param_vals, casalog)
    except Exception as instance:
        casalog.post("*** Error \'%s\' updating HISTORY" % (instance),'WARN')

    mslocal = None
 
 
