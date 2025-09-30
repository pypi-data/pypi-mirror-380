import numpy as np
import shutil
import os
from io import StringIO
import math, re, sys, logging
from functools import reduce
import time as tm
import datetime as dt
import casatools
msmd = casatools.msmetadata()
tb = casatools.table()

desc = {'ANTENNA_ID': {'comment': 'ID of antenna in this array',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'int'},
 'FEED_ID': {'comment': 'Feed id',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'int'},
 'INTERVAL': {'comment': 'Interval for which this set of parameters is accurate',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {'QuantumUnits': np.array(['s'], dtype='<U1')},
  'maxlen': 0,
  'option': 0,
  'valueType': 'double'},
 'SPECTRAL_WINDOW_ID': {'comment': 'ID for this spectral window setup',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'int'},
 'TIME': {'comment': 'Midpoint of time for which this set of parameters is accurate',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'},
   'QuantumUnits': np.array(['s'], dtype='<U1')},
  'maxlen': 0,
  'option': 0,
  'valueType': 'double'},
 'TSYS': {'comment': 'System temp. for each of the two receptors',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {'QuantumUnits': np.array(['K'], dtype='<U1')},
  'maxlen': 0,
  'ndim': -1,
  'option': 0,
  'valueType': 'float'},
 '_define_hypercolumn_': {},
 '_keywords_': {},
 '_private_keywords_': {}}
dminfo = {'*1': {'COLUMNS': np.array(['ANTENNA_ID', 'FEED_ID', 'INTERVAL', 'SPECTRAL_WINDOW_ID', 'TIME',
         'TSYS'], dtype='<U18'),
  'NAME': 'StandardStMan',
  'SEQNR': 0,
  'SPEC': {'BUCKETSIZE': 1152,
   'IndexLength': 7486,
   'MaxCacheSize': 2,
   'PERSCACHESIZE': 2},
  'TYPE': 'StandardStMan'}}
desc_gc = {'ANTENNA_ID': {'comment': 'Antenna identifier',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'int'},
 'FEED_ID': {'comment': 'Feed identifier',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'int'},
 'GAIN': {'comment': 'Gain polynomial',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'ndim': -1,
  'option': 0,
  'valueType': 'float'},
 'INTERVAL': {'comment': 'Interval for which this set of parameters is accurate',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {'QuantumUnits': np.array(['s'], dtype='<U1')},
  'maxlen': 0,
  'option': 0,
  'valueType': 'double'},
 'NUM_POLY': {'comment': 'Number of terms in polynomial',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'int'},
 'SENSITIVITY': {'comment': 'Antenna sensitivity',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {'QuantumUnits': np.array(['K/Jy'], dtype='<U4')},
  'maxlen': 0,
  'ndim': -1,
  'option': 0,
  'valueType': 'float'},
 'SPECTRAL_WINDOW_ID': {'comment': 'Spectral window identifier',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'int'},
 'TIME': {'comment': 'Midpoint of time for which this set of parameters is accurate',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {'MEASINFO': {'Ref': 'UTC', 'type': 'epoch'},
   'QuantumUnits': np.array(['s'], dtype='<U1')},
  'maxlen': 0,
  'option': 0,
  'valueType': 'double'},
 'TYPE': {'comment': 'Gain curve type',
  'dataManagerGroup': 'StandardStMan',
  'dataManagerType': 'StandardStMan',
  'keywords': {},
  'maxlen': 0,
  'option': 0,
  'valueType': 'string'},
 '_define_hypercolumn_': {},
 '_keywords_': {},
 '_private_keywords_': {}}
dminfo_gc = {'*1': {'COLUMNS': np.array(['ANTENNA_ID', 'FEED_ID', 'GAIN', 'INTERVAL', 'NUM_POLY',
         'SENSITIVITY', 'SPECTRAL_WINDOW_ID', 'TIME', 'TYPE'], dtype='<U18'),
  'NAME': 'StandardStMan',
  'SEQNR': 0,
  'SPEC': {'BUCKETSIZE': 1920,
   'IndexLength': 142,
   'MaxCacheSize': 2,
   'PERSCACHESIZE': 2},
  'TYPE': 'StandardStMan'}}

