#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -(last)
string = "Last digit of {} is {}".format(number, last)
if last > 5:
    print(f"{string} and is greater than 5")
elif last == 0:
    print(f"{string} and is 0")
elif last < 6:
    print(f"{string} and is less than 6 and not 0")
