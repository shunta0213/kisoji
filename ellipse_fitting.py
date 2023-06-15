import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

from helper import calculate_center_and_axis_length, calculate_rotation


def plot_ellipse(major_axis_endpoints, minor_axis_endpoints):
    """
    Given the coordinates of the endpoints of the major and minor axis,
    this function plots the corresponding ellipse.
    """
    # Calculate centers, lengths, and rotation
    (
        major_center_x,
        major_center_y,
        major_axis_length,
    ) = calculate_center_and_axis_length(*major_axis_endpoints)
    (
        minor_center_x,
        minor_center_y,
        minor_axis_length,
    ) = calculate_center_and_axis_length(*minor_axis_endpoints)
    rotation = calculate_rotation(*major_axis_endpoints)

    # Plot ellipse
    fig, ax = plt.subplots()
    ellipse = patches.Ellipse(
        (major_center_x, major_center_y),
        major_axis_length,
        minor_axis_length,
        angle=rotation * 180 / math.pi,
        edgecolor="r",
        fc="None",
    )
    ax.add_patch(ellipse)

    ax.set_xlim(
        major_center_x - major_axis_length / 2 - 1,
        major_center_x + major_axis_length / 2 + 1,
    )
    ax.set_ylim(
        major_center_y - major_axis_length / 2 - 1,
        major_center_y + major_axis_length / 2 + 1,
    )
    ax.set_aspect("equal")

    return (
        plt,
        major_center_x,
        major_center_y,
        major_axis_length / 2,
        minor_axis_length / 2,
        rotation,
    )


def print_ellipse_equation(h, k, a, b, theta):
    """
    Given the parameters of a rotated ellipse, this function prints its equation.
    """
    print(
        f"The equation of the ellipse is: ((x-{h})*cos({theta}) + (y-{k})*sin({theta}))^2/{a**2} + ((x-{h})*sin({theta}) - (y-{k})*cos({theta}))^2/{b**2} = 1"
    )


# phi = 10
major_axis_endpoints = (0.439901619, 0.077566524, -0.434544677, -0.076621951)
minor_axis_endpoints = (-0.01488723, 0.084429677, 0.015941404, -0.082011412)


if __name__ == "__main__":
    plt, h, k, a, b, theta = plot_ellipse(major_axis_endpoints, minor_axis_endpoints)
    print_ellipse_equation(h, k, a, b, theta)
    plt.show()