#################################################################################################
# Main task
def appendantab(vis=None, outvis=None, antab=None, 
                overwrite=False, append_tsys=True, append_gc=True):

    # disallow writing to the input vis
    if vis == outvis:
        print("Please provide a path for outvis different to the input vis")
        return
    
    # Require an outvis to be specified
    if not outvis:
        print('Please provide an outvis name to write to')
        return
    
    # get info from vis
    msmd.open(vis)
    ant_names = msmd.antennastations()
    n_band = len(msmd.bandwidths())
    spws = msmd.spwfordatadesc()
    msmd.close()

    # get start time and end time from ms
    tb.open(vis)
    times = tb.getcol('TIME')
    first_time = times[0]
    last_time = times[-1]
    tb.close()

    # Check if the outvis already exists
    if os.path.exists(outvis):
        print("File ", outvis, " already exists, change outvis name")
        return        
    # run the antab parsing and table filling
    shutil.copytree(vis, outvis)
    interpreter = AntabInterp(vis, outvis, antab, ant_names, n_band, spws,
                    first_time, last_time,
                    append_tsys, append_gc, overwrite)
    #antab_interp(vis, outvis, antab, ant_names, n_band, spws,
    #                first_time, last_time,
    #                append_tsys, append_gc, overwrite)
    interpreter.antab_interp()



#################################################################################################
# scanner regex from casavlbitools
def s_err(scanner, error):
    raise RuntimeError("line: %d" % scanner.line_no)

def s_keyword(scanner, token):
    if len(token) > 9 or '.' in token:
        res = ('value', token)
    else:
        res = ('key', token.upper())
    return res

def s_newline(scanner, token):
    scanner.line_no += 1
    return None

def s_quote(scanner, token):
    return ('quote', token[1:-1])

def s_number(scanner, token):
    return ('number', float(token))

def s_angle(scanner, token): # also time
    l = token.split(":")
    ## It's not python to use reduce.
    ## But I neither remember nor care what is.
    val = reduce(lambda acc, x: 60*acc+math.copysign(acc, float(x)), l, 0.0) 
    return ('number', val)

def s_value(scanner, token):
    return ('value', token)

def s_string(scanner, token):
    return ('value', token)

def s_misc(scanner, token):
    logging.debug("Misc token %s at line %d" % (str(token), scanner.line_no))
    return ('misc', token)

def s_comment(scanner, token): # was only used for debugging.
    scanner.line_no += 1
    return ('comment', token)

scanner = re.Scanner([
    ("\!.*\n", s_newline),
    ("[ \t]+", None),
    ("\n", s_newline),
    ("\r\n", s_newline),
    ("=", lambda s, t: ('equal',)),
    ("'[^'\n]*'", s_quote), 
    ("\"[^'\n]*\"", s_quote), # Sigh.  Double quotes used in freq.dat
    ("/", lambda s, t: ('end_chunk',)),
    (",", lambda s, t: ('comma',)),
    ("[+-]?[0-9]+:[0-9]+:[0-9]+(.[0-9]*)?", s_angle),
    ("[+-]?[0-9]+:[0-9]+(.[0-9]*)?", s_angle),
    ("[+-]?[0-9]*\.[0-9]+([Ee][+-][0-9]{1,3})?(?![A-Za-z_0-9()])", s_number),
    ("[+-]?[0-9]+\.?(?![A-Za-z_0-9()])", s_number),
    ## apparently parens and unquoted minus signs are allowed in keywords?
    ("[A-Za-z.0-9]([()A-Za-z_0-9._+-]+)?", s_keyword), 
    (".*", s_misc)
])

def p_all():
    global tok
    chunks = []
    try:
        while True:
            if tok=='EOF':break
            chunks.append(p_chunk())
    except StopIteration:
        pass
    return chunks

def p_chunk():
    global tok
    entries = []
    while tok[0] != 'end_chunk':
        entries.append(p_item())
    logging.debug("p_chunk %s", str(tok))
    tok = next(tokIt)
    return entries

def p_item():
    global tok
    lhs = p_key()

    if tok==('equal',):
        logging.debug("p_item %s", str(tok))
        tok = next(tokIt)
        rhs = p_rhs()
    elif tok[0] in ['value', 'quote', 'number']:
        rhs = p_rhs()
    else:
        rhs = True # for unitary expressions.
    return (lhs, rhs)

def p_key():
    global tok
    logging.debug("p_key: %s", str(tok))
    if tok[0] == 'key':
        res = tok
        tok = next(tokIt)
    else:
        raise RuntimeError("Expected key token, got %s" % str(tok))
    return res[1]

def p_rhs():
    global tok
    val = p_value()
    rhs = [val]
    while tok == ('comma',):
        logging.debug("p_rhs: %s", str(tok))
        tok = next(tokIt)
        rhs.append(p_value()) # p_value advances tok beyond the value.
    if len(rhs)==1:
        rhs = rhs[0]
    return rhs

def p_value():
    global tok
    if tok[0] not in ['value', 'quote', 'number', 'key']:
        raise RuntimeError("Unexpected RHS token %s" % str(tok))
    val = tok
    logging.debug("p_value: %s", str(val))
    tok = next(tokIt)
    return val[1]

scanner.line_no = 0
#################################################################################################
# data table Classes

