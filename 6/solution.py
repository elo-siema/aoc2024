import re
from tqdm import tqdm

lines = open("6/in.txt").read().splitlines()
area = [list(x) for x in lines]

def print_nicely(area):
    [print("".join(line)) for line in area]

print_nicely(area)

#direction = "up"
guard_x = 0
guard_y = 0
move_vectors = {
    "^": (0, -1),
    "v": (0, 1),
    ">": (1, 0),
    "<": (-1, 0)
}
dir_order = ["^", ">", "v", "<"]

# find initial guard position
for y, line in enumerate(area):
    for x, char in enumerate(line):
        if char == "^":
            guard_x = x
            guard_y = y

while True:
    direction = area[guard_y][guard_x]
    vector = move_vectors[direction]

    # case 1: out of bounds
    if guard_x + vector[0] < 0 or guard_x + vector[0] >= len(area[0]) or \
       guard_y + vector[1] < 0 or guard_y + vector[1] >= len(area):
        print("out of bounds")
        area[guard_y][guard_x] = "X"
        break
    # case 2: change dir
    if area[guard_y + vector[1]][guard_x + vector[0]] == "#":
        area[guard_y][guard_x] = dir_order[(dir_order.index(direction) + 1) % 4]
        continue
    # case 3: move
    elif area[guard_y + vector[1]][guard_x + vector[0]] in [".", "X"]:
        area[guard_y][guard_x] = "X"
        area[guard_y + vector[1]][guard_x + vector[0]] = direction
        guard_x += vector[0]
        guard_y += vector[1]
        continue

# count all X
print_nicely(area)
print(sum([line.count("X") for line in area]))

#pt2
def check_loop(area: list[list[str]]):
    guard_x = 0
    guard_y = 0
    move_vectors = {
        "^": (0, -1),
        "v": (0, 1),
        ">": (1, 0),
        "<": (-1, 0)
    }
    dir_order = ["^", ">", "v", "<"]
    visited_spots = set()

    # find initial guard position
    for y, line in enumerate(area):
        for x, char in enumerate(line):
            if char == "^":
                guard_x = x
                guard_y = y

    while True:
        direction = area[guard_y][guard_x]
        vector = move_vectors[direction]

        # case 1: out of bounds
        if guard_x + vector[0] < 0 or guard_x + vector[0] >= len(area[0]) or \
        guard_y + vector[1] < 0 or guard_y + vector[1] >= len(area):
            print("out of bounds")
            area[guard_y][guard_x] = "X"
            return False
        # case 2: change dir
        if area[guard_y + vector[1]][guard_x + vector[0]] == "#":
            area[guard_y][guard_x] = dir_order[(dir_order.index(direction) + 1) % 4]
            continue
        # case 3: move
        elif area[guard_y + vector[1]][guard_x + vector[0]] in [".", "X"]:
            area[guard_y][guard_x] = "X"
            area[guard_y + vector[1]][guard_x + vector[0]] = direction
            guard_x += vector[0]
            guard_y += vector[1]
            if (guard_x, guard_y, direction) in visited_spots:
                return True
            visited_spots.add((guard_x, guard_y, direction))
            continue

areas_to_check = []

# make variations of the area by putting obstacles in every place the guard has visited
for y, line in enumerate(area):
    for x, char in enumerate(line):
        if char == "X":
            new_area = [list(x) for x in lines]
            if new_area[y][x] == "^":
                continue
            new_area[y][x] = "#"
            areas_to_check.append(new_area)

times = 0
for area in tqdm(areas_to_check):
    if check_loop(area):
        print_nicely(area)
        print(times)
        times += 1

print(f"times: {times}")
