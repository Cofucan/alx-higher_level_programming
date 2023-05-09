#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = int(list(str(number))[-1])
last_digit = -(last_digit) if number < 0 else last_digit
pref = "Last digit of"

if last_digit > 5:
    print(f"{pref} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{pref} {number} is {last_digit} and is 0")
elif last_digit < 6:
    print(f"{pref} {number} is {last_digit} and is less than 6 and not 0")
