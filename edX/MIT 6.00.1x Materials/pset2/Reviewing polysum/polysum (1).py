def polysum(numberOfSides, lengthOfSide):
    """
    numberOfSides: number of sides of the polygon
    lengthOfSide: length of each side
    
    Returns: The sum of the area and the squared perimeter of a polygon
    
    """
    
    #import the math library
    import math 

    #calcluate area
    area = (0.25*numberOfSides*(lengthOfSide**2))/math.tan(math.pi/numberOfSides)
    
    #calculate squared perimeter
    squaredPerimeter = (numberOfSides * lengthOfSide)**2
    
    #calculate the sum of area and squared perimeter, rounded to 4 decimals
    polySum=round(area+squaredPerimeter,4)
    
    return polySum

