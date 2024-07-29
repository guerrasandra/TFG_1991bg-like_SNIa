#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:50:36 2024

@author: sandraguerra
"""
import matplotlib.pyplot as plt
import numpy as np

def cargar_datos(filename):

    data = np.loadtxt(filename)
    longitud_onda = data[:, 0]
    flujo = data[:, 1]
    error = data[:, 2]
    return longitud_onda, flujo, error

def normalizar_flujo(longitud_onda, flujo, error, longitud_objetivo=5500):
    idx_cercano = (np.abs(longitud_onda - longitud_objetivo)).argmin()
    flujo_normalizado = flujo / flujo[idx_cercano]
    error_normalizado = error / flujo[idx_cercano]
    return flujo_normalizado, error_normalizado




archivos = [

    "mean1021.txt",
    "mean69.txt",
    "mean25.txt",
    "mean11.txt",
    "mean42.txt",
    "mean115.txt",

]


nombres_espectros = [
    "from 10 to 21",
    "from 6 to 9",
    "from 2 to 5",
    "from -1 to 1",
    "from -4 to -2",   
    "from -11 to -5",





]


fig, ax = plt.subplots(figsize=(10, len(archivos) * 2))

for i, (archivo, nombre) in enumerate(zip(archivos, nombres_espectros)):
    try:
        longitud_onda, flujo, error = cargar_datos(archivo)
        flujo_normalizado, error_normalizado = normalizar_flujo(longitud_onda, flujo, error)
        log_flujo = np.log10(flujo_normalizado)
        
        desplazamiento = i + 1
        
        ax.errorbar(longitud_onda, log_flujo + desplazamiento, xerr=error_normalizado, label=nombre, fmt='-', capsize=3)
    except Exception as e:
        print(f"Error al cargar {archivo}: {e}")

ax.set_xlabel('Wavelength', fontsize=20)
#ax.set_ylabel('log(flux)')
ax.set_title('Mean of each epoch', fontsize=25)
ax.legend()

plt.show()

