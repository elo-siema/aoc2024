import re

lines = open("4.txt").read().splitlines()

def rotate_90_clockwise(lines):
    zipped = list(zip(*lines[::-1]))
    return list(map(''.join, zipped))

def kick_diagonally(lines: list[str]):
    return [i*' '+x+(len(lines)-i-1)*' ' for i, x in enumerate(lines)]

def print_nicely(lines):
    [print(line) for line in lines]

rotations = [
    lines, rotate_90_clockwise(lines), rotate_90_clockwise(kick_diagonally(lines)), rotate_90_clockwise(kick_diagonally(rotate_90_clockwise(lines))),
    ]

for r in rotations:
    print_nicely(r)
    print("=============")

matches = 0
for r in rotations:
    for line in r:
        matches += len(re.findall(r'(?=(XMAS|SAMX))', line)) # (?=(...)) for overlapping matches

print(matches)

#pt2
lines_with_margin = [len(lines[0]) * " ", *[" " + line + " " for line in lines], len(lines[0]) * " ",]
print_nicely(lines_with_margin)

matches = []
mases = 0

for y, l in enumerate(lines_with_margin):
    for x, c in enumerate(l):
        if c == 'A':
            matches.append((x, y))

patterns = [
    ((-1,-1,"M"), (1,1,"S"), (1,-1,"M"), (-1,1,"S")),
    ((-1,-1,"S"), (1,1,"M"), (1,-1,"M"), (-1,1,"S")),
    ((-1,-1,"M"), (1,1,"S"), (1,-1,"S"), (-1,1,"M")),
    ((-1,-1,"S"), (1,1,"M"), (1,-1,"S"), (-1,1,"M")),
]

def check_match(match: tuple[int, int]):
    for pattern in patterns:
        if all(lines_with_margin[match[1]+p[1]][match[0]+p[0]] == p[2] for p in pattern):
            return True
    return False

result = sum([1 for m in matches if check_match(m)])

print(result)
