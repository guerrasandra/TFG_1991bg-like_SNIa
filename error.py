#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:01:52 2024

@author: sandraguerra
"""
import numpy as np
from scipy.signal import savgol_filter

import matplotlib.pyplot as plt

def varflux(file):
    original_data = np.loadtxt('ZTF20acvbrbv_20201214_Lick-3m_0_flux3.ascii')
    smooth_data = np.loadtxt('ZTF20acvbrbv_20201214_Lick-3m_0_flux3_smooth.ascii')
    wavelength_original, rawflux = original_data[:, 0], original_data[:, 1]
    wavelength_smooth, sm1st_flux = smooth_data[:, 0], smooth_data[:, 1]
    #assert np.array_equal(wavelength_original, wavelength_smooth)
    # get the error sepctrum without smoothing
    errorflux = np.abs(rawflux - sm1st_flux)
    # second smoothing of errorflux with vexp = 0.008
    sm2nd_flux = savgol_filter(errorflux, 31, 3)
    # make errorflux become varflux
    var_flux = sm2nd_flux#**2

    lw=len(wavelength_original)
    gaussian = (1/lw/6*np.sqrt(2*np.pi))* np.exp((-0.5)*((wavelength_original-wavelength_original[int(lw/2)])/lw/6)**2)
    errvign=(1/gaussian)/np.min(1/gaussian)*np.mean(var_flux)
    errtot=np.sqrt(errvign**2+var_flux**2)
    #ratio = sm1st_flux/sm2nd_flux

    new_data = np.column_stack((wavelength_smooth, sm1st_flux, errtot))
    fmt = [ '%.12f', '%.15e', '%.15e']
    #np.savetxt('ZTF20acymtbr_20201213_SNIFS_0_flux2_smootherror.ascii', new_data, fmt=fmt)        
    return errtot

varflux('ZTF20acvbrbv_20201214_Lick-3m_0.ascii')



