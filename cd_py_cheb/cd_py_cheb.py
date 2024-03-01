def chebyshev(order, x, data):
    # Evaluate a Chebyshev polynomial
    two_x = 2 * x
    bkp2 = data[order]
    bkp1 = two_x * bkp2 + data[order - 1]
    for n in range(order - 2, 0, -1):
        bk = data[n] + two_x * bkp1 - bkp2
        bkp2 = bkp1
        bkp1 = bk

    return data[0] + x * bkp1 - bkp2


def der_chebyshev(order, x, data):
    # Evaluate the derivative of a Chebyshev polynomial
    two_x = 2 * x
    bkp2 = order * data[order]
    bkp1 = two_x * bkp2 + (order - 1) * data[order - 1]
    for n in range(order - 2, 1, -1):
        bk = n * data[n] + two_x * bkp1 - bkp2
        bkp2 = bkp1
        bkp1 = bk
    return data[1] + two_x * bkp1 - bkp2
