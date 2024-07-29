#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:52:57 2024

@author: sandraguerra
"""

import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np
from spectres import spectres


def read_data(ZTF):
    with open(ZTF, 'r') as archivo:
        data = archivo.readlines()
    x = []
    y = []
    for linea in data:
        if not linea.startswith('#'):
            valores = linea.split()
            x.append(float(valores[0]))
            y.append(float(valores[1]))
    return x, y

archivo= 'ZTF20acvbrbv_20201214_Lick-3m_0_flux3.ascii'
archivo_error = 'ZTF20acvbrbv_20201214_Lick-3m_0_flux3_smootherror.ascii'

x1, y1 = read_data(archivo)
x2, var_flux = np.loadtxt(archivo_error, unpack=True, usecols=(0, 2))


plt.figure(figsize=(25,8))
plt.title('ZTF20acvbrbv_20201214_Lick-3m_0',fontsize=25)
plt.xlabel('Wavelength',fontsize=20)   
plt.ylabel('Flux',fontsize=20)
plt.plot(x1, y1,linestyle='-',c='lightgrey', zorder=0)
sx,sy = x1,savgol_filter(y1, 51, 3)
plt.errorbar(sx, sy, xerr=var_flux, fmt='none', ecolor='red', capsize=5,zorder=1)
plt.plot(sx,sy,color='black',linestyle='-', zorder=2) 

#resampleig
#rx = np.arange(3500., 9000., 1.)
#rx = np.arange(max(min(sx), 3500.), min(max(sx), 9000.), 1.)
rx = np.arange(np.ceil(max(min(sx), 3000.)), np.floor(min(max(sx), 9500.)) + 1, 1)
#ry = spectres(np.array(rx), np.array(sx), np.array(sy),fill=np.nan)
#re = spectres(np.array(rx), np.array(sx), np.array(var_flux),fill=np.nan) 

#ry = spectres(np.array(rx), np.array(sx), np.array(sy),fill=np.nan,verbose=True)
ry =np.interp(np.array(rx), np.array(sx), np.array(sy))
#re = spectres(np.array(rx), np.array(sx), np.array(var_flux),fill=np.nan)
re =np.interp(np.array(rx), np.array(sx), np.array(var_flux))
plt.errorbar(rx, ry, xerr=re, fmt='none', ecolor='green', capsize=5) 
plt.plot(rx,ry,color='blue') # i tens l'error re
 

#zoom_range = (7200, 7250)  # x
#plt.xlim(zoom_range)
#y_min = min(sy[(np.array(sx) >= zoom_range[0]) & (np.array(sx) <= zoom_range[1])])
#y_max = max(sy[(np.array(sx) >= zoom_range[0]) & (np.array(sx) <= zoom_range[1])])
#ry_min = min(ry[(rx >= zoom_range[0]) & (rx <= zoom_range[1])])
#ry_max = max(ry[(rx >= zoom_range[0]) & (rx <= zoom_range[1])])
#plt.ylim(min(y_min, ry_min) * 0.95, max(y_max, ry_max) * 1.05)


plt.grid(True)
plt.tight_layout()
plt.show()


#max_length = max(len(sx), len(sy), len(var_flux), len(rx), len(ry), len(re))
#sx_padded = np.pad(sx, (0, max_length - len(sx)), constant_values=np.nan)
#sy_padded = np.pad(sy, (0, max_length - len(sy)), constant_values=np.nan)
#var_flux_padded = np.pad(var_flux, (0, max_length - len(var_flux)), constant_values=np.nan)
#rx_padded = np.pad(rx, (0, max_length - len(rx)), constant_values=np.nan)
#ry_padded = np.pad(ry, (0, max_length - len(ry)), constant_values=np.nan)
#re_padded = np.pad(re, (0, max_length - len(re)), constant_values=np.nan)

#new_data = np.column_stack((sx_padded, sy_padded, var_flux_padded, rx_padded, ry_padded, re_padded))
#fmt = ['%.12f', '%.15e', '%.15e', '%.12f', '%.15e', '%.15e']
#np.savetxt('data.ascii', new_data, fmt=fmt)

new_data = np.column_stack((rx,ry,re))
fmt = [ '%.12f', '%.15e', '%.15e']
#np.savetxt('ZTF20acymtbr_20201213_SNIFS_0_flux2_resampled.ascii', new_data, fmt=fmt)


    

