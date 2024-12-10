with open("day9.txt") as file:
    input = file.readline().strip()

def get_sequence(number, index, sequence_number):
    if index == 0:
        return str(number)
    if index % 2 == 0:
        return str(number) * sequence_number
    return "." * (sequence_number + 1)

sequence_number = 0
output = []

for index, number in enumerate(input):
    if index == 0:
        for(xx) in range(int(number)):
            output.append(str(sequence_number))
        sequence_number += 1
    elif index % 2 == 0:
        for xx in range(int(number)):
            output.append(str(sequence_number))
        sequence_number += 1
    else:
        for xx in range(int(number)):
            output.append(".")

output = list(output)
reversed = output[::-1]

for each in range(len(output)):
    if output[each] == ".":

        if output[each:].count(".") == len(output[each:]):
            break
        for element in range(len(reversed)):
            if reversed[element] != ".":
                output[each] = reversed[element]
                output[len(output) - element - 1] = "."
                reversed[element] = "." 
                break

checksum = 0
for index, number in enumerate(output):
    if number != ".":
        checksum += int(number) * (index)
print(f"Part 1: {checksum}")

