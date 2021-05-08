import random
import math


# The math behind all this is quite simple.
# At first we have a rectangle of length and width r, so the area is r^2
# In this rectangle there is a fourth circle with the radius r, assume for the rest that r = 1
# So, now we guess, let say 1000 points in this area with a random function, between 0 and 1
# According to the laws of probability, we will hit the circle a few times more, than the corner of the rectangle outside the circle,
# so it is only logical that the ratio of the points in the circle and the total points converges to pi/4,
# hence the ratio of the areas is exactly pi/4, the only thing we have do to is multiply by 4 to get pi.

# pi/4 = (1/4 * pi * r^2)/(r^2)
# pi/4 = (pi * r^2)/(r^2 * 4)
# pi/4 = (pi)/(4)

# There's a other commonly interpretation of this problem. Use a square with sidelength of 2r and a circle with radius r.
# This makes it a little bit more complicate to implement, so I simplified the problem.


def approximate_pi(points: int):
    assert points != 0

    circle = 0

    for __ in range(0, points):
        if math.sqrt(math.pow(random.uniform(0, 1), 2) + math.pow(random.uniform(0, 1), 2)) <= 1:  # use the
            # pythagorean theorem, to calculate the distance
            # for a computer scientist is the square root here not needed, because the square root of a number bigger
            # than one, is always greater than one. The program with out the square root would be more efficient, but for a guy
            # who loves math is the square root required!!!

            circle = circle + 1

    return circle / points * 4


if __name__ == "__main__":
    print(approximate_pi(10000))  # will approximately return pi. run it a few times to be sure, the accuracy increases
    # when you increase points
