import sys

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib import rc
import scienceplots
from helper import spline_interp

# requires latex


def arg_data():
    arg = sys.argv
    if len(arg) != 2:
        print("invalid arguments")
        print(arg)
        exit(1)
    return arg[1]


def plot(name, theta, i, popt):
    fig, p = plt.subplots(1, 1, sharex=True)
    p.plot(
        theta,
        i,
        "o",
        markersize=3,
        markeredgewidth=0.0,
        fillstyle="full",
    )

    theta2, i2 = spline_interp(theta, fit_func(theta, *popt))

    p.plot(theta2, i2, color="black")
    p.set(xlabel=x_label)
    p.set(ylabel=y_label)
    # plt.show()
    plt.savefig(name, format="png")


def custom_params(data):
    if data == "1":
        x_label = r"angle of 'kenko-ban' $\theta$ /degree"
        filename = "./csv/1.csv"
        param_init = [0.2, 1, 0]

        def fit_func(x, a, b, c):
            # [ 0.20555135  0.99874721 -0.02353551]
            # [0.00069022 0.00329661 0.00251298]
            return (
                a
                * np.cos(b * (x / 180 * np.pi - c))
                * np.cos(b * (x / 180 * np.pi - c))
            )

    elif data == "2-1":
        x_label = r"angle of '$\lambda/4$-ban' $\phi$ /degree"
        filename = "./csv/2-1.csv"
        param_init = [0.2, 1.5]

        def fit_func(x, a, b):
            # [0.20643363 1.57594805]
            # [0.00046881 0.00572144]
            return a * (
                1
                - np.sin(2 * x * np.pi / 180)
                * np.sin(2 * x * np.pi / 180)
                * np.sin(b / 2)
                * np.sin(b / 2)
            )

    elif data == "2-1-90":
        x_label = r"angle of '$\lambda/4$-ban' $\phi$ /degree"
        filename = "./csv/2-1-90.csv"
        param_init = [0.1]

        # a  * (1 - np.sin(b / 2) * np.sin(b / 2))が係数であり、a, bが任意の値を取れる。
        def fit_func(x, a):
            # [0.10358179]
            # [0.00031036]
            return (
                a
                * np.sin(2 * x * np.pi / 180)
                * np.sin(2 * x * np.pi / 180)
                # * (1 - np.sin(b / 2) * np.sin(b / 2))
            )

    else:
        print("invalid data name: " + data)
        exit(1)

    return x_label, filename, param_init, fit_func


if __name__ == "__main__":
    data = arg_data()

    x_label, filename, param_init, fit_func = custom_params(data)
    y_label = r"electric current \textit{I}/mA"

    # graph style
    plt.style.use(["science", "no-latex", "ieee"])
    # font in graph
    rc("text", usetex=True)

    df = pd.read_csv(filename, delimiter=",", header=None)
    theta = df.iloc[:, 0].values
    i = df.iloc[:, 1].values

    popt, pcov = curve_fit(fit_func, theta, i, p0=param_init)
    perr = np.sqrt(np.diag(pcov))
    print("popt:")
    print(popt)
    print("perr:")
    print(perr)

    path = "./graph-for-consi/" + data + "-fit-curve.png"
    print("exporting image to: " + path)
    plot(path, theta, i, popt)
    print("finished")
