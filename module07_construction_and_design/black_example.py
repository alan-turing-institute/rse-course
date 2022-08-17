import numpy as np

def my_complex_function(important_argument_1,important_argument_2,optional_argument_3 = 3,optional_argument_4 = 4):
    return np.random.random()*important_argument_1*important_argument_2*optional_argument_3*optional_argument_4

def hello(name,greet='Hello',end="!"):
    print(greet,    name,    end)
