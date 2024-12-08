def find_pairs(grid):
    pairs = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != ".":    
                if grid[y][x] in pairs:
                    pairs[grid[y][x]].append((x,y))
                else:
                    pairs[grid[y][x]] = [(x,y)]
    
    return pairs

# Part 1

with open("day8.txt") as file:
    grid = file.read().splitlines()

pairs = find_pairs(grid)
antinodes = set()

for key in pairs:
    for i in range(len(pairs[key])):
        for j in range(i, len(pairs[key])):

            distance_x = pairs[key][j][0] - pairs[key][i][0]
            distance_y = pairs[key][j][1] - pairs[key][i][1]

            antinode_one = (pairs[key][i][0] - distance_x, pairs[key][i][1] - distance_y)
            antinode_two = (pairs[key][j][0] + distance_x, pairs[key][j][1] + distance_y)

            for antinode in [antinode_one, antinode_two]:
                    x, y = antinode
                    if antinode != pairs[key][i] and antinode != pairs[key][j] and 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                        antinodes.add(antinode)
           
print(f"Part 1: {len(antinodes)}")

# Part 2
with open("day8.txt") as file:
    grid = file.read().splitlines()

pairs = find_pairs(grid)
number_anti = 0
for key in pairs:
    for i in range(len(pairs[key])):
        for j in range(i, len(pairs[key])):
            for xx in range(len(grid[0])):
                distance_x = (pairs[key][j][0] - pairs[key][i][0]) * xx
                distance_y = (pairs[key][j][1] - pairs[key][i][1]) * xx

                antinode_one = ((pairs[key][i][0] - distance_x), (pairs[key][i][1] - distance_y))
                antinode_two = ((pairs[key][j][0] + distance_x), (pairs[key][j][1] + distance_y))

                for antinode in [antinode_one, antinode_two]:
                    x, y = antinode
                    if antinode != pairs[key][i] and antinode != pairs[key][j] and 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                        if grid[y][x] == ".":
                            grid[y] = grid[y][:x] + "#" + grid[y][x+1:]
                            number_anti += 1
                        
count = sum([1 for row in grid for elem in row if elem != "."])
print(f"Part 2: {count}")
