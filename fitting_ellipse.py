from helper import (
    calculate_center_and_axis_length,
    calculate_rotation,
    find_extrema,
    polar_to_cartesian,
    interleave_arrays,
)


def get_major_and_minor_axis_endpoints(r, theta):
    maxima, maxima_theta, minima, minima_theta = find_extrema(r, theta)
    maxima_x, maxima_y = polar_to_cartesian(maxima, maxima_theta)
    minima_x, minima_y = polar_to_cartesian(minima, minima_theta)

    major_axis_points = interleave_arrays(maxima_x, maxima_y)
    minor_axis_points = interleave_arrays(minima_x, minima_y)
    return major_axis_points, minor_axis_points


def calculate_params(major_axis_endpoints, minor_axis_endpoints):
    """
    calculate ellipse parameters
    ((x-{h})*cos({theta}) + (y-{k})*sin({theta}))^2/{a**2} + ((x-{h})*sin({theta}) - (y-{k})*cos({theta}))^2/{b**2} = 1
    """
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

    return (
        major_center_x,
        major_center_y,
        major_axis_length / 2,
        minor_axis_length / 2,
        rotation,
    )
