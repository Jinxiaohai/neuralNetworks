#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


x = tf.placeholder("float", shape=[None, 1])

W = tf.Variable(tf.zeros([1, 1]))
b = tf.Variable(tf.zeros([1]))

y = tf.matmul(x, W) + b
y_ = tf.placeholder("float", [None, 1])

cost = tf.reduce_sum(tf.pow((y-y_), 2))

tran_step = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

All_x = np.empty(shape=[1, 1])
All_y = np.empty(shape=[1, 1])

for i in range(1000):
    x_s = np.random.rand(1, 1)

    y_s = np.dot([[0.33]], np.random.rand(1, 1)) + 0.33

    feed = {x: x_s, y_: y_s}
    sess.run(tran_step, feed_dict=feed)

    All_x = np.concatenate((All_x, x_s))
    All_y = np.concatenate((All_y, y_s))

print All_x
print All_y
