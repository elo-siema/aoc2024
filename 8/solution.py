import re

lines = open("8/ex.txt").read().splitlines()
area = [list(x) for x in lines]

antennas: dict[str, list[tuple[int, int]]] = {}

for y, line in enumerate(area):
    for x, char in enumerate(line):
        if re.match(r"\d|\w", char):
            if char not in antennas:
                antennas[char] = []
            antennas[char].append((x, y))

for char, positions in antennas.items():
    print(char, positions)

antinodes = [list("."*len(area[0])) for _ in range(len(area))]

print(antinodes)

def get_antinodes(area: list[list[str]], antennas: dict[str, list[tuple[int, int]]] = {}) -> set[tuple[int, int]]:

    antinodes = set()

    # iterate through antennas of the same type
    for char, same_type_antennas in antennas.items():

        # get all pairs of antennas
        pairs = [(a, b) for a in same_type_antennas for b in same_type_antennas if a != b]

        for pair in pairs:
            # calculate vector between them
            x1, y1 = pair[0]
            x2, y2 = pair[1]
            vector = (x2 - x1, y2 - y1)

            # antinodes in up direction
            i = 1
            while True:
                a = (x1 - i * vector[0], y1 - i * vector[1])
                if a[0] < 0 or a[1] < 0 or a[0] >= len(area[0]) or a[1] >= len(area):
                    break
                antinodes.add(a)
                i += 1

            # antinodes in down direction
            i = 1
            while True:
                a = (x1 + i * vector[0], y1 + i * vector[1])
                if a[0] < 0 or a[1] < 0 or a[0] >= len(area[0]) or a[1] >= len(area):
                    break
                antinodes.add(a)
                i += 1

    return antinodes

result = get_antinodes(area, antennas)

print(result)

print(len(result))
