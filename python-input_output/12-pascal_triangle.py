#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []

    for i in range(n):
        cote = []
        for j in range(i + 1):
            pass