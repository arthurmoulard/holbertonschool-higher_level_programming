#!/usr/bin/env python3
import sys

count = len(sys.argv) - 1

if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print(f"{count} arguments:")

index = 1
for arg in sys.argv[1:]:
    print(f"{index}: {arg}")
    index += 1