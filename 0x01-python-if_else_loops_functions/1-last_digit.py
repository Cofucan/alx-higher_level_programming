#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
abs(number)  # Ensure that the number is of correct type.
last_digit = int(list(str(number))[-1])  # Convert to list and get last num.
last_digit = -(last_digit) if number < 0 else last_digit

print(f"Last digit of {number} is {last_digit} and is ", end="")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
elif last_digit < 6:
    print("less than 6 and not 0")
