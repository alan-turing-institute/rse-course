#!/usr/bin/env python
# coding: utf-8

# # Recap example: Monte-Carlo

# ## Problem: Implement and test a simple Monte-Carlo algorithm
# 
# Given an input function (energy) and starting point (density) and a temperature $T$: 
# 
# 1. Compute energy at current density.
# 1. Move randomly chosen agent randomly left or right.
# 1. Compute second energy.
# 1. Compare the two energies:
# 1. If second energy is lower, accept move.
# 1. $\beta$ is a parameter which determines how likely
#    the simulation is to move from a 'less favourable' situation to a 'more favourable' one.
# 1. Compute $P_0=e^{-\beta (E_1 - E_0)}$ and $P_1$ a random number between 0 and 1,
# 1. If $P_0 > P_1$, do the move anyway.
# 1. Repeat.

# * the algorithm should work for (m)any energy function(s).
# * there should be separate tests for separate steps! What constitutes a step?
# * tests for the Monte-Carlo should not depend on other parts of code.
# * Use [matplotlib](http://matplotlib.org/) to plot density at each iteration, and make an animation

# **NB.** If you are using the Windows command prompt, you will have to replace all `%%bash` directives in this notebook with `%%cmd` 

# ## Solution

# We need to break our problem down into pieces:

# 1. A function to generate a random change: `random_agent()`, `random_direction()`
# 1. A function to compute the energy before the change and after it: `energy()`
# 1. A function to determine the probability of a change given the energy difference (1 if decreases, otherwise based on exponential): `change_density()`
# 1. A function to determine whether to execute a change or not by drawing a random number`accept_change()`
# 1. A method to iterate the above procedure: `step()`

# Next Step: Think about the possible unit tests

# 1. Input insanity: e.g. density should non-negative integer; testing by giving negative values etc.
# 1. `change_density()`: density is change by a particle hopping left or right? Do all positions have an equal chance of moving?
# 1. `accept_change()` will move be accepted when second energy is lower?
# 1. Make a small test case for the main algorithm. (Hint: by using mocking, we can pre-set who to move where.)

# In[1]:


get_ipython().run_cell_magic('bash', '', 'rm -rf DiffusionExample\nmkdir DiffusionExample\n')


# **Windows:** You will need to run the following instead
#     
# ```cmd
# %%cmd
# rmdir /s DiffusionExample
# mkdir DiffusionExample
# ```

# In[2]:


get_ipython().run_cell_magic('writefile', 'DiffusionExample/MonteCarlo.py', 'import matplotlib.pyplot as plt\nfrom numpy import sum, array\nfrom numpy.random import randint, choice\n\n\nclass MonteCarlo:\n    """A simple Monte Carlo implementation"""\n\n    def __init__(self, energy, density, temperature=1, itermax=1000):\n        from numpy import any, array\n\n        density = array(density)\n        self.itermax = itermax\n\n        if temperature == 0:\n            raise NotImplementedError("Zero temperature not implemented")\n        if temperature < 0e0:\n            raise ValueError("Negative temperature makes no sense")\n\n        if len(density) < 2:\n            raise ValueError("Density is too short")\n        # of the right kind (integer). Unless it is zero length,\n        # in which case type does not matter.\n        if density.dtype.kind != "i" and len(density) > 0:\n            raise TypeError("Density should be an array of *integers*.")\n        # and the right values (positive or null)\n        if any(density < 0):\n            raise ValueError("Density should be an array of" + "*positive* integers.")\n        if density.ndim != 1:\n            raise ValueError(\n                "Density should be an a *1-dimensional*" + "array of positive integers."\n            )\n        if sum(density) == 0:\n            raise ValueError("Density is empty.")\n\n        self.current_energy = energy(density)\n        self.temperature = temperature\n        self.density = density\n\n    def random_direction(self):\n        return choice([-1, 1])\n\n    def random_agent(self, density):\n        # Particle index\n        particle = randint(sum(density))\n        current = 0\n        for location, n in enumerate(density):\n            current += n\n            if current > particle:\n                break\n        return location\n\n    def change_density(self, density):\n        """Move one particle left or right."""\n\n        location = self.random_agent(density)\n\n        # Move direction\n        if density[location] - 1 < 0:\n            return array(density)\n        if location == 0:\n            direction = 1\n        elif location == len(density) - 1:\n            direction = -1\n        else:\n            direction = self.random_direction()\n\n        # Now make change\n        result = array(density)\n        result[location] -= 1\n        result[location + direction] += 1\n        return result\n\n    def accept_change(self, prior, successor):\n        """Returns true if should accept change."""\n        from numpy import exp\n        from numpy.random import uniform\n\n        if successor <= prior:\n            return True\n        else:\n            return exp(-(successor - prior) / self.temperature) > uniform()\n\n    def step(self):\n        iteration = 0\n        while iteration < self.itermax:\n            new_density = self.change_density(self.density)\n            new_energy = energy(new_density)\n\n            accept = self.accept_change(self.current_energy, new_energy)\n            if accept:\n                self.density, self.current_energy = new_density, new_energy\n            iteration += 1\n\n        return self.current_energy, self.density\n\n\ndef energy(density, coefficient=1):\n    """Energy associated with the diffusion model\n    :Parameters:\n    density: array of positive integers\n    Number of particles at each position i in the array/geometry\n    """\n    from numpy import array, any, sum\n\n    # Make sure input is an array\n    density = array(density)\n\n    # of the right kind (integer). Unless it is zero length, in which case type does not matter.\n    if density.dtype.kind != "i" and len(density) > 0:\n        raise TypeError("Density should be an array of *integers*.")\n    # and the right values (positive or null)\n    if any(density < 0):\n        raise ValueError("Density should be an array" + "of *positive* integers.")\n    if density.ndim != 1:\n        raise ValueError(\n            "Density should be an a *1-dimensional*" + "array of positive integers."\n        )\n\n    return coefficient * 0.5 * sum(density * (density - 1))\n')


