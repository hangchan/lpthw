#!/bin/usr/env python3

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Rooster", 100 - 25 * 3 % 4) # 25 * 3 = 75, 75 % 4 = 3, 100 - 3 = 97

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6) # 4 % 2 = 0, 1.0 / 4 = .25, 3 + 2 + 1 - 5 + 0 - .25 + 6 = 6.75

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7) # false, 5 < -2

print("What is 3 + 2?", 3 + 2) # 5
print("What is 5 - 7?", 5 - 7) # -2

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2) # True
print("Is it greater or equal?", 5 >= -2) # True
print("Is it less or equal?", 5 <= -2) # False