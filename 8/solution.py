lines = open("7/in.txt").read().splitlines()

def search_tree(desired: int, so_far: int, numbers: list[int]) -> bool:
    # stopping conditions
    if so_far > desired:
        return False
    if len(numbers) == 0:
        return so_far == desired

    ops = [
        lambda x, y: x+y,
        lambda x, y: x*y,
        lambda x, y: int(str(x) + str(y)) # pt2
    ]

    # recursion
    return any([
        search_tree(desired, op(so_far, numbers[0]), numbers[1:])
        for op in ops
    ])

results = []

for line in lines:
    desired_str, numbers_line = line.split(": ")
    desired = int(desired_str)
    numbers = [int(n) for n in numbers_line.split(" ")]

    result = search_tree(desired, numbers[0], numbers[1:])
    if result:
        results.append(desired)

print(sum(results))
