import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots

from fitting_ellipse import calculate_params, get_major_and_minor_axis_endpoints
from helper import read_data


"""
result

0
h: -7.15874999999977e-05
k: 2.780312364420516e-17
a: 0.45398787949999997
b: 0.0080562835
phi: 3.141592653589793

10
h: 0.0026784707709689715
k: 0.0004722866639607984
a: 0.4439680195
b: 0.08431724333427472
phi: -2.9670597283903604

15:
h: 0.009939891911672188
k: -0.03669914566198677
a: 0.4345852868986664
b: 0.12687548750000002
phi: -2.8798139530449145

30:
h: -0.0002440953222344333
k: -0.00014092850000003987
a: 0.39026903600000007
b: 0.233719765
phi: -2.6179938779914944
"""

if __name__ == "__main__":
    # 2-2-0, 10, 15, 30
    lam_angle = "30"

    filename = "2-2-" + lam_angle + "-sqrt"

    print(filename)
    r, theta = read_data(filename)

    major_axis_endpoints, minor_axis_endpoints = get_major_and_minor_axis_endpoints(
        r, theta
    )

    print(major_axis_endpoints, minor_axis_endpoints)

    h, k, a, b, phi = calculate_params(major_axis_endpoints, minor_axis_endpoints)

    print("h:", h, "\nk:", k, "\na:", a, "\nb:", b, "\nphi:", phi)

    # h = 0
    # k = 0

    t = np.linspace(0, 2 * np.pi, 1000)
    x = h + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
    y = k + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)
    ellipse_r = np.sqrt(x**2 + y**2)
    ellipse_theta = np.arctan2(y, x)

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

    plt.savefig("./graph-for-consi/" + filename + "-polar-ellipse.png", format="png")
    # plt.show()
