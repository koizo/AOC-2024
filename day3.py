# https://adventofcode.com/2024/day/3
import re

with open("day3.txt", "r") as file:
    text = file.read()

pattern_mul = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern_mul, text)
print(matches)
results = []

for match in matches:
    x, y = map(int, match)
    results.append(x * y)

print("Part 1:", sum(results))

pattern = r"(mul\(\d{1,5},\d{1,5}\)|do\(\)|don't\(\))"
matches = re.findall(pattern, text)
enable =  True
to_add = []

for match in matches:
    if match == "do()":
        enable = True
    elif match == "don't()":
        enable = False
    elif enable and match.startswith('mul') and (mult := re.findall(pattern_mul, match)):
        x, y = map(int, mult[0])
        to_add.append(x * y)

print("Part 2:", sum(to_add))