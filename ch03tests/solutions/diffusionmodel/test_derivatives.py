""" Tests partial derivative via mocking """
from mock import MagicMock
from nose.tools import assert_equal, assert_true
from diffusion_model import partial_derivative

def test_partial_derivative():
  """ Mocks a call to partial derivative. """
  from numpy import array, sum, abs
  # setups arguments
  function = MagicMock(side_effect=[3, 2])
  density = array([0, 1, 2])

  # Makes call 
  result = partial_derivative(function, density, 1)
  # Check magnitude of result: sign depends on order of call since we are faking it. 
  assert_equal(abs(result), 1, "Magnitude of partial derivative")

  # Check function was called twice
  assert_equal(function.call_count, 2, "Function was called twice")

  for name, args, kwargs in function.mock_calls:
    # Called function itself
    assert_equal(name, '')
    # No keyword arguments 
    assert_equal(kwargs, {})
    # Single argument
    assert_equal(len(args),  1)

    # Density is at most off by one
    assert_true(abs(sum(args[0] - density)) <= 1)

  # Checks that args in two calls are off by one and that sign of result is correct
  first_density = function.mock_calls[0][1][0]
  second_density = function.mock_calls[1][1][0]
  assert_equal(sum(first_density - second_density), result)
