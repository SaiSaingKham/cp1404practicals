import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_PER_QUICK_PICK = 6
NUMBER_QUICK_PICKS = 5


number_quick_picks = int(input("How many quick picks? "))


for i in range(number_quick_picks):
    numbers = random.sample(range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1), NUMBER_PER_QUICK_PICK)
    numbers.sort()

    print(" ".join("{:2d}".format(n) for n in numbers))
