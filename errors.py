#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:35:31 2018

@author: phil
"""
import OhmsLawGui as root


def count_error():
    print("count error")
    root.Ui_MainWindow.error_message(root, text='Enter two values!')
    
def clear_error():
    print("clear error")
    root.Ui_MainWindow.error_message(root, text='Too many values!')