#!/usr/bin/python3
"""
prints out pascal's triangle for a given value of n
"""


def pascal_triangle(n):
    """prints out pascal's triangle for a given value <n>"""
    psc = []
    current_pos = 1

    if n == 0:
        return []

    while current_pos <= n:
        tmp_psc = []

        for i in range(current_pos):
            if i == 0 or i == current_pos - 1:
                tmp_psc.append(1)
            else:
                tmp_psc.append(
                    psc[current_pos - 2][i] + psc[current_pos - 2][i - 1]
                )
        psc.append(tmp_psc)
        current_pos += 1
    return psc
