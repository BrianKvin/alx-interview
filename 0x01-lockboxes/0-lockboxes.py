#/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnLockAll(boxes):
    """a method determining if all the boxes can be opened"""
    if not boxes or type(boxes) is not list:
        return False

    unlock = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key , len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False


"""
def canUnlockAll(boxes):
    canUnlockAll = False
    keys = {0: True}
    n_boxes = len(boxes)
    while(True):

        n_keys = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
"""
