"""Quick Picks lottery picker"""
import random

NUMBERS = 6
MAX_VALUE = 45
MIN_VALUE = 1


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("Cannot have negative quick picks. Enter an appropriate number of picks: ")
        quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        picks = []
        for number in range(NUMBERS):
            number = random.randint(MIN_VALUE, MAX_VALUE)
            picks.append(number)
        picks.sort()
        print(" ".join(f"{number:3}" for number in picks))


main()
