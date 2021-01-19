import matplotlib.pyplot as plt
from numpy import sum, array
from numpy.random import randint, choice



class MonteCarlo:
    """ A simple Monte Carlo implementation """

    def __init__(self, energy, density, temperature=1, itermax=1000):
        from numpy import any, array
        density = array(density)
        self.itermax = itermax

        if temperature == 0:
            raise NotImplementedError(
                "Zero temperature not implemented")
        if temperature < 0e0:
            raise ValueError(
                "Negative temperature makes no sense")

        if len(density) < 2:
            raise ValueError("Density is too short")
        # of the right kind (integer). Unless it is zero length,
        # in which case type does not matter.
        if density.dtype.kind != 'i' and len(density) > 0:
            raise TypeError("Density should be an array of *integers*.")
        # and the right values (positive or null)
        if any(density < 0):
            raise ValueError("Density should be an array of" +
                             "*positive* integers.")
        if density.ndim != 1:
            raise ValueError("Density should be an a *1-dimensional*" +
                             "array of positive integers.")
        if sum(density) == 0:
            raise ValueError("Density is empty.")

        self.current_energy = energy(density)
        self.temperature = temperature
        self.density = density

    def random_direction(self): return choice([-1, 1])

    def random_agent(self, density):
        # Particle index
        particle = randint(sum(density))
        current = 0
        for location, n in enumerate(density):
            current += n
            if current > particle:
                break
        return location

    def change_density(self, density):
        """ Move one particle left or right. """

        location = self.random_agent(density)

        # Move direction
        if(density[location]-1 < 0):
            return array(density)
        if location == 0:
            direction = 1
        elif location == len(density) - 1:
            direction = -1
        else:
            direction = self.random_direction()

        # Now make change
        result = array(density)
        result[location] -= 1
        result[location + direction] += 1
        return result

    def accept_change(self, prior, successor):
        """ Returns true if should accept change. """
        from numpy import exp
        from numpy.random import uniform
        if successor <= prior:
            return True
        else:
            return exp(-(successor - prior) / self.temperature) > uniform()

    def step(self):
        iteration = 0
        while iteration < self.itermax:
            new_density = self.change_density(self.density)
            new_energy = energy(new_density)

            accept = self.accept_change(self.current_energy, new_energy)
            if accept:
                self.density, self.current_energy = new_density, new_energy
            iteration += 1

        return self.current_energy, self.density


def energy(density, coefficient=1):
    """ Energy associated with the diffusion model
        :Parameters:
        density: array of positive integers
        Number of particles at each position i in the array/geometry
    """
    from numpy import array, any, sum

    # Make sure input is an array
    density = array(density)

    # of the right kind (integer). Unless it is zero length, in which case type does not matter.
    if density.dtype.kind != 'i' and len(density) > 0:
        raise TypeError("Density should be an array of *integers*.")
    # and the right values (positive or null)
    if any(density < 0):
        raise ValueError("Density should be an array" +
                         "of *positive* integers.")
    if density.ndim != 1:
        raise ValueError("Density should be an a *1-dimensional*" +
                         "array of positive integers.")

    return coefficient * 0.5 * sum(density * (density - 1))
