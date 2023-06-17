import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

from fitting_ellipse import calculate_params_origin, get_major_and_minor_axis_endpoints
from helper import read_data, find_extrema, polar_to_cartesian


"""
result
15:
h: 0.009939891911672188
k: -0.03669914566198677
a: 0.4345852868986664
b: 0.12687548750000002
phi: -2.8798139530449145

"""

if __name__ == "__main__":
    # 15
    lam_angle = "15"

    filename = "2-2-" + lam_angle + "-sqrt"

    print(filename)
    r, theta = read_data(filename)

    major_axis_endpoints, minor_axis_endpoints = get_major_and_minor_axis_endpoints(
        r, theta
    )

    a, b, phi = calculate_params_origin(major_axis_endpoints, minor_axis_endpoints)

    print("\na:", a, "\nb:", b, "\nphi:", phi)

    # h = 0
    # k = 0

    t = np.linspace(0, 2 * np.pi, 1000)
    x = a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
    y = a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)
    ellipse_r = np.sqrt(x**2 + y**2)
    ellipse_theta = np.arctan2(y, x)

    # ellipse_maxima, minima
    (
        ellipse_maxima,
        ellipse_maxima_theta,
        ellipse_minima,
        ellipse_minima_theta,
    ) = find_extrema(r, theta)

    print(
        ellipse_maxima,
        ellipse_maxima_theta * 180 / np.pi,
        ellipse_minima,
        ellipse_minima_theta * 180 / np.pi,
    )

    # Plot Config
    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    angles = np.linspace(0, 360, 12, endpoint=False)
    ax.set_thetagrids(angles, fontsize=12)
    ax.set_rlim(0, 0.5)
    ax.set_rgrids(np.linspace(0, 0.5, 6), angle=75)

    ax.plot(theta, r, "o")
    ax.plot(ellipse_theta, ellipse_r, label="the shape of polarization")

    # legends
    angle = np.deg2rad(67.5)
    ax.legend(
        loc="lower left",
        bbox_to_anchor=(0.5 + np.cos(angle) / 2, 0.55 + np.sin(angle) / 2),
    )

    plt.savefig(
        "./graph-for-consi/" + filename + "-polar-ellipse-with-center-at-origin.png",
        format="png",
    )
    # plt.show()
