#!/usr/bin/python3
"""
Solves the N-Queen puzzle using backtracking.
"""

def is_safe(queens, n):
    """ Check if queens can coexist without attacking. """
    for i in range(n):
        if queens[i] == queens[n] or abs(queens[i] - queens[n]) == abs(i - n):
            return False
    return True


def solve(size):
    """ Start the N-Queen solver. """
    queens = [-1 for _ in range(size)]
    place_queen(queens, 0)


def display(queens, n):
    """ Show positions of queens. """
    res = [[i, queens[i]] for i in range(n)]
    print(res)


def place_queen(queens, n):
    """ Use backtracking to place queens. """
    if n == len(queens):
        display(queens, n)
        return

    queens[n] = -1
    while queens[n] < len(queens) - 1:
        queens[n] += 1
        if is_safe(queens, n):
            place_queen(queens, n + 1)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(size)
