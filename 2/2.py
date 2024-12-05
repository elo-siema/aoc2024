import os

filename = "2.txt"
file = open(os.path.join(os.path.dirname(__file__), filename))
lines = file.read().splitlines()


def is_safe(line):
    zipped = list(zip(line[:-1], line[1:]))
    diffs = list(map(lambda x: int(x[0]) - int(x[1]), zipped))
    if not (all(diff < 0 for diff in diffs) or all(diff > 0 for diff in diffs)):
        return False
    if not all(abs(diff) in range(1, 4) for diff in diffs):
        return False
    return True

count = 0
for line in lines:
    levels = line.split()
    if is_safe(levels):
        count += 1

print(count)

# pt2

count = 0
for line in lines:
    levels = line.split()

    permutations = [
        levels,
        *[levels[:x]+levels[(x+1):] for x in range(len(levels))]
    ]

    if any(is_safe(p) for p in permutations):
        count += 1

print(count)
