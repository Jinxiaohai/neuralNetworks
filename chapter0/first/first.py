#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


hello = tf.constant("hello Tensorflow")
sess = tf.Session()
print sess.run(hello)
a = tf.constant(10)
b = tf.constant(20)
print sess.run(a+b)
