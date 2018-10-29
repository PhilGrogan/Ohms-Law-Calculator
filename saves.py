#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:15:54 2018

@author: phil
"""
import pandas as pd
import datetime as dt
from pathlib import Path
from openpyxl import load_workbook

l_volts = []
l_amps = []
l_watts = []
l_ohms = []
def temp(v, a, w, o):
    l_volts.append(v)
    l_amps.append(a)
    l_watts.append(w)
    l_ohms.append(o)
    
def save():
    df = pd.DataFrame({"Volts":l_volts, "Amps":l_amps, "Watts":l_watts, "Ohms":l_ohms})
    home = str(Path.home())
    file = home + "/OhmsLaw.xlsx"
    if not Path(file).exists():
        writer = pd.ExcelWriter(file, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=str(dt.datetime.now().strftime("%Y-%m-%d-%H%M")), index=False)
        writer.save()
        writer.close()
    
    else:
        book = load_workbook(file)
        writer = pd.ExcelWriter(file, engine='openpyxl')
        writer.book = book
        df.to_excel(writer, sheet_name=str(dt.datetime.now().strftime("%Y-%m-%d-%H%M")), index=False)
        writer.save()
        writer.close()
    l_volts.clear()
    l_amps.clear()
    l_watts.clear()
    l_ohms.clear()
    
def delete():
    l_volts.clear()
    l_amps.clear()
    l_watts.clear()
    l_ohms.clear()
    
   
    
