with open("day7.txt", 'r') as file:
    lines = [line.strip() for line in file]
    
def calculate_pairs(current, number, pairs):
    if current > number:
        return False
    if current == number and not pairs:
        return True
    if not pairs:
        return False
    first = int(pairs[0])
    for op in ("+", "*", "||"):
        if op == "+":
            if calculate_pairs(current + first, number, pairs[1:]):
                return True
        elif op == "*":
            if calculate_pairs(current * first, number, pairs[1:]):
                return True
        elif op == "||":
            if calculate_pairs(int(str(current) + str(first)), number, pairs[1:]):
                return True
    return False

total = 0
for line in lines:
    number = int(line.split(":")[0])
    pairs = line.split(":")[1].split(" ")[1:]
    initial_value = int(pairs[0])
    pairs = pairs[1:]
    if calculate_pairs(initial_value, number, pairs):
        total += number

print(f"Part 1: {total}")