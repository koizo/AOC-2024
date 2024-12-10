with open("day10.txt") as file:
    map = [line.strip() for line in file]

def find_starting(map_data):
    return [(i, j)
            for i, row in enumerate(map_data)
            for j, val in enumerate(row)
            if int(val) == 0]


def find_next(map_data, x, y, number):
    if 0 <= x < len(map_data) and 0 <= y < len(map_data) and map_data[x][y] != '.' and int(map_data[x][y]) == number:
        return x, y
    return None

def recursive_count(map_data, x, y, number, visited=None, check_visited=True):
    visited = visited or set()

    if check_visited and (x, y) in visited:
        return 0
    visited.add((x, y))

    if number == 9:
        return 1

    total_ways = 0
    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        nxt = find_next(map_data, nx, ny, number + 1)
        if nxt:
            total_ways += recursive_count(map_data, nxt[0], nxt[1], number + 1, visited, check_visited)

    return total_ways

starting_locations = find_starting(map)
total_paths_part1 = 0
total_paths_part2 = 0

for x, y in starting_locations:
    total_paths_part1 += recursive_count(map, x, y, 0)
    total_paths_part2 += recursive_count(map, x, y, 0, check_visited=False)

print(f"Part 1: {total_paths_part1}")
print(f"Part 2: {total_paths_part2}")
