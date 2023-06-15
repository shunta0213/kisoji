import numpy as np
import pandas as pd
from helper import get_major_and_minor_axis_endpoints, calculate_params
import matplotlib.pyplot as plt
import scienceplots

if __name__ == "__main__":
    # 2-2-0, 10, 15, 30
    lam_angle = "15"

    filename = "2-2-" + lam_angle + "-sqrt"
    print(filename)
    df = pd.read_csv("./csv/" + filename + ".csv", delimiter=",", header=None)

    theta = df.iloc[:, 0].values
    r = df.iloc[:, 1].values
    theta = np.deg2rad(theta)
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
    ax.plot(ellipse_theta, ellipse_r)

    plt.show()
