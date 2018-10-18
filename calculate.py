#!/usr/bin/env python3
"""
watts = volts * amps
watts = amps ** 2 * ohms
watts = sqrt(watts * ohms)
ohms = volts / amps
ohms = volts ** 2 / watts
ohms = watts / amsp ** 2
volts = watts / amps
volts = amps * ohms
volts = sqrt(watts * ohms)
amps = watts / volts
amps = volts / ohms
amps = sqrt(watts / ohms)
"""
from math import sqrt

def volts1(a, w):
    return(w/a)
    
def watts1(v, a):
    return(v*a)

def ohms1(v, a):
    return(v/a)

def amps1(v, w):
    return(w/v)

def amps2(v, o):
    return(v/o)

def watts2(a, o):
    return(a**2 * o)
    
def volts2(o, w):
    return(sqrt(o*w))