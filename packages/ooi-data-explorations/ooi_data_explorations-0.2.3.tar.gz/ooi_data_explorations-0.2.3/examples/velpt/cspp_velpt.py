#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from ooi_data_explorations.common import get_vocabulary, load_gc_thredds, update_dataset, CONFIG, ENCODINGS
from ooi_data_explorations.uncabled.process_velpt import velpt_cspp


def main():
    # Setup needed parameters for the request, the user would need to vary
    # these to suit their own needs and sites/instruments of interest. Site,
    # node, sensor, stream and delivery method names can be obtained from the
    # Ocean Observatories Initiative website. The last two parameters (level
    # and instrmt) will set path and naming conventions to save the data to
    # the local disk.
    site = 'CE02SHSP'           # OOI Net site designator
    node = 'SP001'              # OOI Net node designator
    sensor = '02-VELPTJ000'     # OOI Net sensor designator
    stream = 'velpt_j_cspp_instrument_recovered'  # OOI Net stream name
    method = 'recovered_cspp'   # OOI Net data delivery method
    level = 'cspp'              # local directory name, level below site
    instrmt = 'velpt'           # local directory name, instrument below level

    # download information about the instrument and site
    vocab = get_vocabulary(site, node, sensor)[0]

    # download the data for deployment 17 from the Gold Copy THREDDS catalog
    velpt = load_gc_thredds(site, node, sensor, method, stream, 'deployment0017.*VELPT.*\\.nc$')

    # clean-up and reorganize
    velpt = velpt_cspp(velpt)
    velpt = update_dataset(velpt, vocab['maxdepth'])

    # save the data
    out_path = os.path.join(CONFIG['base_dir']['m2m_base'], site.lower(), level, instrmt)
    out_path = os.path.abspath(out_path)
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    out_file = ('%s.%s.%s.deploy17.%s.%s.nc' % (site.lower(), level, instrmt, method, stream))
    nc_out = os.path.join(out_path, out_file)

    velpt.to_netcdf(nc_out, mode='w', format='NETCDF4', engine='h5netcdf', encoding=ENCODINGS)


if __name__ == '__main__':
    main()
