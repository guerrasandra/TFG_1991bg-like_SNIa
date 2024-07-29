#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:52:25 2024

@author: sandraguerra
"""

import matplotlib.pyplot as plt

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

archivo1 = 'ZTF20acvbrbv_20201214_Lick-3m_0.ascii'
archivo2 = 'ZTF20acvbrbv_20201214_Lick-3m_0_flux1.ascii'
#archivo3 = 'ZTF20acvbrbv_20201214_Lick-3m_0_flux2.ascii'
#archivo4 = 'ZTF20acvbrbv_20201214_Lick-3m_0_flux3.ascii'


x1, y1 = leer_datos(archivo1)
x2, y2 = leer_datos(archivo2)
#x3, y3 = leer_datos(archivo3)
#x4, y4 = leer_datos(archivo4)

plt.figure(figsize=(25,8))
plt.plot(x1, y1, label='original',linestyle='-', color='black')
plt.plot(x2, y2, label='1st correction ',linestyle='-', color='red')
#plt.plot(x3, y3, label='2nd correction',linestyle='-', color='green')
#plt.plot(x4, y4, label='3rd correction',linestyle='-', color='purple')
plt.title('ZTF20acvbrbv_20201214_Lick-3m_0',fontsize=25) 
plt.xlabel('Wavelength', fontsize=20)
plt.ylabel('Flux', fontsize=20)   
#plt.ylim(-1e-16, 1e-16)
plt.legend(fontsize=19)
plt.grid(True)
plt.tight_layout()
plt.show()
