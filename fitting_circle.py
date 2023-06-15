def circle_fitting(xi, yi):
    M = np.array(
        [
            [np.sum(xi**2), np.sum(xi * yi), np.sum(xi)],
            [np.sum(xi * yi), np.sum(yi**2), np.sum(yi)],
            [np.sum(xi), np.sum(yi), 1 * len(xi)],
        ]
    )
    Y = np.array(
        [
            [-np.sum(xi**3 + xi * yi**2)],
            [-np.sum(xi**2 * yi + yi**3)],
            [-np.sum(xi**2 + yi**2)],
        ]
    )

    M_inv = np.linalg.inv(M)
    X = np.dot(M_inv, Y)
    a = -X[0] / 2
    b = -X[1] / 2
    r = np.sqrt((a**2) + (b**2) - X[2])
    return a, b, r
