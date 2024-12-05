with open('day5.txt', 'r') as f:
    lines = [line.strip() for line in f]

orders = {}
ordering = []
parsing_orders = True

for line in lines:
    if not line:
        parsing_orders = False
        continue

    if parsing_orders:
        key, value = line.split("|")
        orders.setdefault(key, []).append(value)
    else:
        ordering.append(line.split(","))

# Part 1
total_sum = 0
to_order = []

for print_order in ordering:
    validated = []
    invalid = False

    for number in print_order:
        if any(valid in orders.get(number, []) for valid in validated):
            invalid = True
            to_order.append(print_order)
            break
        validated.append(number)

    if not invalid:
        total_sum += int(print_order[len(print_order) // 2])

print(f"Part 1: {total_sum}")

# Part 2
end_orders = []

for order in to_order:
    validated = []

    for number in order:
        invalid = False

        for index, valid in enumerate(validated):
            if valid in orders.get(number, []) and number not in validated:
                validated.insert(index, number)
                invalid = True
                break

        if not invalid:
            validated.append(number)

    end_orders.append(validated)

total_sum = 0
for order in end_orders:
    total_sum += int(order[len(order) // 2])

print(f"Part 2: {total_sum}")