# Score categories.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = set
FOUR_OF_A_KIND = '4'
LITTLE_STRAIGHT = [1, 2, 3, 4, 5]
BIG_STRAIGHT = [2, 3, 4, 5, 6]
CHOICE = sum


def score(dice, category):
    
    dice.sort()

    numbers = [
            ONES, TWOS, THREES,
            FOURS, FIVES, SIXES
    ]
    if category in numbers:
        return dice.count(category) * category

    states = [
            LITTLE_STRAIGHT,
            BIG_STRAIGHT
    ]
    if category in states:
        if category == dice:
            return 30
        return 0

    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
        return 0

    if category == CHOICE:
        return sum(dice)

    if category == FOUR_OF_A_KIND:
        if dice.count(dice[0]) > 3:
            return dice[0] * 4
        elif dice.count(dice[0]) == 1 and dice.count(dice[1]) == 4:
            return dice[1] * 4
        return 0

    if category == FULL_HOUSE:
        if (len(set(dice)) == 2 and
                (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3)):
            return sum(dice)
        return 0
