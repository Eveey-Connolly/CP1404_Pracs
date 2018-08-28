import random
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
number_of_quick_picks = int(input("How many quick picks?"))
while number_of_quick_picks <= 0:
    print("Invalid Number of Quick Picks")
    number_of_quick_picks = int(input("How many quick picks?"))
for i in range(number_of_quick_picks):
    quick_picks = []
    for n in range(NUMBERS_PER_LINE):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_picks:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join("{:2}".format(number) for number in quick_picks))
