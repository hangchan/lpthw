#!/usr/bin/env python3
i = 0
numbers = []

def addnum(num):
    i = 0
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

addnum(8)

for num in numbers:
    print(num)