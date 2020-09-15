"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = "Yacht"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FullHouse"
FOUR_OF_A_KIND = "FourKind"
LITTLE_STRAIGHT = "LittleStraight"
BIG_STRAIGHT = "BigStraight"
CHOICE = "Choice"


def score(dice, category):
    dice.sort()
    unique_die = list(set(dice))
    first_die_count = dice.count(unique_die[0])
    score = 0
    if type(category) is int:
        score = category * dice.count(category)
    if category == "FullHouse" and len(unique_die) == 2 and first_die_count in [2, 3]:
        score = sum(dice)
    if category == "FourKind" and len(unique_die) in [1, 2]:
        if first_die_count == 1:
            score = 4 * unique_die[1]
        elif first_die_count in [4, 5]:
            score = 4 * unique_die[0]
    if (category == "LittleStraight" and dice == [1, 2, 3, 4, 5]) or (category == "BigStraight" and dice == [2, 3, 4, 5, 6]):
        score = 30
    if category == "Choice":
        score = sum(dice)
    if category == 'Yacht' and len(unique_die) == 1:
        score = 50
    return score
