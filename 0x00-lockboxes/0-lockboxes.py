#!/usr/bin/python3
'''Lockboxes '''


def canUnlockAll(boxes):
    '''
    determines if all the boxes can be opened
    '''

    openboxes = [0]
    for key in openboxes:
        # go to box according key number
        for box in boxes[key]:
            if box not in openboxes and box < len(boxes):
                openboxes.append(box)
    # all boxes can be opened
    if len(openboxes) == len(boxes):
        return True
    return False
