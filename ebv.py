#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:30:32 2024

@author: sandraguerra
"""

#from dustmaps.config import config
#config['data_dir'] = '/opt/anaconda3/lib/python3.8/site-packages/dustmaps/data/' 
#dustmaps.sfd.fetch()

from astropy.coordinates import SkyCoord
from dustmaps.sfd import SFDQuery
from astropy import units as u
sfd = SFDQuery()

coords = SkyCoord(154.846936,44.408572,unit=(u.deg, u.deg), frame='icrs')
ebv = sfd(coords) * 0.86
print('E(B-V) = {:.3f} mag'.format(ebv))