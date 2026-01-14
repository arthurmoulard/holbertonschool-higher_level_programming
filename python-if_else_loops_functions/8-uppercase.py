#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            print(f"{chr(ord(c) - 32)}", end="")
        else:
            print(f"{c}", end="")
    print()