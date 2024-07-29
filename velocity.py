#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 11:16:35 2024

@author: sandraguerra
"""

import numpy as np
import glob

c = 299792458

files =[
        
    "ZTF20abxlham_20200906_SEDm_0_flux3_resampled.txt",
    "ZTF20aciigcw_20201016_SEDm_0_flux3_resampled.txt",
    "ZTF20aagloch_20200126_SEDm_0_flux3_resampled.txt",
    "ZTF20acuoacn_20201207_NTT_0_flux3_resampled.txt",
    "ZTF20aattotq_20200328_Ekar_0_flux3_resampled.txt",
    "ZTF19abalrbb_20190625_SEDm_0_flux3_resampled.txt",
    "ZTF19abcttsc_20190711_SEDm_0_flux3_resampled.txt",
    "ZTF20aaflaug_20200123_SEDm_0_flux3_resampled.txt",
    "ZTF20aattotq_20200329_SEDm_0_flux3_resampled.txt",
    "ZTF18aahjaxz_20180418_SEDm_0_flux3_resampled.txt",
    "ZTF19abzprpk_20190924_SEDm_0_flux3_resampled.txt",
    "ZTF18aajtlbf_20180420_P200_0_flux3_resampled.txt",
    "ZTF18abixkdo_20180730_SEDm_0_flux3_resampled.txt",
    "ZTF18abtnbys_20180913_P200_0_flux3_resampled.txt",
    "ZTF19abhbjge_20190727_SEDm_0_flux3_resampled.txt",
    "ZTF19aaejslw_20190127_NTT_0_flux3_resampled.txt",
    "ZTF19acblzux_20191004_SEDm_0_flux3_resampled.txt",
    "ZTF18abdmgab_20180713_Keck_0_flux3_resampled.txt",
    "ZTF20abegopd_20200615_SEDm_0_flux3_resampled.txt",
    "ZTF20aatzwgk_20200411_Other_0_flux3_resampled.txt",
    "ZTF18acrcetn_20181203_SNIFS_0_flux3_resampled.txt",
    "ZTF20acvbrbv_20201211_SEDm_0_flux3_resampled.txt",
    "ZTF18abltdfj_20180811_SEDm_0_flux3_resampled.txt",
    "ZTF19achahea_20191023_SEDm_0_flux3_resampled.txt",
    "ZTF19aaarhtg_20200719_Lick-3m_0_flux3_resampled.txt",
    "ZTF18aarcypa_20180516_SEDm_0_flux3_resampled.txt",
    "ZTF18aaimxdx_20180411_P200_0_flux3_resampled.txt",
    "ZTF20acbakkg_20200928_SEDm_0_flux3_resampled.txt",
    "ZTF18absnqyo_20180915_Lick-3m_0_flux3_resampled.txt",
    "ZTF20abzettb_20200916_P200_0_flux3_resampled.txt"  ,
    "mean113.txt"
        
        
]

def calculate_velocity(wavelengths, fluxes, target_wavelength=6100, window=100):
    mask = (wavelengths >= (target_wavelength - window)) & (wavelengths <= (target_wavelength + window))
    restricted_wavelengths = wavelengths[mask]
    restricted_fluxes = fluxes[mask]
    
    if len(restricted_fluxes) == 0:
        raise ValueError("No data points within the specified wavelength range.")
        
    min_flux_index = np.argmin(restricted_fluxes)
    min_wavelength = restricted_wavelengths[min_flux_index]
    
    velocity = ((min_wavelength - 6355) / 6355) * c
    
    velocity_kms = velocity / 1000
    return min_wavelength, velocity_kms

velocities = []

for file in files:
    data = np.loadtxt(file)
    wavelengths = data[:, 0]  
    fluxes = data[:, 1]       
    
    try:
        min_wavelength, velocity_kms = calculate_velocity(wavelengths, fluxes)
        velocities.append(velocity_kms)
        print(f"File: {file}, Min Wavelength: {min_wavelength}, Velocity: {velocity_kms:.2f} km/s")
    except ValueError as e:
        print(f"File: {file}, Error: {e}")

#np.savetxt("supernovae_velocities_km.txt", velocities, header="Velocity (km/s)")

print("Calculated velocities for all supernovae:")
for i, v in enumerate(velocities, 1):
    print(f"Supernova {i}: {v:.2f} km/s")
    
    
    
    