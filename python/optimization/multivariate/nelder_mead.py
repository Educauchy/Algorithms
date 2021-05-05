#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:53:46 2018

@author: vadim
"""

import numpy as np
import random

def func(point, f):
    x, y = point
    if f == 1:
        return (1-x) ** 2 + 100 * (y - x ** 2) ** 2 # Rosenbrock
    elif f == 2:
        return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2 # Himmelblau
    elif f == 3:
        return (x - 4) ** 2 + y ** 2
    
def output(point, f):
    x, y = point
    digits = 3
    return 'Point: (' + str((round(x, digits), round(y, digits))) + ', F: ' + str(round(f, 0))
    
def mid(points):
    p1 = np.array(points[0])
    p2 = np.array(points[1])
    return (p1 + p2) / 2
    
def reflect(m, alfa, w):
    m = np.array(m, float)
    w = np.array(w, float)
    return m + alfa * (m - w)
    
def expand(m, gamma, xr):
    m = np.array(m, float)
    return m + gamma * (xr - m)
    
def contract(m, beta, w):
    m = np.array(m, float)
    w = np.array(w, float)
    return m + beta * (w - m)

def shrink(points, delta):
    b = np.array(points[0], float)
    g = np.array(points[1], float)
    w = np.array(points[2], float)
    g_new = b + delta * (g - b)
    w_new = b + delta * (w - b)
    return (g_new, w_new)

def NM(points, f, counter = 0, iters = 100):
    alfa, beta, gamma = 1, 0.5, 2
    fu = {
        'v1': (points[0], func(points[0], f)),
        'v2': (points[1], func(points[1], f)),
        'v3': (points[2], func(points[2], f))
    }
    points_sort = sorted(fu.items(), key=lambda x: x[1][1])
    b, g, w = points_sort[0][1][0], points_sort[1][1][0], points_sort[2][1][0]

    m = mid((b, g))
    
    #reflection
    r = reflect(m, alfa, w)
    if func(r, f) < func(g, f):
        if func(b, f) < func(r, f):
            w = r
        else:
            #expansion
            e = expand(m, gamma, r)
        
            if func(e, f) < func(b, f):
                w = e
            else:
                w = r
    else:
        if func(r, f) < func(w, f):
            w = r
        
        #contract
        c = contract(m, beta, w)
        if func(c, f) < func(w, f):
            w = c
        else:
            #shrink
            w = mid((b, w))
            g = m
      
    g = tuple(g)
    w = tuple(w)

    if counter > iters:
        return b
    else:
        return NM([b, g, w], f, counter + 1)

#Rosenbrock function
init = [(10, 9), (10, -2), (21, 1)]
x, y = NM(init, 1)
f = func((x, y), 1)
print(output((x,y), f) + '\n')

#Himmelblau function
results = []
for _ in range(100):
    init = [(random.randint(-30, 30), random.randint(-30, 30)) for _ in range(3)]
    x, y = NM(init, 2)
    x = round(x, 2)
    y = round(y, 2)
    results.append((x, y))
results = set(results)
for _, point in enumerate(results):
    f = func(point, 2)
    print(output(point, f))
