class MonteCarlo:
    """ A simple Monte Carlo implementation """

    def __init__(self, temperature=100, itermax=100):

        if temperature == 0:
            raise NotImplementedError("Zero temperature not implemented")
        if temperature < 0e0:
            raise ValueError("Negative temperature makes no sense")

        self.temperature = temperature
        """ Temperature at which to run simulation """
        self.itermax = itermax
        """ Maximum number of iterations """

    def change_density(self, density):
        """ Move one particle left or right. """
        from numpy import sum, array
        from numpy.random import randint, choice

        # Particle index
        particle = randint(sum(density))
        # Location
        current = 0
        for location, n in enumerate(density):
            current += n
            if n > particle:
                break

        # Move direction
        if location == 0:
            direction = 1
        elif location == len(density) - 1:
            direction = -1
        else:
            direction = choice([-1, 1])

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
        return exp(-(successor - prior) / self.temperature) > uniform()

    def __call__(self, energy, density):
        """ Runs Monte-carlo """
        from numpy import any, array

        density = array(density)
        if len(density) < 2:
            raise ValueError("Density is too short")
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
        if sum(density) == 0:
            raise ValueError("Density is empty.")

        iteration = 0
        current_energy = energy(density)
        while iteration < self.itermax or self.itermax < 0:

            new_density = self.change_density(density)
            new_energy = energy(new_density)

            accept = self.accept_change(current_energy, new_energy)
            if accept:
                density, current_energy = new_density, new_energy

            if not self.observe(iteration, accept, density, current_energy):
                break

            iteration += 1

    def observe(self, iteration, accepted, density, energy):
        """Called at every step to observe simulation.

        :returns: True if simulation should keep going.
        """
        return True
