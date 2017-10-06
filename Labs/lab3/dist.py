def dist(x,y):
    """Returns: The number line distance between x and y

    Example: dist(2,5) returns 3
    Example: dist(5,2) returns 3

    Parameter x: the starting point
    Precondition: x is a number
       
    Parameter y: the ending point
    Precondition: y is a number"""
       
    a = y-x
    if a < 0:
        b=-a
    else:
        b=a
    return b


