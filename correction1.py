#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:36:14 2024

@author: sandraguerra
"""

from extinction import fitzpatrick99 as f99, apply
import numpy as np

data = np.loadtxt('ZTF20acvbrbv_20201214_Lick-3m_0')

ebv =  0.066
z = 0.04717255

new_data_flux1 = []  # (wave_0, flux_1)
new_data_flux2 = []  # (wave_2, flux_2)



for row in data:
    wave_0 = np.array([row[0]])  
    flux_0 = np.array(row[1])
    
    flux_1 = apply(f99(wave_0, -3.1 * ebv, 3.1), flux_0)[0]  

    
    flux_2 = flux_1 * (1 + z)
    wave_2 = wave_0 / (1 + z)
    
    new_data_flux1.append([wave_0, flux_1])
    new_data_flux2.append([wave_2, flux_2])

new_data_flux1 = np.array(new_data_flux1)
new_data_flux2 = np.array(new_data_flux2)


fmt = ['%.12f', '%.15e']
#np.savetxt('ZTF18acefgoc_20181024_LT_0_flux1.ascii', new_data_flux1, fmt=fmt)
#np.savetxt('ZTF18acefgoc_20181024_LT_0_flux2.ascii', new_data_flux2, fmt=fmt)

