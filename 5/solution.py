import re
import itertools
from typing import Optional

ordering, prints = open("5/in.txt").read().split("\n\n")

ordering = ordering.splitlines()
prints = prints.splitlines()

successors = {}
for line in ordering:
    pre, suc = line.split("|")
    if pre not in successors:
        successors[pre] = []
    successors[pre] = [*successors[pre], suc]

print(successors)

mids = []
incorrects = []

def return_mid_if_correct(nums) -> Optional[str]:
    nums = [*nums, None]
    for i, n in enumerate(nums[:-1]):
        next = nums[i+1]
        if next is None:
            print(f"Success on {pr}")
            mid = nums[len(nums)//2-1]
            return mid
        elif next not in (successors.get(n) or []):
            return None


for pr in prints:
    nums = pr.split(",")
    mid = return_mid_if_correct(nums)
    if mid is None:
        incorrects.append(nums)
    else:
        mids.append(mid)




#print(mids)
#print(sum([int(m) for m in mids]))

print(incorrects)


def fix(incorrect: list) -> str:

    possible_permutations = itertools.permutations(incorrect)

    for perm in possible_permutations:
        mid = return_mid_if_correct(perm)
        if mid is not None:
            return mid

mids = [fix(incorrect) for incorrect in incorrects]
print(mids)
print(sum([int(m) for m in mids]))
