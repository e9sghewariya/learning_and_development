"""
assessment013.py
This file is part of the Python Project Euler Solutions repository."""

# # Problem No. 18
# ## Maximum Path Sum - Simple

# By starting at the top of the triangle below
# and moving to adjacent numbers on the row below, the maximum total from top to bottom is $23$.</p>
# <p>That is, $3 + 7 + 4 + 9 = 23$.</p>
# ## Part A
# <p>Find the maximum total from top to bottom of the triangle below:</p>

# <p align="center">
# 75<br>
# 95 64<br>
# 17 47 82<br>
# 18 35 87 10<br>
# 20 04 82 47 65<br>
# 19 01 23 75 03 34<br>
# 88 02 77 73 07 63 67<br>
# 99 65 04 28 06 16 70 92<br>
# 41 41 26 56 83 40 80 70 33<br>
# 41 48 72 33 47 32 37 16 94 29<br>
# 53 71 44 65 25 43 91 52 97 51 14<br>
# 70 11 33 28 77 73 17 78 39 68 17 57<br>
# 91 71 52 38 17 14 91 43 58 50 27 29 48<br>
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31<br>
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# </p>

# Edit the file `answer.py` and update the function
# `answer()` to return the answer.

# ## Part B

# Given a triangle of numbers of variable height `n`,
# find the maximum total from top to bottom.
# Edit the file `solver.py` and update the function
# `solver()` with your generalized solution.
# ```python
# solver()
# ```

triangle_data = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def answer():
    """Top-down max path sum for full triangle (15 rows)."""
    triangle = [row[:] for row in triangle_data]  # Create a fresh copy of each row

    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row - 1][col]
            elif col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row - 1][col - 1]
            else:
                triangle[row][col] += max(
                    triangle[row - 1][col - 1], triangle[row - 1][col]
                )
    return max(triangle[-1])


print(answer())  # Output: 1074


def solver(height):
    """Top-down max path sum for variable height triangle."""
    if height <= 0 or height > len(triangle_data):
        return None

    triangle = [
        row[:] for row in triangle_data[:height]
    ]  # Copy only up to given height

    for row in range(1, height):
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row][col] += triangle[row - 1][col]
            elif col == len(triangle[row]) - 1:
                triangle[row][col] += triangle[row - 1][col - 1]
            else:
                triangle[row][col] += max(
                    triangle[row - 1][col - 1], triangle[row - 1][col]
                )

    return max(triangle[-1])


# Usage
print(solver(15))  # Output: 1074
print(solver(4))  # Output: 234
