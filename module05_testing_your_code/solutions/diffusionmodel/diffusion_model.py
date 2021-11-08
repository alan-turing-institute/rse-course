"""  Simplistic 1-dimensional diffusion model """


def energy(density, coefficient=1):
    """Energy associated with the diffusion model

    :Parameters:
      density: array of positive integers
         Number of particles at each position i in the array/geometry
    """
    from numpy import array, any, sum

    # Make sure input is an array
    density = array(density)

    # of the right kind (integer). Unless it is zero length, in which case type does not matter.
    if density.dtype.kind != "i" and len(density) > 0:
        raise TypeError("Density should be an array of *integers*.")
    # and the right values (positive or null)
    if any(density < 0):
        raise ValueError("Density should be an array of *positive* integers.")
    if density.ndim != 1:
        raise ValueError(
            "Density should be an a *1-dimensional* array of positive integers."
        )

    return coefficient * 0.5 * sum(density * (density - 1))


def partial_derivative(function, x, index):
    """Computes right derivative of function over integers

    :Parameters:
       function: callable object
         The function for which to compute the delta/derivative
       x: array of integers
         The point at which to compute the right-derivative
       index: integer
         Partial derivative direction.
    """
    from numpy import array

    # Computes left value
    left_value = function(x)

    # Copies and modifies x. Could do it without copy, but that complicates mocking.
    x = array(x)
    x[index] += 1
    right_value = function(x)

    return right_value - left_value
