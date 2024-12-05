import os
import numpy as np

filename = "1ex.txt"
file = open(os.path.join(os.path.dirname(__file__), filename))
lines = file.read().splitlines()

pairs = [l.split() for l in lines]
pairs_arr = np.array(pairs)
transposed = pairs_arr.T
sorted_transposed = np.array([sorted(transposed[0]), sorted(transposed[1])])
sorted_pairs = sorted_transposed.T
sum_distances = sum([abs(int(p[0]) - int(p[1])) for p in sorted_pairs])

print(sum_distances)

# pt2
sum = 0

for pair in sorted_pairs:
    occurences = sorted_transposed[1].tolist().count(pair[0])
    sum += int(pair[0]) * occurences

print(sum)
