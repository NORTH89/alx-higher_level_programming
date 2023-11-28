#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    mod = number % 10
else:
    mod = ((number * -1) % 10) * -1
msg = "Last digit of {:d} is {:d} and is "
if number % 10 > 5:
    print(msg.format(number, mod) + "greater than 5")
elif number % 10 == 0:
    print(msg.format(number, mod) + "0")
else:
    print(msg.format(number, mod) + "less than 6 and not 0")
