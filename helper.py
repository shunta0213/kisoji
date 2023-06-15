import numpy as np
import math
import pandas as pd
from scipy.interpolate import interp1d


def read_data(filename):
    df = pd.read_csv("./csv/" + filename + ".csv", delimiter=",", header=None)

    theta = df.iloc[:, 0].values
    r = df.iloc[:, 1].values
    theta = np.deg2rad(theta)
    return r, theta


def get_max_r_and_corresponding_theta(r, theta):
    """
    Given arrays of r and theta, this function returns the maximum r and its corresponding theta.
    """
    max_r_index = np.argmax(r)
    max_r = r[max_r_index]
    corresponding_theta = theta[max_r_index]
    return max_r, corresponding_theta


def find_extrema(r, theta):
    """
    Given arrays of r and theta, this function returns the values and corresponding thetas of local maxima and minima.
    """
    r_shifted_left = np.roll(r, -1)  # Shift array to the left
    r_shifted_right = np.roll(r, 1)  # Shift array to the right

    local_maxima_indices = (r > r_shifted_left) & (r > r_shifted_right)
    local_minima_indices = (r < r_shifted_left) & (r < r_shifted_right)

    return (
        np.array(r[local_maxima_indices]),
        np.array(theta[local_maxima_indices]),
        np.array(r[local_minima_indices]),
        np.array(theta[local_minima_indices]),
    )


def polar_to_cartesian(r, theta):
    """
    Given arrays of r and theta (in radians), this function returns corresponding x and y in Cartesian coordinates.
    """
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


def interleave_arrays(a, b):
    """
    This function takes in two numpy arrays of the same length and returns a new array
    that consists of elements from a and b taken alternately.
    """
    return np.ravel(np.column_stack((a, b)))


def calculate_rotation(x1, y1, x2, y2):
    """
    Given the coordinates of the two endpoints of the major axis,
    this function calculates the rotation angle of the ellipse.
    """
    return math.atan2((y2 - y1), (x2 - x1))


def calculate_center_and_axis_length(x1, y1, x2, y2):
    """
    Given the coordinates of the two endpoints of an axis,
    this function calculates the coordinates of the center and the length of the axis.
    """
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    axis_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return center_x, center_y, axis_length


def spline_interp(in_theta, in_r):
    out_theta = np.linspace(np.min(in_theta), np.max(in_theta), np.size(in_theta) * 100)
    func_spline = interp1d(in_theta, in_r, kind="cubic")
    out_r = func_spline(out_theta)
    return out_theta, out_r
