import re

text = open("3mod.txt").read()
text2 = re.sub(r"((don't\(\).*?)(do\(\)|$))", "", text)
matches = re.findall(r"mul\((\d+,\d+)\)", text2)
result = sum([int(m.split(",")[0]) * int(m.split(",")[1]) for m in matches])

print(result)
