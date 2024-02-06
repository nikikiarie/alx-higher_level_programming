#!/usr/bin/python3
"""dDefines Pascals Triangle function"""


def pascal_triangle(n):
    """Represents Pascal triangle size n"""
    if n <= 0:
        return []
    tri =[[1]]
    while len(tri)!= n:
        t = tri[-1]
        temp = [1]
        for a in range(len(t) -1):
            temp.append(t[a] + t[a + 1])
        temp.append(1)
        tri.append(temp)
    return tri
