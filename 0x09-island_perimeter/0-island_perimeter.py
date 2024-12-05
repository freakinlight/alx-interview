#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid: 2D list where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4

                # Check the top cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Check the left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
