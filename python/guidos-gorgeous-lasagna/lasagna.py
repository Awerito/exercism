EXPECTED_BAKE_TIME: int = 40  # Minutes
PREPARATION_TIME: int = 2  # Minutes


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as an
    argument and returns how many minutes the lasagna still needs to bake based on the
    `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """
    :param layers: int how many layers do you want on the lasagna
    :return: int actual time of baking

    Function that takes the number of layers for the lasagna and returns how mush time it
    needs to bake.
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """
    :param number_of_layers: int number of layers of the lasagna
    :param elapsed_bake_time: int how many time has on preparation
    :return: int remaning time

    Calculate the remaining time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
