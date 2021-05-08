# This method uses the newton-raphson-iteration-method
# The math behind it is quite simple
# https://en.wikipedia.org/wiki/Newton%27s_method

# It holds that: r_(n + 1) = r_n - f(r_n)/f'(r_n)
# Now we have to find a equation with the solution we want:
# Let say, we want to compute the square root of 2.
# x^2 - 2 = 0, +sqrt(2) and -sqrt(2) is a solution for that equation, we're only interested in the positive value

# It's boring to compute only square roots, so I want to implement a method, that can compute a the n root of a positive, real number.
# hence: x^n - value = 0
# now we have to build the derivative of this equation: n * x^(n - 1)
# in the end we will have something like this: result = result - (result ** exponent - value) / (exponent * result ** (exponent - 1))

def root(exponent: int, startValue: float, iterations: int, value: float):
    assert exponent > 0
    assert iterations != 0
    assert value > 0 # for the complex world, you have to add an i in the end, frankly I'm to lazy to implement that
    # That's trivial, to quote a teacher of mine.

    result = startValue - (startValue ** exponent - value) / (exponent * startValue ** (exponent - 1))

    for __ in range(0, iterations):
        result = result - (result ** exponent - value) / (exponent * result ** (exponent - 1))

    # in case something went wrong use abs
    return abs(result)


def sqrt(startValue: float, iterations: int, value: float):
    return root(2, startValue, iterations, value)


if __name__ == "__main__":
    print(root(5, 1, 10, 20))  # fifth root of 20 is approx. 1.82056
    print(root(2, 1, 10, 100))  # square root of 100 is 10
    print(root(3, 1, 10, 27))  # third root of 27 is 3

    # last but least the most beautiful square root
    print(root(2, 1, 10, 2))  # square root of 2 is approx. 1.41
