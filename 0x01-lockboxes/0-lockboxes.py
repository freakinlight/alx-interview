#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): A list where each index contains the keys to
        other boxes.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    visited = set()
    to_visit = [0]  # Start with box 0 (unlocked)

    while to_visit:
        current_box = to_visit.pop()

        if current_box not in visited:
            visited.add(current_box)
            for key in boxes[current_box]:
                if key not in visited and key < len(boxes):
                    to_visit.append(key)

    return len(visited) == len(boxes)
