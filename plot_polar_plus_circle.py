from matplotlib import patches, pyplot as plt
import numpy as np
from helper import read_data, polar_to_cartesian
from fitting_circle import circle_fitting

"""
result:
a: -0.0003154726505443008
b: 0.00030219489885071184
rad: 0.32040401732139506
"""

if __name__ == "__main__":
    filename = "2-2-45-sqrt"

    print(filename)
    r, theta = read_data(filename)

    circle_x, circle_y = polar_to_cartesian(r, theta)
    a, b, rad = circle_fitting(circle_x, circle_y)

    print("a:", *a, "\nb:", *b, "\nrad:", *rad)

    t = np.linspace(0, 2 * np.pi, 1000)
    x = a + rad * np.cos(t)
    y = b + rad * np.sin(t)
    # Convert to polar coordinates
    circle_r = np.sqrt(x**2 + y**2)
    circle_theta = np.arctan2(y, x)

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
    ax.plot(circle_theta, circle_r)

    plt.show()
