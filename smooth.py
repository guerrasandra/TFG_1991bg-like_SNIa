#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:44:58 2024

@author: sandraguerra
"""

import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np


def leer_datos(ZTF):
    with open(ZTF, 'r') as archivo:
        datos = archivo.readlines()
    x = []
    y = []
    for linea in datos:
        if not linea.startswith('#'):
            valores = linea.split()
            x.append(float(valores[0]))
            y.append(float(valores[1]))
    return x, y

archivo = 'ZTF20acvbrbv_20201214_Lick-3m_0_flux3.ascii'

x1, y1 = leer_datos(archivo)

plt.figure(figsize=(25,8))
plt.title('ZTF20acvbrbv_20201214_Lick-3m_0', fontsize=25)
plt.xlabel('Wavelength',fontsize=20)
plt.ylabel('Flux',fontsize=20)   
plt.plot(x1, y1,linestyle='-',c='lightgrey')
sx,sy = x1,savgol_filter(y1,51,3)
plt.plot(sx,sy,color='black', linestyle='-')  
plt.grid(True)
plt.tight_layout()
plt.show()


smooth_data = [[sx[i], sy[i]] for i in range(len(sx))]
fmt = ['%.12f', '%.15e']
#np.savetxt('ZTF20acymtbr_20201213_SNIFS_0_flux2_smooth.ascii', smooth_data, fmt=fmt)
