#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from ooi_data_explorations.common import get_vocabulary, load_gc_thredds, update_dataset, ENCODINGS
from ooi_data_explorations.uncabled.process_optaa import optaa_datalogger


# Setup needed parameters for the request, the user would need to vary these to
# suit their own needs and sites/instruments of interest. Site, node, sensor,
# stream and delivery method names can be obtained from the Ocean Observatories
# Initiative website. The last two will set path and naming conventions to save
# the data to the local disk
site = 'CE02SHSM'                               # OOI Net site designator
node = 'RID27'                                  # OOI Net node designator
sensor = '01-OPTAAD000'                         # OOI Net sensor designator
stream = 'optaa_dj_dcl_instrument_recovered'    # OOI Net stream name
method = 'recovered_host'                       # OOI Net data delivery method
tag = '.*deployment0003.*OPTAA.*\\.nc$'         # limit request to OPTAA NetCDF files from Deployment 3
level = 'nsif'                                  # local directory name, level below site
instrmt = 'optaa'                               # local directory name, instrument below level

# recovered host data is best downloaded from the Gold Copy THREDDS catalog (much faster than an M2M request)
optaa = load_gc_thredds(site, node, sensor, method, stream, tag)
vocab = get_vocabulary(site, node, sensor)[0]

# set up the calibration file path and name
cal_path = os.path.join(os.path.expanduser('~'), 'ooidata/m2m', site.lower(), level, instrmt)
cal_path = os.path.abspath(cal_path)
if not os.path.exists(cal_path):
    os.makedirs(cal_path)

cal_file = ('{}.{}.{}.deploy03.cal_coeffs.json'.format(site.lower(), level, instrmt))
cal_file = os.path.join(cal_path, cal_file)

# clean-up and reorganize
optaa = optaa_datalogger(optaa, cal_file)
optaa = update_dataset(optaa, vocab['maxdepth'])

# save the data
out_path = os.path.join(os.path.expanduser('~'), 'ooidata/m2m', site.lower(), level, instrmt)
out_path = os.path.abspath(out_path)
if not os.path.exists(out_path):
    os.makedirs(out_path)

out_file = ('{}.{}.{}.deploy03.{}.{}.nc'.format(site.lower(), level, instrmt, deploy, method, stream))
nc_out = os.path.join(out_path, out_file)

optaa.to_netcdf(nc_out, mode='w', format='NETCDF4', engine='h5netcdf', encoding=ENCODINGS)
