from random import choice
from itertools import product
from string import ascii_uppercase, digits


names_cache = list()


class Robot:
    def __init__(self):
        global names_cache
        for _ in iter(int, 1):  # More time efficient "while True"
            # Format: AA000
            candidate = "".join(
                choice([p for p in product(ascii_uppercase, repeat=2)])
                + choice([p for p in product(digits, repeat=3)])
            )
            # Check if not in cache
            if candidate not in names_cache:
                self.name = candidate
                names_cache.append(candidate)
                break

    def reset(self):
        self.__init__()
