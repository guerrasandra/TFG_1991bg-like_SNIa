#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:30:14 2024

@author: sandraguerra
"""

from astropy.time import Time
from datetime import datetime


txt = "ZTF20acvbrbv_20201211_2903.ascii"
x = txt.split("_")
print(x[1])

fecha_con_guiones = datetime.strptime(str(x[1]), '%Y%m%d').date()
print(fecha_con_guiones)

data = fecha_con_guiones.strftime('%Y-%m-%d')
t = Time(data, format='isot',scale='utc')
t_sp=t.mjd
print(t_sp)

t_exp = 59192.99030668463

epoca0=t_sp-t_exp
print(epoca0)

z= 0.04717255

epoca=epoca0/(1+z)
print(epoca)

