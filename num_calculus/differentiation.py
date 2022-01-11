def first_derivative(function, x, dx): 
    return (function(x+dx)-function(x-dx))/(2*dx)