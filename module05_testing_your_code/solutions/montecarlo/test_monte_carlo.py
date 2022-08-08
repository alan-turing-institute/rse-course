""" Tests Monte-Carlo method, in isolation of diffusion model """
import pytest
from monte_carlo import MonteCarlo


def test_input_sanity():
    """Check incorrect input do fail"""

    with pytest.raises(NotImplementedError):
        MonteCarlo(temperature=0e0)
    with pytest.raises(ValueError):
        MonteCarlo(temperature=-1e0)

    mc = MonteCarlo()
    with pytest.raises(TypeError):
        mc(lambda x: 0, [1.0, 2, 3])
    with pytest.raises(ValueError):
        mc(lambda x: 0, [-1, 2, 3])
    with pytest.raises(ValueError):
        mc(lambda x: 0, [[1, 2, 3], [3, 4, 5]])
    with pytest.raises(ValueError):
        mc(lambda x: 0, [3])
    with pytest.raises(ValueError):
        mc(lambda x: 0, [0, 0])


def test_move_particle_one_over():
    """Check density is change by a particle hopping left or right."""
    from numpy import multiply, nonzero
    from numpy.random import randint

    mc = MonteCarlo()

    for i in range(100):  # Do this n times, to avoid issues with random numbers
        # Create density
        density = randint(50, size=randint(2, 6))
        # Change it
        new_density = mc.change_density(density)

        # Make sure any movement is by one
        indices = nonzero(density - new_density)[0]
        assert len(indices) == 2, "densities differ in two places"
        assert (
            multiply.reduce((density - new_density)[indices]) == -1
        ), "densities differ by + and - 1"


def test_equal_probability():
    """Check particles have equal probability of movement."""
    from numpy import array, count_nonzero, sqrt

    mc = MonteCarlo()
    density = array([1, 0, 99])
    changes_at_zero = [
        (density - mc.change_density(density))[0] != 0 for i in range(10000)
    ]
    assert count_nonzero(changes_at_zero) == pytest.approx(
        0.01 * len(changes_at_zero), abs=0.5 * sqrt(len(changes_at_zero))
    )


def test_accept_change():
    """Check that move is accepted if second energy is lower"""
    from numpy import count_nonzero, exp, sqrt

    mc = MonteCarlo(temperature=100.0)
    # Should always be true. But do more than one draw, in case random incorrectly crept
    # into implementation
    for i in range(10):
        assert mc.accept_change(0.5, 0.4)
        assert mc.accept_change(0.5, 0.5)

    # This should be accepted only part of the time, depending on exponential
    # distribution
    prior, successor = 0.4, 0.5
    accepted = [mc.accept_change(prior, successor) for i in range(10000)]
    assert count_nonzero(accepted) / float(len(accepted)) == pytest.approx(
        exp(-(successor - prior) / mc.temperature), abs=3e0 / sqrt(len(accepted))
    )


def test_main_algorithm():
    """Check set path through main algorithm"""
    from unittest.mock import Mock, call

    mc = MonteCarlo(temperature=100.0, itermax=4)

    # Patch mc so that it takes a pre-determined path through
    acceptance = [True, True, False, True]
    mc.accept_change = Mock(side_effect=acceptance)
    densities = (
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [2, 2, 2, 2],
        [2, 3, 3, 2],
        [5, 3, 3, 5],
    )
    mc.change_density = Mock(side_effect=densities[1:])
    mc.observe = Mock(return_value=True)

    # Fake energy method
    energies = [0.1, -0.1, -0.2, -0.15, -0.25]
    energy = Mock(side_effect=energies)

    # Call simulation
    mc(energy, densities[0])

    # Now, analyze path. First check length.
    assert len(mc.accept_change.mock_calls) == 4
    assert len(mc.change_density.mock_calls) == 4
    assert len(mc.observe.mock_calls) == 4
    assert len(energy.mock_calls) == 5  # one extra call to get first energy

    # Easiest to look at observe, since it should have all the info about the step
    observe_path = [
        call(0, acceptance[0], densities[1], energies[1]),
        call(1, acceptance[1], densities[2], energies[2]),
        call(2, acceptance[2], densities[2], energies[2]),
        call(3, acceptance[3], densities[4], energies[4]),
    ]
    assert observe_path == mc.observe.call_args_list


def test_stop_simulation():
    """Checks that if observe returns False, iteration stops."""
    from unittest.mock import Mock

    mc = MonteCarlo(temperature=100.0, itermax=8)

    # Make a fake observer
    mc.observe = Mock(side_effect=[True, False, True])
    # Fake energy method
    energies = [0.1, -0.1, -0.2, -0.15, -0.25]
    energy = Mock(side_effect=energies)
    # Call simulation
    mc(energy, [0, 1, 2, 3])

    assert len(mc.observe.mock_calls) == 2
    assert len(energy.mock_calls) == 3  # one extra call to get first energy
