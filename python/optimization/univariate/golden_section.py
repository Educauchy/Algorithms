#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:32:01 2018

@author: vadim
"""
from math import sqrt

def func(x):
    return (x - 2) ** 2 + 3

def golden(a, b):
    e = 0.001
    
    x1 = b - (b - a) / fib
    x2 = a + (b - a) / fib
    
    f1 = func(x1)
    f2 = func(x2)
    
    print("a: " + str(a) + "; b: " + str(b) + "; f1: " + str(f1) + "; f2: " + str(f2))
    
    if (f1 > f2):
        a = x1
    else:
        b = x2

    if (abs(b - a) < e):
        x = (a + b) / 2
        print("(" + str(round(x, 0)) + ", " + str(round(func(x), 0)) + ")")
    else:
        golden(a, b)
    
a = -5
b = 3
fib = (1 + sqrt(5)) / 2

golden(a, b)