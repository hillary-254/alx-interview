#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    num_boxes = len(boxes)
    visited_boxes = set([0])
    unvisited_boxes = set(boxes[0]).difference(set([0]))

    while len(unvisited_boxes) > 0:
        current_box_index = unvisited_boxes.pop()

        # Skip invalid box indices
        if not current_box_index or current_box_index >= num_boxes or current_box_index < 0:
            continue

        # Process the current box if not already visited
        if current_box_index not in visited_boxes:
            unvisited_boxes = unvisited_boxes.union(boxes[current_box_index])
            visited_boxes.add(current_box_index)

    return num_boxes == len(visited_boxes)
