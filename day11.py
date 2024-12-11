import functools

with open("day11.txt") as file:
    stones = file.readline().split()

def process_stone(stone):
    return (
        ["1"] if int(stone) == 0 else
        [stone[:len(stone) // 2], str(int(stone[len(stone) // 2:]))] if len(stone) % 2 == 0 else
        [str(int(stone) * 2024)]
    )

@functools.cache
def count_stones(stone, blinks):
    return 1 if blinks == 0 else sum(count_stones(new_stone, blinks - 1) for new_stone in process_stone(stone))

print(f"Part 1: {sum([count_stones(stone, 25) for stone in stones])}")
print(f"Part 2: {sum([count_stones(stone, 75) for stone in stones])}")
