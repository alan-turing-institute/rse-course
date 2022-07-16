""" Unit tests for a diffusion model """
from diffusion_model import energy
from pytest import approx

# def test_energy_fails_on_non_integer_density():
#   with assert_raises(TypeError) as exception: energy([1.0, 2, 3])
#
# def test_energy_fails_on_negative_density():
#   with assert_raises(ValueError) as exception: energy([-1, 2, 3])
#
# def test_energy_fails_ndimensional_density():
#   with assert_raises(ValueError) as exception: energy([[1, 2, 3], [3, 4, 5]])


def test_zero_energy_cases():
    # Zero energy at zero density
    densities = [[], [0], [0, 0, 0]]
    for density in densities:
        assert energy(density) == approx(0)

    # Zero energy for coefficient == 0
    assert energy([1, 1, 1], coefficient=0) == approx(0)


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
        expected = density[element_index] if density[element_index] > 0 else 0
        actual = energy(density_plus_one) - energy(density)
        assert expected == approx(actual)


def test_derivative_no_self_energy():
    """If particle is alone, then its participation to energy is zero"""
    from numpy import array

    density = array([1, 0, 1, 10, 15, 0])
    density_plus_one = density.copy()
    density[1] += 1

    expected = 0
    actual = energy(density_plus_one) - energy(density)
    assert expected == approx(actual)


def test_coefficient_is_linear():
    from numpy import array

    density = array([1, 0, 1, 10, 15, 0])

    value = energy(density, coefficient=1)
    twice = energy(density, coefficient=2e0)
    assert value + value == approx(twice)
