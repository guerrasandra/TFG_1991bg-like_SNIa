#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:36:09 2024

@author: sandraguerra
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d



archivos = [
    "ZTF19aanhgqg_20190325_SEDm_0_flux3_resampled.ascii",
    "ZTF19acynije_20191220_LT_0_flux3_resampled.ascii",
    "ZTF20acduffd_20200927_SEDm_0_flux3_resampled.ascii",
    "ZTF19aanhgqg_20190326_SEDm_0_flux3_resampled.ascii",
    "ZTF18aabstmw_20180307_LCO-FLOYDS_0_flux3_resampled.ascii",
    "ZTF18aabstmw_20180307_SEDm_0_flux3_resampled.ascii",
    "ZTF19abzlsbl_20190921_SEDm_0_flux3_resampled.ascii",
    "ZTF20abjapav_20200630_LT_0_flux3_resampled.txt"
]


data_list = []
for file in archivos:
    data = pd.read_csv(file, delim_whitespace=True, header=None, names=['longitud_onda', 'flujo', 'error'])
    data['flujo'] /= data['flujo'].max()
    data_list.append(data)
    
longitudes_onda_unicas = sorted(set(np.concatenate([data['longitud_onda'].values for data in data_list])))

flujo_ponderado = []
error_ponderado = []

for longitud in longitudes_onda_unicas:
    flujos = []
    errores = []
    for data in data_list:
        if longitud in data['longitud_onda'].values:
            flujo = data[data['longitud_onda'] == longitud]['flujo'].values[0]
            error = data[data['longitud_onda'] == longitud]['error'].values[0]
            flujos.append(flujo)
            errores.append(error)
    
    if flujos:
        flujos = np.array(flujos)
        errores = np.array(errores)
        peso = 1 / (errores ** 2)
        flujo_media_ponderada = np.sum(flujos * peso) / np.sum(peso)
        error_combinado = np.sqrt(1 / np.sum(peso))
        
        flujo_ponderado.append(flujo_media_ponderada)
        error_ponderado.append(error_combinado)
    else:
        flujo_ponderado.append(np.nan)
        error_ponderado.append(np.nan)

resultados = np.column_stack((longitudes_onda_unicas, flujo_ponderado, error_ponderado))

fmt = ['%.12f', '%.15e', '%.15e']
np.savetxt('mean1153.txt', resultados, fmt=fmt)

columnas = ['longitud_onda', 'flujo_ponderado', 'error_ponderado']
data = pd.read_csv('mean1153.txt', delim_whitespace=True, names=columnas)

x1 = data['longitud_onda']
y1 = data['flujo_ponderado']
var_flux = data['error_ponderado']

plt.figure(figsize=(25, 8))
plt.xlabel('wavelength', fontsize=12)
plt.ylabel('flux', fontsize=12)
plt.plot(x1, y1, linestyle='-', color='black', zorder=1)
plt.errorbar(x1, y1, xerr=var_flux, fmt='none', ecolor='lightgrey', capsize=5, zorder=0)
plt.title('from -11 to -5', fontsize=15)
plt.grid(True)
plt.tight_layout()
plt.show()


