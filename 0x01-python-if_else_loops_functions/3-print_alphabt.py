#!/usr/bin/python3
"""print the alphabet in lowercase, not followed by a new line."""

for letter in range(97, 123):
    if letter not in [101, 113]:
        print("{}".format(chr(letter)), end="")
