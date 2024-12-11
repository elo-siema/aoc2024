import re

diskmap = list(open("9/in.txt").read().splitlines()[0])

disk = []

for i, char in enumerate(diskmap):
    sequence_to_append = '.' if i % 2 == 1 else str(i//2)
    for x in range(int(char)):
        disk.append(sequence_to_append)

print(disk)

beg = 0
end = len(disk)-1

while True:
    while disk[beg] != '.':
        beg += 1

    while disk[end] == '.':
        end -= 1

    if beg >= end:
        break

    disk[beg], disk[end] = disk[end], disk[beg]
    beg += 1
    end -= 1

print(disk)

checksum = sum([i * int(x) for i, x in enumerate(disk) if x != '.'])

print(checksum)


# pt2

disk = []

for i, char in enumerate(diskmap):
    disk.append({
        "free": i % 2 == 1,
        "id": "." if i % 2 == 1 else str(i//2),
        "size": int(char)
    })

print(disk)

for backwards in range(len(disk)-1,-1,-1):
    if disk[backwards]["free"]:
        continue

    file = disk[backwards]

    for forwards, space in enumerate(disk):
        if forwards >= backwards:
            break

        if not space["free"]:
            continue

        if space["size"] >= file["size"]:
            disk[forwards] = {
                "free": False,
                "id": file["id"],
                "size": file["size"]
            }
            disk[backwards] = {
                "free": True,
                "id": ".",
                "size": file["size"]
            }
            disk.insert(forwards+1, {
                "free": True,
                "id": ".",
                "size": space["size"] - file["size"]
            })
            break

expanded = []
for x in disk:
    for i in range(x["size"]):
        expanded.append(x["id"])


checksum = sum([i * int(x) for i, x in enumerate(expanded) if x != '.'])

print(checksum)
