with open("day1.txt", 'r') as file:
    pairs = [line.strip().split("   ") for line in file]

left, right = map(sorted, zip(*pairs))

abs_diff_total = sum(abs(int(l) - int(r)) for l, r in zip(left, right))
print(f"Part 1: {abs_diff_total}")

weighted_sum = sum(int(number) * right.count(number) for number in left)
print(f"Part 2: {weighted_sum}")