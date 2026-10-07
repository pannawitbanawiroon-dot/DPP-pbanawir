#!/usr/bin/env python3
import math
user_input = input("Give me a number: ")
try:
    num = float(user_input)
    print(math.ceil(num))
except ValueError:
    pass