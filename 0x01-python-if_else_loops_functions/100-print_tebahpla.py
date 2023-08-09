#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
a = 0
for z in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(z - a)), end="")
    a = 32 if a == 0 else 0
