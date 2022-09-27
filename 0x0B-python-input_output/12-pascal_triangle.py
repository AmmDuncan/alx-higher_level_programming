#!/usr/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    res = [[]] * (n + 2)
    res[1] = [1]
    res[2] = [1, 1]

    for i in range(3, n + 1):
        row = []
        for j in range(i):
            last = i - 1
            if j == 0 or j == last:
                row.append(1)
            else:
                row.append(res[i - 1][j - 1] + res[i - 1][j])
        res[i] = row

    return res[1:n + 1]