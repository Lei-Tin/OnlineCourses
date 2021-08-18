from math import pi, tan

def polysum(n, s):
    '''
    Input [Regular polygon]
        n = number of sides
        s = lenght of side
    Returns the sum of the area and the square of the perimeter
    '''
    area = 0.25 * n * s ** 2 / tan(pi/n)
    sq_p = (n * s)**2
    s = area + sq_p
    return round(s, 4)
