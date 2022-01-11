def first_derivative( function, x, dx ):
    """ Calculates first derivative numerically, with error h^2

    Args:
        function : function to be detivated
        x : point in which derivated
        dx : length of interval

    Returns:
        numerical value for first derivative
    """    
    return (function(x+dx)-function(x-dx))/(2*dx)