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

rev = {}
for index, element in enumerate(output):
    if element != ".":
        if element in rev:
            rev[element]["count"] += 1
            rev[element]["last"] = index
        else:
            rev[element] = {"count": 1, "last": index}

for each in range(len(reversed)):
    if number == reversed[each]:
        continue

    if reversed[each] != ".":
        number = reversed[each]
        count = rev[number]["count"]
        index = 0
        location = 0
        last_seen = rev[number]["last"]
        for element in range(0, last_seen):

            if output[element] == ".":
                index += 1
                if index == count:
                    location = element-(count-1)
                    if int(location) < int(last_seen):
                        for i in range(count):
                                pos = int(last_seen - i)
                                output[pos] = "."
                        break
        
            else:
                index = 0
                location = 0
        
        if location > 0 and int(location) < int(last_seen):
            for i in range(count):
                output[location + i] = number
checksum = 0
for index, number in enumerate(output):
    if number != ".":
        checksum += int(number) * (index)
print(f"Part 2: {checksum}")