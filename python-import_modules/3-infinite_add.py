#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    somme = 0

    for arg in sys.argv[1:]:
        somme += int(arg)

    print(somme)
    