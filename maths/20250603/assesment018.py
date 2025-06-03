"""
assessment013.py
This file is part of the Python Project Euler Solutions repository."""
# # Problem No. 18
# ## Maximum Path Sum - Simple

# By starting at the top of the triangle below
# and moving to adjacent numbers on the row below, the maximum total from top to bottom is $23$.</p>
# <p align="center">
#   <span style="text-decoration: underline;"><b>3</b></span><br>
#   <span style="text-decoration: underline;"><b>7</b></span> 4<br>
#   2 <span style="text-decoration: underline;"><b>4</b></span> 6<br>
#   8 5 <span style="text-decoration: underline;"><b>9</b></span> 3
# </p>
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
    """Find the maximum total from top to bottom of the triangle."""
    for row in range(len(triangle_data) - 2, -1, -1):
        for col in range(len(triangle_data[row])):
            triangle_data[row][col] = triangle_data[row][col] + max(
                triangle_data[row + 1][col], triangle_data[row + 1][col + 1]
            )
    return triangle_data[0][0]

print(answer())
# Output: 1074


def solver(height):
    """Find the maximum total from top to bottom of a triangle of variable height."""
    if height <= 0 or height > len(triangle_data):
        return None

    triangle = triangle_data[:height]

    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] = triangle[row][col] + max(
                triangle[row + 1][col], triangle[row + 1][col + 1]
            )

    return triangle[0][0]
print(solver(15))
