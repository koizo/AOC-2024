with open('day4.txt', 'r') as f:
    grid = [line.strip() for line in f]

size = len(grid)

grid = [list(row) for row in grid]

def lookup_array(array, word, direction, x, y):
    direction_moves = {
        "e": (0, 1),
        "w": (0, -1),
        "n": (-1, 0),
        "s": (1, 0),
        "se": (1, 1),
        "sw": (1, -1),
        "ne": (-1, 1),
        "nw": (-1, -1),
    }
    
    xx, yy = direction_moves.get(direction)
    for i in range(len(word)):
        if 0 <= x < size and 0 <= y < size:
            if word[i] != array[x][y]:
                return False
            x += xx
            y += yy
        else:
            return False
    return True

count = 0
directions = ["e", "w", "n", "s", "se", "sw", "ne", "nw"]
for i in range(size):
    for j in range(size):
        for direction in directions:
            if lookup_array(grid, "XMAS", direction, i, j):
                count += 1
                
print(f"Part 1: {count}")

count = 0
directions = {
    "nw": (-1, -1),
    "ne": (-1, 1),
    "sw": (1, -1),
    "se": (1, 1)
}

for i in range(1, size - 1):
    for j in range(1, size - 1):
        if grid[i][j] == "A":
            diagonals = [grid[i + x][j + y] for x, y in directions.values()]
            if all(cell in ("S", "M") for cell in diagonals):
                if diagonals[0] != diagonals[3] and diagonals[1] != diagonals[2]:
                    count += 1

print(f"Part 2: {count}")