""" Unit tests for a diffusion model """

from pytest import raises
from .model import energy

def test_energy_fails_on_non_integer_density():
    with raises(TypeError) as exception: 
       energy([1.0, 2, 3])
    
def test_energy_fails_on_negative_density():
    with raises(ValueError) as exception: energy(
            [-1, 2, 3])
        
def test_energy_fails_ndimensional_density():
    with raises(ValueError) as exception: energy(
            [[1, 2, 3], [3, 4, 5]])

def test_zero_energy_cases():
  # Zero energy at zero density
  densities = [ [], [0], [0, 0, 0] ]
  for density in densities: 
    assert energy(density) == 0

def test_derivative():
  from numpy.random import randint

  # Loop over vectors of different sizes (but not empty)
  for vector_size in randint(1, 1000, size=30): 

    # Create random density of size N
    density = randint(50, size=vector_size)

    # will do derivative at this index
    element_index = randint(vector_size)

    # modified densities
    density_plus_one = density.copy()
    density_plus_one[element_index] += 1

    # Compute and check result
    # d(n^2-1)/dn = 2n
    expected = (2.0*density[element_index] 
                if density[element_index] > 0 
                else 0 )
    actual = energy(density_plus_one) - energy(density) 
    assert expected == actual

def test_derivative_no_self_energy():
  """ If particle is alone, then its participation to energy is zero """
  from numpy import array

  density = array([1, 0, 1, 10, 15, 0])
  density_plus_one = density.copy()
  density[1] += 1 

  expected = 0
  actual = energy(density_plus_one) - energy(density) 
  assert expected == actual