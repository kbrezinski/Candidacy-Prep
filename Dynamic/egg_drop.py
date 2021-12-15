
import random

max_floors = 100
floor = random.randint(1, max_floors)  # last floor which it doesn't break


# main function call
def max_floor():
    max_floor_aux(start=0, end=max_floors, floor=floor, count=0, breaks=0)


# auxiliary call for main function call
def max_floor_aux(start: int, end: int, floor: int, count: int, breaks: int):

    # halfway mark in current floor range
    mid = int((start + end) / 2)

    if mid == start:
        print(f"Egg doesn't break at floor: {start} | Answer: {floor} | Drops: {count} | Breaks: {breaks}")
    elif start < end:

        # check if floor is below if egg breaks
        if mid > floor:
            print(f"Egg breaks on floor: {mid}")
            max_floor_aux(start=start, end=mid, floor=floor, count=count+1, breaks=breaks+1)

        # check if floor is above
        elif mid <= floor:
            print(f"Egg didn't break on floor: {mid}")
            max_floor_aux(start=mid, end=end, floor=floor, count=count+1, breaks=breaks)


# run routine
max_floor()
