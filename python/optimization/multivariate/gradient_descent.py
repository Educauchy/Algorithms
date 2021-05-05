#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:04:43 2018

@author: vadim
"""

import random

def func(point, f):
    x, y = point
    if f == 1:
        return (1-x) ** 2 + 100 * (y - x ** 2) ** 2 # Rosenbrock
    elif f == 2:
        return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2 # Himmelblau
    elif f == 3:
        return (x - 4) ** 2 + y ** 2

def part_x(point, f):
    x, y = point
    if f == 1:
        return -2 + 2 * x - 400 * x * y + 400 * x ** 3
    elif f == 2:
        return 4 * x ** 3 + 2 * y ** 2 + 4 * x * y - 42 * x - 14
    elif f == 3:
        return 2 * x - 8
    
def part_y(point, f):
    x, y = point
    if f == 1:
        return 200 * y - 200 * x ** 2
    elif f == 2:
        return 4 * y ** 3 + 2 * x ** 2 + 4 * x * y - 26 * y - 22
    elif f == 3:
        return 2 * y
    
def output(point, f):
    x, y = point
    digits = 0
    return 'Point: (' + str((round(x, digits), round(y, digits))) + ', F: ' + str(round(f, 0))
    
def GD(init, f, iters = 0):
    rate = 0.000001 # learning rate
    accuracy = 0.00000000000001
    x, y = init

    x_new = x - rate * part_x(init, f)
    y_new = y - rate * part_y(init, f)
    init_new = (x_new, y_new)

    if abs(func(init, f) - func(init_new, f)) < accuracy or iters > 2000:
        return init_new
    else:
        return GD(init_new, f, iters + 1)

#Rosenbrock function
init = (1.1, 1.1)
x, y = GD(init, 1)
f = func((x, y), 1)
print(output((x,y), f) + '\n')

#Himmelblau function
results = []
for _ in range(100):
    init = (random.randint(-5, 5), random.randint(-5, 5))
    x, y = GD(init, 2)
    x = round(x, 2)
    y = round(y, 2)
    results.append((x, y))
results = set(results)
for _, point in enumerate(results):
    f = func(point, 2)
    print(output(point, f))