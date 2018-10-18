#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:15:54 2018

@author: phil
"""
l_volts = []
l_amps = []
l_watts = []
l_ohms = []
def temp(v, a, w, o):
    l_volts.append(v)
    l_amps.append(a)
    l_watts.append(w)
    l_ohms.append(o)
    print(l_volts, l_amps, l_watts, l_ohms)
    