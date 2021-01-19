# Above line tells the notebook to treat the rest of this
# cell as content for a file on disk.
import math

import numpy as np
import matplotlib.pyplot as plt


def make_figure():
    theta = np.arange(0, 4 * math.pi, 0.1)
    eight = plt.figure()
    axes = eight.add_axes([0, 0, 1, 1])
    axes.plot(0.5 * np.sin(theta), np.cos(theta / 2))
    return eight
