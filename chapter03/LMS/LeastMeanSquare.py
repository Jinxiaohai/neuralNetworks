# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:27:25 2017

@author: Jagpreet Singh
"""

import numpy as num
import random as rand
import math
import matplotlib.pyplot as plt

size = int(8)
mu = 0.01
pii = math.pi

weights = num.zeros(shape = (size, 1))
input_sequence = num.zeros(shape = (size, 1))

iteration = 0
sq_error_array = []

while 1:
    iteration = iteration + 1
    print(iteration)
    
    sinx = num.sin((2*pii*iteration)/size)
    sinx = round(sinx, 2)
    
    sin3x = num.sin((6*pii*iteration)/size)
    sin3x = round(sin3x, 2)
    
    noise_amp = num.sqrt(abs(sinx)*0.001)
    noise_amp = round(noise_amp, 2)
    
    randomNumber = rand.random()-0.5
    noise = noise_amp*randomNumber
    noise = round(noise, 2)
    
    x = sinx + sin3x + noise
    x = round(x, 2)
    
    for i in range(0, size-1):
        temp = input_sequence[size-2-i, 0]
        input_sequence[size-1-i] = temp
    input_sequence[0, 0] = x
    output_sequence = input_sequence*weights
    output_sequence = num.round(output_sequence, 2)
    
    output_sum = num.sum(output_sequence)
    output_sum = round(output_sum, 2)
    
    error = sinx-output_sum
    error = round(error, 2)
    
    square_error = round(error**2, 2)
    
    weights = weights + 2*mu*input_sequence*error
    weights = num.round(weights, 2)
    
    sq_error_array.append(square_error)
    
    if iteration == 100:
        break
# print(sq_error_array)
plt.plot(sq_error_array)
plt.show()
