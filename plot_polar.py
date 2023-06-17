import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import pandas as pd

from helper import spline_interp, read_data

"""
- normal
1, 1-expanded, 2-1, 2-1-90, 2-2-0, 10, 15, 30, 45
- sqrt
"""
filename = "2-2-15"

if __name__ == "__main__":
    r, theta = read_data(filename)

    theta2, r2 = spline_interp(theta, r)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(theta, r, "o")
    ax.plot(theta2, r2)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    angles = np.linspace(0, 360, 12, endpoint=False)
    ax.set_thetagrids(angles, fontsize=12)

    # TODO select grids
    # for normal
    ax.set_rlim(0, 0.25)
    ax.set_rgrids(np.linspace(0, 0.25, 6), angle=75)
    # for sqrt
    # ax.set_rlim(0, 0.5)
    # ax.set_rgrids(np.linspace(0, 0.5, 6), angle=75)

    # TODO fix dist path
    # plt.savefig("./graph-for-consi/" + filename + "-polar.png", format="png")
    plt.show()
