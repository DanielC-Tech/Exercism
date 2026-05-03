"""Functions for calculating time spent preparing and cooking lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - the total preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME
    

def elapsed_time_in_minutes(num_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.
    :param num_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - the time already spent baking.
    :return: int - the total elapsed time (in minutes).
    """
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time