class TSysTable:
    def __init__(self):
        self.time = []
        self.time_interval = []
        self.source_id = []
        self.antenna_no = []
        self.array = []
        self.freqid = []
        self.tsys_1 = []
        self.tsys_2 = []
        self.tant = []
        return

class GainCurveTable:
    def __init__(self):
        self.antenna_no = []
        self.array = []
        self.freqid = []
        self.spwid = []
        self.nterm = []
        self.y_typ = []
        self.gain = []
        self.sens_1 = []
        self.sens_2 = []
        return
    
##################################################################


def read_keyfile(f):
    global tok, tokIt
    scanner.line_no = 0

    try:
        res = scanner.scan(f.read())
        if res[1]!='':
            raise RuntimeError("Unparsed text: %s." % (res[1][:20]))
        tokIt = iter(res[0]+['EOF'])
        try: 
            tok = next(tokIt)
            res = p_all()
        except StopIteration: # empty file
            res = ''
    except RuntimeError as txt:
        #print("line %d:  %s" % (scanner.line_no, txt), file=sys.stderr)
        raise RuntimeError
    return res

def update_map(pols, spws, spwmap, index):
    idx = 0
    if not isinstance(index, (list, tuple)):
        index = [index]
        pass
    for labels in index:
        for label in labels.split('|'):
            pol = label[0]
            rng = label[1:].split(':')
            if pol != 'X':
                if not pol in pols:
                    pols.append(pol)
                    pass
                if len(rng) == 1:
                    rng.append(rng[0])
                    pass
                rng = [int(x) - 1 for x in rng]
                for spw in range(rng[0], rng[1] + 1):
                    if not spw in spws:
                        spws.append(spw)
                        pass
                    spwmap[(pol, spw)] = idx
                    continue
                pass
            continue
        idx += 1
        continue
    spws = sorted(spws)
    return

def find_antenna(keys, ignore):
    for key in keys[1:]:
        if not type(key[1]) is bool:
            continue
        if key[0] in ignore:
            continue
        return key[0]
    return None

def skip_values(infp):
    for line in infp:
        if line.startswith('!'):
            continue
        if line.strip().endswith('/'):
            break
        continue
    return

def get_antenna_index(antenna_name, ant_names):
    return ant_names.index(antenna_name)

def mjd_to_date(mjd):
    # Method used in FITSDateUtil
    mjd_epoch = dt.datetime(1858, 11 , 17, 0, 0, 0)

    mjd_int = int(mjd / 86400)
    delta = dt.timedelta(days=mjd_int)
    return mjd_epoch + delta

def mjd_seconds(yy, mm, dd, d=0):
    if (mm < 3):
        yy -= 1
        mm += 12

    dd += d
    b = 0

    if (yy>1582 or (yy==1582 and (mm>10 or (mm==10 and dd >= 15)))): 
        b = np.floor(yy/100.)
        b = 2 - b + int(b/4)
    
    val = np.floor(365.25*yy) + np.floor(30.6001*(mm+1)) + dd - 679006.0 + b
    return val


def get_timetuple(ts):
    # ts as string with these possible formats:
    # hh.hh      
    # hh:mm.mm   
    # hh:mm:ss.ss
    # NOTE: Regexs below will match any number of decimals on the last quantity (e.g. 19.8222222 and 19.8 both work)
    if re.match(r"[0-9]{2}\.[0-9]+", ts):
        # hh.hh 
        tm_hour = int(ts.split('.')[0])
        tm_min = math.modf(60*float(ts.split('.')[1]))
        tm_sec = int(60 * tm_min[0])
        tm_min = int(tm_min[1])
    elif re.match(r"[0-9]{2}:[0-9]{2}\.[0-9]+", ts):
        # hh:mm.mm 
        tm_hour = int(ts.split(':')[0])
        tm_min = math.modf(float(ts.split(':')[1]))
        tm_sec = int(60 * tm_min[0])
        tm_min = int(tm_min[1])
    elif re.match(r"[0-9]{2}:[0-9]{2}:[0-9]{2}$", ts):
        # hh:mm:ss
        tm_hour = int(ts.split(':')[0])
        tm_min = int(ts.split(':')[1])
        tm_sec = int(ts.split(':')[2])
    elif re.match(r"[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]+", ts):
        # hh:mm:ss.ss
        tm_hour = int(ts.split(':')[0])
        tm_min = int(ts.split(':')[1])
        tm_sec = float(ts.split(':')[2])
    return tm_hour, tm_min, tm_sec

############## interp class ###################

