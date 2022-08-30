import math
import numpy as np
import matplotlib.pyplot as plt

'''
A function to draw a curve that looks like
the infinity symbol
'''


def make_figure():
    omega = np.arange((-0.5 * np.pi), (1.5 * np.pi), 0.1)
    curve = plt.figure()
    axes = curve.add_axes([0, 0, 1, 1])
    axes.plot(0.5 * np.cos(omega), np.sin(omega)*np.cos(omega), color='red')
    return curve