# In[3]:


import sys

sys.path.append("DiffusionExample")
from MonteCarlo import MonteCarlo, energy
import numpy as np
import numpy.random as random
from matplotlib import animation
from matplotlib import pyplot as plt
from IPython.display import HTML


Temperature = 0.1

density = [np.sin(i) for i in np.linspace(0.1, 3, 100)]
density = np.array(density) * 100
density = density.astype(int)

fig = plt.figure()
ax = plt.axes(xlim=(-1, len(density)), ylim=(0, np.max(density) + 1))
image = ax.scatter(range(len(density)), density)
txt_energy = plt.text(0, 100, "Energy = 0")
plt.xlabel("Temperature = 0.1")
plt.ylabel("Energy Density")


mc = MonteCarlo(energy, density, temperature=Temperature)


def simulate(step):
    energy, density = mc.step()
    image.set_offsets(np.vstack((range(len(density)), density)).T)
    txt_energy.set_text("Energy = {}".format(energy))


anim = animation.FuncAnimation(fig, simulate, frames=200, interval=50)
HTML(anim.to_jshtml())


# In[4]:


get_ipython().run_cell_magic('writefile', 'DiffusionExample/test_model.py', 'from MonteCarlo import MonteCarlo\nfrom unittest.mock import MagicMock\nfrom pytest import raises, approx\n\n\ndef test_input_sanity():\n    """Check incorrect input do fail"""\n    energy = MagicMock()\n\n    with raises(NotImplementedError) as exception:\n        MonteCarlo(sum, [1, 1, 1], 0e0)\n    with raises(ValueError) as exception:\n        MonteCarlo(energy, [1, 1, 1], temperature=-1e0)\n\n    with raises(TypeError) as exception:\n        MonteCarlo(energy, [1.0, 2, 3])\n    with raises(ValueError) as exception:\n        MonteCarlo(energy, [-1, 2, 3])\n    with raises(ValueError) as exception:\n        MonteCarlo(energy, [[1, 2, 3], [3, 4, 5]])\n    with raises(ValueError) as exception:\n        MonteCarlo(energy, [3])\n    with raises(ValueError) as exception:\n        MonteCarlo(energy, [0, 0])\n\n\ndef test_move_particle_one_over():\n    """Check density is change by a particle hopping left or right."""\n    from numpy import nonzero, multiply\n    from numpy.random import randint\n\n    energy = MagicMock()\n\n    for i in range(100):\n        # Do this n times, to avoid\n        # issues with random numbers\n        # Create density\n\n        density = randint(50, size=randint(2, 6))\n        mc = MonteCarlo(energy, density)\n        # Change it\n        new_density = mc.change_density(density)\n\n        # Make sure any movement is by one\n        indices = nonzero(density - new_density)[0]\n        assert len(indices) == 2, "densities differ in two places"\n        assert (\n            multiply.reduce((density - new_density)[indices]) == -1\n        ), "densities differ by + and - 1"\n\n\ndef test_equal_probability():\n    """Check particles have equal probability of movement."""\n    from numpy import array, sqrt, count_nonzero\n\n    energy = MagicMock()\n\n    density = array([1, 0, 99])\n    mc = MonteCarlo(energy, density)\n    changes_at_zero = [\n        (density - mc.change_density(density))[0] != 0 for i in range(10000)\n    ]\n    assert count_nonzero(changes_at_zero) == approx(\n        0.01 * len(changes_at_zero), 0.5 * sqrt(len(changes_at_zero))\n    )\n\n\ndef test_accept_change():\n    """Check that move is accepted if second energy is lower"""\n    from numpy import sqrt, count_nonzero, exp\n\n    energy = MagicMock()\n    mc = MonteCarlo(energy, [1, 1, 1], temperature=100.0)\n    # Should always be true.\n    # But do more than one draw,\n    # in case randomness incorrectly crept into\n    # implementation\n    for i in range(10):\n        assert mc.accept_change(0.5, 0.4)\n        assert mc.accept_change(0.5, 0.5)\n\n    # This should be accepted only part of the time,\n    # depending on exponential distribution\n    prior, successor = 0.4, 0.5\n    accepted = [mc.accept_change(prior, successor) for i in range(10000)]\n    assert count_nonzero(accepted) / float(len(accepted)) == approx(\n        exp(-(successor - prior) / mc.temperature), 3e0 / sqrt(len(accepted))\n    )\n\n\ndef test_main_algorithm():\n    import numpy as np\n    from numpy import testing\n    from unittest.mock import Mock\n\n    density = [1, 1, 1, 1, 1]\n    energy = MagicMock()\n    mc = MonteCarlo(energy, density, itermax=5)\n\n    acceptance = [True, True, True, True, True]\n    mc.accept_change = Mock(side_effect=acceptance)\n    mc.random_agent = Mock(side_effect=[0, 1, 2, 3, 4])\n    mc.random_direction = Mock(side_effect=[1, 1, 1, 1, -1])\n    np.testing.assert_equal(mc.step()[1], [0, 1, 1, 2, 1])\n')


# In[5]:


get_ipython().run_cell_magic('bash', '', 'cd DiffusionExample\npy.test\n')

