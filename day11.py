import time
import functools

start_time = time.time()

with open("day11.txt") as file:
    stones = file.readline().split()

@functools.cache
def process_stone(stone):
    if int(stone) == 0:
        return ["1"]
    if len(stone) % 2 == 0:
        mid = len(stone) // 2
        return [stone[:mid], str(int(stone[mid:]))]
    return [str(int(stone) * 2024)]

@functools.cache
def count_stones(stone, blinks):
    if blinks == 0:
        return 1
    new_stones = process_stone(stone)
    return sum([count_stones(new_stone, blinks - 1) for new_stone in new_stones])

print(f"Part 1: {sum([count_stones(stone, 25) for stone in stones])}")
print(f"Part 2: {sum([count_stones(stone, 75) for stone in stones])}")
