with open("day2.txt", "r") as file:
    lines = [line.strip().split() for line in file]

def calc_diffs(line):
    nums = list(map(int, line))
    diffs = [b - a for a, b in zip(nums, nums[1:])]
    return diffs if all(diff != 0 for diff in diffs) else []

def is_safe(line):
    diffs = calc_diffs(line)
    if not diffs:
        return False
    asc = all(diff > 0 for diff in diffs)
    desc = all(diff < 0 for diff in diffs)
    within_range = all(1 <= abs(diff) <= 3 for diff in diffs)
    return (asc or desc) and within_range

def is_safe_dampener(line):
    if is_safe(line):
        return True
    for i in range(len(line)):
        new_line = line[:i] + line[i+1:]
        if is_safe(new_line):
            return True
    return False

safe = sum(is_safe(line) for line in lines)
safe_dampener = sum(is_safe_dampener(line) for line in lines)

print(f"Part 1: {safe}")
print(f"Part 2: {safe_dampener}")