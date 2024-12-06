import copy

with open('new.txt') as f:
        grid_original =  [list(line) for line in f.read().splitlines()]

def find_starting_point(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '^':
                return (x, y)

def move_forward(location, direction, grid):
    directions = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)
    }
    x, y = location
    moves = 0
    
    while True:
        if not 0 < x < len(grid[0])-1 or not 0 < y < len(grid)-1:
            return False, moves
        dx, dy = directions[direction]
        new_x, new_y = x + dx, y + dy

        if grid[new_y][new_x] == '#':
            return (x, y), moves
        
        x, y = new_x, new_y
        if grid[y][x] != 'X':
            moves += 1
        grid[y][x] = 'X'

def calculate_moves(grid, starting_point):
    visited_positions = set()
    direction = "up"
    total_moves = 1
    current_position = starting_point
    directions = ['up', 'right', 'down', 'left']

    while True:
        new_location, moves = move_forward(current_position, direction, grid)
        total_moves += moves

        if new_location:
            if (new_location[0], new_location[1], direction) in visited_positions:
                return False
            visited_positions.add((new_location[0], new_location[1], direction))

            current_index = directions.index(direction)
            direction = directions[(current_index + 1) % 4]
            current_position = new_location
        else:
            return total_moves

starting_point = find_starting_point(grid_original)
grid_original[starting_point[0]][starting_point[1]] = 'X'
total_moves = 1

grid2 = copy.deepcopy(grid_original)
print("Part 1:", calculate_moves(grid2,starting_point))

part2_moves = 0
for x, row in enumerate(grid_original):
    for y, cell in enumerate(row):
        new_grid = copy.deepcopy(grid_original)
        if cell == ".":
            new_grid[x][y] = "#"
        else:
            continue
        if not calculate_moves(new_grid, starting_point):
            part2_moves += 1

print("Part 2:", part2_moves)

