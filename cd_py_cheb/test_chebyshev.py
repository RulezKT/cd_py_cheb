from chebyshev import chebyshev, der_chebyshev


def test_chebyshev():
    assert chebyshev(3, 0.5, [1, 2, 3, 4]) == -3.5


def test_der_chebyshev():
    assert der_chebyshev(3, 0.5, [1, 2, 3, 4]) == 8
