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
YACHT = None
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FH"
FOUR_OF_A_KIND = "FourKind"
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    if type(category) is int:
        return category * dice.count(category)
    if category is "FH":
        if len(set(dice)) == 2 and dice.count(dice[0]) in [2,3]:
            return sum(dice)
    if category is "FourKind"
        if (len(set(dice)) == 2 and dice.count(dice[0]) in [1,4]):
            
            

    return 0