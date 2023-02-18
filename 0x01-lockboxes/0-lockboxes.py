#!/usr/bin/python3
"""Lock boxes problem"""


def canUnlockAll(boxes):
    """Lock boxes problem"""
    visited = {0}
    stack = [0]

    while stack:
        keys = boxes[stack.pop()]
        for key in keys:
            if key not in visited:
                visited.add(key)
                stack.append(key)
    return len(visited) == len(boxes)
