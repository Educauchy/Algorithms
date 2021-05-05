#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 12:30:58 2018

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

def J(point, f):
    x, y = point
    if f == 1:
        return (np.array([[-2 + 2 * x - 400 * x * y + 400 * x ** 3],
                          [200 * y - 200 * x ** 2]], dtype = 'float')).reshape(2, 1)
    elif f == 2:
        return (np.array([[4 * x ** 3 + 2 * y ** 2 + 4 * x * y - 42 * x - 14],
                          [4 * y ** 3 + 2 * x ** 2 + 4 * x * y - 26 * y - 22]], dtype = 'float')).reshape(2, 1)
    elif f == 3:
        return 2 * x - 8
    
def H(point, f):
    x, y = point

    if f == 1:
        return np.matrix([[1200 * x ** 2 - 400 * y + 2, -400 * x],
                          [-400 * x, 200]], dtype = 'float')
    elif f == 2:
        return np.matrix([[12 * x ** 2 + 4 * x - 42, 4 * y + 4 * x],
                          [4 * x + 4 * y, 12 * y ** 2 + 4 * x - 26]], dtype = 'float')
    elif f == 3:
        return 2 * x - 8
 
def output(point, f):
    x, y = point
    digits = 3
    return 'Point: (' + str((round(x, digits), round(y, digits))) + ', F: ' + str(round(f, 0))
    
def QN(point, f, iters = 0):
    point_next = np.squeeze(np.asarray((np.subtract(
                    point,
                        np.dot(
                                np.linalg.inv(H(point, f)),
                                J(point, f)))
                ).reshape(1, 2)))
    
    if iters < 30:
        return QN(point_next.reshape(2, 1), f, iters + 1)
    else:
        return point_next


# Rosenbrock
init = (np.array([4, 5], dtype = 'float')).reshape(2, 1)
r_point = QN(init, 1)
print(output(r_point, func(r_point, 1)) + '\n')

# Himmelblau
results = []
for _ in range(100):
    init = (np.array([random.randint(-30, 30), random.randint(-30, 30)], dtype = 'float')).reshape(2, 1)
    x, y = QN(init, 2)
    x = round(x, 2)
    y = round(y, 2)
    results.append((x, y))
results = set(results)
for _, point in enumerate(results):
    f = func(point, 2)
    print(output(point, f))