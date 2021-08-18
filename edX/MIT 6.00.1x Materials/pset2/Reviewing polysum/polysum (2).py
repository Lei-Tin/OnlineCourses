import math
"""
Optional Problem
"""
"""A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:  0.25∗n∗s^2 / tan(π/n) 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular 
polygon. The function returns the sum, rounded to 4 decimal places."""


def polysum(n, s):
    """
    Sums the area and square of the perimeter of a regular
    polygon.

    :param n: number of sides
    :param s: length of side
    :return: sum of area and perimeter squared, rounded to 4 decimal places.
    """
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    perimeter = (s * n)

    return round(area + perimeter ** 2, 4)
