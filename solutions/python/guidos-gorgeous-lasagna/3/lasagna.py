"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time
    #bake_time_remaining.__doc__

def preparation_time_in_minutes(elapsed_bake_time):
    """Calculate the preparation time in minutes.
    
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - preparation time in minutes.
    Function that takes the elapsed minutes the lasagna will be in the oven as
    an argument and returns twice the elapsed time.
    """
    return elapsed_bake_time * 2
    elapsed_time_in_minutes.__doc__


def elapsed_time_in_minutes(elapsed_bake_layer, elapsed_bake_time):
    
    """Calculate the elapsed time in minutes.

    :param elapsed_bake_time: int - baking time already elapsed.
    elapsed_bake_layer: int - bake layer
    :return: int - sum of elapsed bake layer time 2 and elapsed bake time.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return (elapsed_bake_layer *2) + elapsed_bake_time
    elapsed_time_in_minutes.__doc__

