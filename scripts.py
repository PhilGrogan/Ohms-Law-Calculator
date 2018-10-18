#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:28:30 2018

@author: phil
"""
import calculate
import errors as er

def calc_clicked(volts, amps, watts, ohms):
    count = 0
    b_volts, count = is_float(volts, count)
    b_amps, count = is_float(amps, count)
    b_watts, count = is_float(watts, count)
    b_ohms, count = is_float(ohms, count)
    if count == 4:
        er.clear_error()
    elif count != 2:
        er.count_error()
    else:
        if b_volts == True and b_amps == True:
            watts = calculate.watts1(float(volts), float(amps))
            ohms = calculate.ohms1(float(volts), float(amps))
        elif b_volts == True and b_watts == True:
            amps = calculate.amps1(float(volts), float(watts))
            ohms = calculate.ohms1(float(volts), float(amps))
        elif b_volts == True and b_ohms == True:
            amps = calculate.amps2(float(volts), float(ohms))
            watts = calculate.watts1(float(volts), float(amps))
        elif b_amps == True and b_watts == True:
            volts = calculate.volts1(float(amps), float(watts))
            ohms = calculate.ohms1(float(volts), float(amps))
        elif b_amps == True and b_ohms == True:
            watts = calculate.watts2(float(amps), float(ohms))
            volts = calculate.volts1(float(amps), float(watts))
        elif b_ohms == True and b_watts == True:
            volts = calculate.volts2(float(ohms), float(watts))
            amps = calculate.amps1(float(volts), float(watts))
    return(volts, amps, ohms, watts)
        
        
        
def is_float(value, c):
    try:
        float(value)
        c += 1
        return True, c
    except:
        return False, c