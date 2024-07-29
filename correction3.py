#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:53:12 2024

@author: sandraguerra
"""

from extinction import fitzpatrick99 as f99, apply
import numpy as np

data = np.loadtxt('ZTF20acymtbr_20201213_SNIFS_0_flux2.ascii')

z = 0.06107559
ebv_host = 0.184

new_data_flux3 = []  #(wave_2, flux_3)
#wave_3=wave_2

for row in data:
    wave_2 = np.array([row[0]])  
    flux_2 = np.array(row[1])
    
    flux_3 = apply(f99(wave_2,-2.5*ebv_host,2.5),flux_2)[0]
    
    new_data_flux3.append([wave_2, flux_3])


new_data_flux3 = np.array(new_data_flux3)

fmt = ['%.12f', '%.15e']
np.savetxt('ZTF20acymtbr_20201213_SNIFS_0_flux3.ascii', new_data_flux3, fmt=fmt)


