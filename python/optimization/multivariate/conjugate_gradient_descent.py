#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:33:12 2018

@author: vadim
"""

import numpy as np

def func(point):
    x, y = point
    #return (1-x) ** 2 + 100 * (y - x ** 2) ** 2 # Rosenbrog
    #return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2 # Himmelblau
    
