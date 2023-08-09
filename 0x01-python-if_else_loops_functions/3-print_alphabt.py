#!/usr/bin/python3
for ascii_char in range(ord("a"), ord("z") + 1):
    if ascii_char != 101 and ascii_char != 113:
        print("{}".format(chr(ascii_char)), end="")
