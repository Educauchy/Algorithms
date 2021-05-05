#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:49:01 2018

@author: vadim
"""

def func(x):
    return (x - 2) ** 2 + 3

def dichotomy(a, b):
    e = 0.001
    x = (a + b) / 2
    f1 = func(x - e)
    f2 = func(x + e)

    print("a: " + str(a) + "; b: " + str(b) + "; x: " + str(x) + "; f1: " + str(f1) + "; f2: " + str(f2))
    
    if (f2 < f1):
        a = x
    else:
        b = x
    
    if (abs(b - a) < e):
        x = (a + b) / 2
        print("(" + str(round(x, 0)) + ", " + str(round(func(x), 0)) + ")")
    else:
        dichotomy(a, b)

a = -5
b = 3

dichotomy(a, b)