class AntabInterp:
    def __init__(self, vis, outvis, antab,
                 ant_names, n_band, spws,
                 first_time, last_time,
                 append_tsys, append_gc,
                 overwrite):
        
        # Passed to class when constructing
        self.vis = vis
        self.outvis = outvis
        self.antab = antab
        self.ant_names = ant_names
        self.n_band = n_band
        self.first_time = first_time
        self.last_time = last_time
        self.spws = spws
        self.append_tsys = append_tsys
        self.append_gc = append_gc
        self.overwrite = overwrite

        # used during procesing
        self.keys = None
        self.data = None
        self.data_gc = None
        self.pols = None
        self.spw_ranges = {}
        self.gain_keys = [ 'EQUAT', 'ALTAZ', 'ELEV', 'GCNRAO', 'TABLE', 'RCP', 'LCP' ]
        self.replacements = dict()


    # Core antab interp function
    def antab_interp(self):
        self.pols = []
        self.data = TSysTable()
        self.data_gc = GainCurveTable()
        keys = StringIO()
        fp = open(self.antab, 'r')

        for line in fp:
            #print(line)
            if line.startswith('!'):
                continue
            keys.write(line)
            if line.strip().endswith('/'):
                keys.seek(0)
                try:
                    tsys = read_keyfile(keys)
                    #print('TSYS: ', tsys)
                except RuntimeError:
                    print("\n", keys.getvalue(), file=sys.stderr)
                    raise RuntimeError('error parsing ANTAB file')
                if tsys and tsys[0] and tsys[0][0][0] == 'TSYS':
                    self.process_tsys(fp, tsys)
                    pass
                elif tsys and tsys[0] and tsys[0][0][0] == 'GAIN':
                    #print('ENTER PROCESS GC')
                    self.process_gc(fp, tsys)
                keys = StringIO()
                continue
            continue
        
        # Create the subtable for syscal if selected in params
        if self.append_tsys: 
            self.create_syscal_subtable()
        if self.append_gc: 
            self.create_gaincurve_subtable()

    def get_spw_ranges(self):
        # Get ranges for each spectral window
        try:
            tb.open(f'{self.vis}/SPECTRAL_WINDOW')
            for spw in self.spws:
                chan_freq = tb.getcol('CHAN_FREQ')[:,spw]
                min_freq = min(chan_freq) / (1e6)
                max_freq = max(chan_freq) / (1e6)
                self.spw_ranges[spw] = (min_freq, max_freq)
            tb.close()
        except Exception as e:
            print("ERROR FAILED TO GET SPW FREQ RANGES")

    def check_which_spw(self, freq):
        in_spw = []
        for spw, ranges in self.spw_ranges.items():
            if ranges[0] >= freq[0] and ranges[1] <= freq[1]:
                in_spw.append(spw)
        # If there is no spw that this belongs to default to what we were setting this value to before
        if not in_spw:
            print("WARNING: NO CORRESPONDING SPW FOUND FOR FREQ {}".format(freq))
            return [-1]
        else:
            return in_spw

    def process_tsys(self, infp, keys):
        # Get the antenna name
        antenna_name = find_antenna(keys[0], ['SRC/SYS'])
        # Skip if no antenna name found
        if not antenna_name:
            print('ANTENNA missing from TSYS group')
            skip_values(infp)
            return
        try:
            antenna = get_antenna_index(antenna_name, self.ant_names)
        except:
            print('Antenna {0} not present in the Measurement Set. {0} values will be ignored.'.format(antenna_name))
            skip_values(infp)
            return

        try:
            self.get_spw_ranges()
            spw_ids = self.check_which_spw(keys['FREQ'])
        except Exception as e:
            spw_ids = [-1]
            print('ANTAB HAS NO FREQ INFORMATION DEFAULTING TO FREQ ID -1')
        
        keys = dict(keys[0])
        spws = []
        spwmap = {}
        
        if 'INDEX' in keys:
            update_map(self.pols, spws, spwmap, keys['INDEX'])
        if 'INDEX2' in keys:
            update_map(self.pols, spws, spwmap, keys['INDEX2'])
            pass
        if len(spws) != self.n_band:
            print('INDEX for antenna %s does not match FITS-IDI file'
                % antenna_name, file=sys.stderr)
            pass

        spws = range(self.n_band)
        timeoff = 0
        if 'TIMEOFF' in keys:
            timeoff = float(keys['TIMEOFF'])

        for line in infp:
            if line.startswith('!'):
                continue

            fields = line.split()

            if len(fields) > 1:
                tm_yday = int(fields[0])
                # Get timestamp data depending on data format
                obs_date = mjd_to_date(self.first_time)
                tm_year = obs_date.year
                idi_time = tm.strptime(f"{obs_date.year}-{obs_date.month}-{obs_date.day}","%Y-%m-%d")
                idi_ref = tm.mktime(idi_time)

                # Get the start time in sec for MJD using the method from the table filler
                mjd_sec = mjd_seconds(int(obs_date.year), int(obs_date.month), int(obs_date.day)) * 86400

                tm_hour, tm_min, tm_sec = get_timetuple(fields[1])
                days = (tm_hour*3600 + tm_min*60 + tm_sec) / 86400
                t = "%dy%03dd%02dh%02dm%02ds" % \
                    (tm_year, tm_yday, tm_hour, tm_min, tm_sec)
                t = tm.mktime(tm.strptime(t, "%Yy%jd%Hh%Mm%Ss"))
                days = (t + timeoff - idi_ref) / 86400

                curr_time = mjd_sec + (days*86400)

                source = 0
                if (days) > ((self.last_time-mjd_sec)/86400) or (days) < ((self.first_time-mjd_sec)/86400):
                    source = -1

                #print(deg - mjd_sec)
                values = fields[2:]
                tsys = {'R': [], 'L': []}
                for spw in spws:
                    for pol in ['R', 'L']:
                        try:
                            value = float(values[spwmap[(pol, spw)]])
                            if value == 999.9:
                                value = float(-999.9)
                                pass
                        except:
                            value = float(-999.9)
                            pass
                        tsys[pol].append(value)
                        continue
                    continue
                if source != -1:
                    time_val = mjd_sec + (days * 86400)
                    self.data.time.append(time_val)
                    self.data.time_interval.append(0.0)
                    self.data.antenna_no.append(antenna)
                    self.data.tsys_1.append(tsys['R'])
                    self.data.tsys_2.append(tsys['L'])
                    self.data.freqid.append(spw_ids)

                    pass
                pass

            if line.strip().endswith('/'):
                break
            continue
        return

    def process_gc(self, infp, keys):
        antenna_name = find_antenna(keys[0], self.gain_keys)
        if not antenna_name:
            print('Antenna missing from GAIN group')
            skip_values(infp)
            return
        try:
            antenna = get_antenna_index(antenna_name, self.ant_names)
        except:
            print('Antenna {0} not present in the Measurement Set. {0} values will be ignored.'.format(antenna_name))
            skip_values(infp)
            return
        keys = dict(keys[0])

        try:
            freq = keys['FREQ']
            self.get_spw_ranges()
            spw_ids = self.check_which_spw(keys['FREQ'])
        except Exception as e:
            spw_ids = [-1]
            freq = [0, 0]
            print('ANTAB HAS NO FREQ INFORMATION DEFAULTING TO SPW ID -1 and freq to [0, 0]')

        dpfu = {}
        try:
            dpfu['R'] = keys['DPFU'][0]
            dpfu['L'] = keys['DPFU'][1]
            self.pols.append('R')
            self.pols.append('L')
        except:
            dpfu['R'] = dpfu['L'] = keys['DPFU']
            self.pols.append('X')
            pass
        try:
            value = keys['POLY'][0]
        except:
            keys['POLY'] = [keys['POLY']]
            pass

        y_typ = 0
        if 'ELEV' in keys:
            y_typ = 1
        elif 'EQUAT' in keys:
            y_typ = 1
        elif 'ALTAZ' in keys:
            y_typ = 2
        else:
            print('Unknown gain curve type for antenna %s' % antenna_name)
            return

        poly = keys['POLY']
        self.data_gc.antenna_no.append(antenna)
        self.data_gc.array.append(1)
        self.data_gc.freqid.append(freq)
        self.data_gc.spwid.append(spw_ids)
        self.data_gc.y_typ.append(y_typ)
        self.data_gc.nterm.append(len(poly))
        self.data_gc.gain.append(poly)
        self.data_gc.sens_1.append(dpfu['R'])
        self.data_gc.sens_2.append(dpfu['L'])
        return

    def create_existing_data_table(self):
        existing_data = dict()
        self.replacements = dict()
        if os.path.exists(f'{self.outvis}/GAIN_CURVE'):
            tb.open(f'{self.outvis}/GAIN_CURVE')
            antennas = tb.getcol('ANTENNA_ID')
            times = tb.getcol('TIME')
            spws = tb.getcol('SPECTRAL_WINDOW_ID')

            # add a set of times for each antenna
            # add a list of rows and spws for each antenna
            for i in range(len(antennas)):
                if antennas[i] not in existing_data:
                    existing_data[antennas[i]] = dict()
                    existing_data[antennas[i]]['times'] = set()
                    existing_data[antennas[i]]['rows'] = []
                    existing_data[antennas[i]]['spws'] = []

                    existing_data[antennas[i]]['times'].add(times[i])
                    existing_data[antennas[i]]['rows'].append(i)
                    existing_data[antennas[i]]['spws'].append(spws[i])
                else:
                    existing_data[antennas[i]]['times'].add(times[i])
                    existing_data[antennas[i]]['rows'].append(i)
                    existing_data[antennas[i]]['spws'].append(spws[i])
                    
            tb.close()

        return existing_data

    def create_gaincurve_subtable(self):
        # If no subtable exists add one
        if not os.path.exists(f'{self.outvis}/GAIN_CURVE'):
            # Create the subtable for gain curve
            tb.create(f'{self.outvis}/GAIN_CURVE', desc_gc, dminfo=dminfo_gc)
            tb.putkeyword('GAIN_CURVE', f'Table: {self.outvis}/GAIN_CURVE')

        # assemble columns
        ANTENNA_ID = []
        FEED_ID = []
        SPECTRAL_WINDOW_ID = []
        TIME = []
        INTERVAL = []
        TYPE = []
        NUM_POLY = []
        GAIN = []
        SENSITIVITY = [[],[]]

        # If a subtable exists then read contents into assembed data
        # Create data structure for antenna an time stamps to ignore if not overwriting
        existing_data = self.create_existing_data_table()

        # try getting channel freq information
        tb.open(f'{self.vis}/SPECTRAL_WINDOW')
        chan_freqs = tb.getcol('CHAN_FREQ')
        tb.close()

        # Get interval information from the observation table instead of meta-data
        tb.open(f'{self.outvis}/OBSERVATION')
        time_range = tb.getcol("TIME_RANGE")
        gc_interval = (time_range[1] - time_range[0])[0]
        gc_time = np.mean(time_range)
        tb.close()

        # New Array filler
        for row in range(len(self.data_gc.gain)):
            # iterate over spw range for non-overlapping case
            for j in self.spws:
                # get antenna and freqency range from antab for this row
                ant = self.data_gc.antenna_no[row]
                freq_range = self.data_gc.freqid[row]

                # If there is already data for that antenna and time and overwrite = False then skip
                if ant in existing_data and gc_time in existing_data[ant]['times'] and not self.overwrite:
                    print("antenna: {} has data present for the time {}. The antab data for this value will be ignored".format(ant, gc_time))
                    continue

                # If there is data present and overwrite is true then fill the replacement table
                elif ant in existing_data and gc_time in existing_data[ant]['times'] and self.overwrite:
                    # Get all the relevant data to put in replacements
                    rows = existing_data[ant]['rows']
                    spws = existing_data[ant]['spws']
                    # For each row and get chan freq of corrisponding spw
                    for i in range(len(rows)):
                        # r is the row that the data exists in the original GAIN_CURVE table
                        r = rows[i]
                        spw = spws[i]
                        freq = chan_freqs[row, spw] / (1e6)
                        # get the sensitivity from the proper freqency range
                        if freq >= freq_range[0] and freq <= freq_range[1]:
                            sens = [self.data_gc.sens_1[row], self.data_gc.sens_2[row]]
                        else:
                            continue

                        # Make an entry for row r in the replacments table
                        # r is the row in the gaincurve table that will be replaced
                        # row is the row in the antab where the data is present
                        self.replacements[r] = {'ANTENNA_ID':ant, 'FEED_ID':-1, 'INTERVAL':gc_interval,
                                                'TYPE':self.data_gc.y_typ[row], 'NUM_POLY':self.data_gc.nterm[row], 'GAIN':self.data_gc.gain[row],
                                                'TIME':gc_time, 'SPECTRAL_WINDOW_ID':spw, 'SENSITIVITY':sens}
                    continue
                
                # If the data doesn't overlap with existing data append as normal
                else:
                    TIME.append(gc_time)
                    ANTENNA_ID.append(self.data_gc.antenna_no[row])
                    FEED_ID.append(-1)
                    INTERVAL.append(gc_interval)
                    TYPE.append(str(self.data_gc.y_typ[row]))
                    NUM_POLY.append(self.data_gc.nterm[row])
                    GAIN.append(self.data_gc.gain[row])
                    SPECTRAL_WINDOW_ID.append(int(j))
                    SENSITIVITY[0].append(self.data_gc.sens_1[row])
                    SENSITIVITY[1].append(self.data_gc.sens_2[row])

        # If appending get existing cols and append values to it
        tb.open(f'{self.outvis}/GAIN_CURVE', nomodify=False)
        if not self.overwrite and tb.nrows() > 0:
            #tb.addrows(len(TIME))
            TIME = np.append(tb.getcol('TIME'), TIME)
            ANTENNA_ID = np.append(tb.getcol('ANTENNA_ID'), ANTENNA_ID)
            FEED_ID = np.append(tb.getcol('FEED_ID'), FEED_ID)
            INTERVAL = np.append(tb.getcol('INTERVAL'), INTERVAL)
            TYPE = np.append(tb.getcol('TYPE'), TYPE)
            NUM_POLY = np.append(tb.getcol('NUM_POLY'), NUM_POLY)

            # Can't call getcol on Gain since dimensions can vary
            tmp_GAIN = []
            # TODO ISSUE: Should only apply the gains for certain frequency ranges?
            for row in range(tb.nrows()):
                tmp_GAIN.append(tb.getcell('GAIN', row))
            # re-assembled the old and new gain col
            GAIN = tmp_GAIN + GAIN
            SPECTRAL_WINDOW_ID = np.append(tb.getcol('SPECTRAL_WINDOW_ID'), SPECTRAL_WINDOW_ID)
            tmp_0 = np.append(tb.getcol('SENSITIVITY')[0], SENSITIVITY[0])
            tmp_1 = np.append(tb.getcol('SENSITIVITY')[1], SENSITIVITY[1])
            SENSITIVITY = np.asarray([tmp_0, tmp_1])

        # If overwriting then go over the existing rows to overwrite
        if self.overwrite:
            TIME = np.append(tb.getcol('TIME'), TIME)
            ANTENNA_ID = np.append(tb.getcol('ANTENNA_ID'), ANTENNA_ID)
            FEED_ID = np.append(tb.getcol('FEED_ID'), FEED_ID)
            INTERVAL = np.append(tb.getcol('INTERVAL'), INTERVAL)
            TYPE = np.append(tb.getcol('TYPE'), TYPE)
            NUM_POLY = np.append(tb.getcol('NUM_POLY'), NUM_POLY)
            # Can't call getcol on Gain since dimensions can vary
            tmp_GAIN = []
            # TODO ISSUE: Should only apply the gains for certain frequency ranges?
            for row in range(tb.nrows()):
                tmp_GAIN.append(tb.getcell('GAIN', row))
            # re-assembled the old and new gain col
            GAIN = tmp_GAIN + GAIN
            SPECTRAL_WINDOW_ID = np.append(tb.getcol('SPECTRAL_WINDOW_ID'), SPECTRAL_WINDOW_ID)
            tmp_0 = np.append(tb.getcol('SENSITIVITY')[0], SENSITIVITY[0])
            tmp_1 = np.append(tb.getcol('SENSITIVITY')[1], SENSITIVITY[1])
            SENSITIVITY = np.asarray([tmp_0, tmp_1])
            
            for row, data in self.replacements.items():
                TIME[row] = data['TIME']
                ANTENNA_ID[row] = data['ANTENNA_ID']
                FEED_ID[row] = data['FEED_ID']
                INTERVAL[row] = data['INTERVAL']
                TYPE[row] = data['TYPE']
                NUM_POLY[row] = data['NUM_POLY']
                GAIN[row] = data['GAIN']
                SPECTRAL_WINDOW_ID[row] = data['SPECTRAL_WINDOW_ID']
                SENSITIVITY[:, row] = [data['SENSITIVITY'][0], data['SENSITIVITY'][1]]
                
        tb.close()

        # Add the columns to the table
        tb.open(f'{self.outvis}/GAIN_CURVE', nomodify=False)
        to_add = len(TIME) - tb.nrows()
        tb.addrows(to_add)
        tb.putcol('TIME', TIME)
        tb.putcol('ANTENNA_ID', ANTENNA_ID)
        tb.putcol('FEED_ID', FEED_ID)
        tb.putcol('SPECTRAL_WINDOW_ID', SPECTRAL_WINDOW_ID)
        tb.putcol('INTERVAL', INTERVAL)
        # Type 1 POWER(EL) Type 2 POWER(ZA)
        tb.putcol('NUM_POLY', NUM_POLY)

        #Fill gain row by row
        for i in range(len(GAIN)):
            # If the gain col shape doesn't match what the table filler does
            if len(np.shape(GAIN[i])) < 2:
                tb.putcell('GAIN', i, [GAIN[i],GAIN[i]])
            else:
                tb.putcell('GAIN', i, GAIN[i])
            
            # Convert Type to proper string
            if TYPE[i] == '1':
                TYPE[i] = 'POWER(EL)'
            elif TYPE[i] == '2':
                TYPE[i] = 'POWER(ZA)'

        tb.putcol('TYPE', TYPE)
        tb.putcol('SENSITIVITY', SENSITIVITY)
        #tb.flush()
        tb.close()


    def create_syscal_subtable(self):    
        # If no subtable exists
        if not os.path.exists(f'{self.outvis}/SYSCAL'):
            # Create the subtable for syscal
            tb.create(f'{self.outvis}/SYSCAL', desc, dminfo=dminfo)
            tb.putkeyword('SYSCAL', f'Table: {self.outvis}/SYSCAL')

        # Assemble columns
        ANTENNA_ID = []
        FEED_ID = []
        INTERVAL = []
        SPW_ID = []
        TIME = []
        TSYS = [[],[]]
        self.data.tsys_1 = np.asarray(self.data.tsys_1)
        self.data.tsys_2 = np.asarray(self.data.tsys_2)

        # If a subtable exists then read contents into assembed data
        # Create data structure for antenna an time stamps to ignore if not overwriting
        existing_data = self.create_existing_data_table()

        # Fill the arrays
        to_skip = []
        self.replacements = dict()
        for i in range(len(self.data.time)):
            # if the antenna has been visited already with the same time stamp then ignore
            if self.data.antenna_no[i] in existing_data and self.data.time[i] in existing_data[self.data.antenna_no[i]]['times'] and not self.overwrite:
                # This data is already in the subtable so ignore
                print("antenna: {} has data present for the time {}. The antab data for this value will be ignored".format(self.data.antenna_no[i], self.data.time[i]))
                to_skip.append(True)
                continue
            else:
                to_skip.append(False)

            for j in self.spws:
                # get antenna from antab for this row
                ant = self.data.antenna_no[i]

                # Check that this antenna is in this spectral window
                if j not in self.data.freqid[i] and self.data.freqid[i] != [-1]:
                    continue
                if ant in existing_data and self.data.time[i] in existing_data[ant]['times'] and self.overwrite:
                    # Get the row and information to overwrite the row from the ms
                    # Get all the relevant data to put in replacements
                    rows = existing_data[ant]['rows']
                    spws = existing_data[ant]['spws']

                    for r in range(len(rows)):
                        row = rows[r]
                        spw = spws[r]
                        
                        self.replacements[row] = {'ANTENNA':self.data.antenna_no[i], 'FEED_ID':0, 'INTERVAL':self.data.time_interval[i],
                                        'SPW_ID':spw, 'TIME':self.data.time[i], 'TSYS':[[],[]]}
                        print(row, spw, int(j))
                    #row = existing_data[ant]['row']
                    to_skip.append(True)

                    #self.replacements[row] = {'ANTENNA':self.data.antenna_no[i], 'FEED_ID':0, 'INTERVAL':self.data.time_interval[i],
                    #                    'SPW_ID':int(j), 'TIME':self.data.time[i], 'TSYS':[[],[]]}

                    continue

                ANTENNA_ID.append(self.data.antenna_no[i])
                FEED_ID.append(0)
                INTERVAL.append(self.data.time_interval[i])
                SPW_ID.append(int(j))
                TIME.append(self.data.time[i])

        for i in range(len(self.data.tsys_1)):
            if to_skip[i] and not self.overwrite:
                continue
            elif to_skip[i] and self.overwrite:
                self.replacements[i]['TSYS'][0].extend(self.data.tsys_1[i])
                self.replacements[i]['TSYS'][1].extend(self.data.tsys_2[i])
                continue
            TSYS[0].extend(self.data.tsys_1[i])
            TSYS[1].extend(self.data.tsys_2[i])

        # If appending get existing cols and append values to it also check if empty
        tb.open(f'{self.outvis}/SYSCAL', nomodify=False)
        if not self.overwrite and tb.nrows() > 0:
            TIME = np.append(tb.getcol('TIME'), TIME)
            ANTENNA_ID = np.append(tb.getcol('ANTENNA_ID'), ANTENNA_ID)
            INTERVAL = np.append(tb.getcol('INTERVAL'), INTERVAL)
            SPW_ID = np.append(tb.getcol('SPECTRAL_WINDOW_ID'), SPW_ID)
            tmp_0 = np.append(tb.getcol('TSYS')[0], TSYS[0])
            tmp_1 = np.append(tb.getcol('TSYS')[1], TSYS[1])
            TSYS = np.asarray([tmp_0, tmp_1])

        # If overwriting then go over the existing rows to overwrite
        if self.overwrite:
            for row, data in self.replacements.items():
                TIME[row] = data['TIME']
                ANTENNA_ID[row] = data['ANTENNA']
                INTERVAL[row] = data['INTERVAL']
                SPW_ID[row] = data['SPW_ID']
                #print(TSYS[0][row], TSYS[1][row])
                TSYS[0][row] = data['TSYS'][0]
                TSYS[1][row] = data['TSYS'][1]
        tb.close()

        # Add the columns to the table
        tb.open(f'{self.outvis}/SYSCAL', nomodify=False)
        to_add = len(TIME) - tb.nrows()
        tb.addrows(to_add)
        tb.putcol('TIME', TIME)
        tb.putcol('ANTENNA_ID', ANTENNA_ID)
        tb.putcol('INTERVAL', INTERVAL)
        tb.putcol('SPECTRAL_WINDOW_ID', SPW_ID)
        tb.putcol('TSYS', TSYS)
        #tb.flush()
        tb.close()
