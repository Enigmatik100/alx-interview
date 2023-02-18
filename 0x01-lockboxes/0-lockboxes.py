#!/usr/bin/python3
"""Lock boxes problem"""


def canUnlockAll(boxes):
    """Lock boxes problem"""
    unlocked = {0}
    tobe_visited = [0]

    while tobe_visited:
        index = tobe_visited.pop()
        keys = boxes[index]
        for key in keys:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                tobe_visited.append(key)

    return len(unlocked) == len(boxes)
