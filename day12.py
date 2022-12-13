from collections import deque


with open('data.txt') as file:
    data = file.read().split("\n")
    alpha = "abcdefghijklmnopqrstuvwxyz"
    char_map = {alpha[i]: i + 1 for i in range(len(alpha))}  # convert letters to numbers
    height_grid = []

    for i, line in enumerate(data):
        height_grid.append([])
        for j, char in enumerate(line):
            if char == "S":
                start_row, start_col = (i, j)
                height_grid[i].append(char_map['a'])
            elif char == "E":
                height_grid[i].append(char_map['z'])
                end_row, end_col = (i, j)
            else:
                new_char = char_map[char]
                height_grid[i].append(new_char)


GRID_LENGTH = len(height_grid)
GRID_WIDTH = len(height_grid[0])
visualisation = [["."] * GRID_WIDTH for _ in range(GRID_LENGTH)]


def display_grid(grid: list):
    string = [[str(e) for e in row] for row in grid]
    lengths = [max(map(len, col)) for col in zip(*string)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lengths)
    display = [fmt.format(*row) for row in string]
    print('\n'.join(display))
    print("\n")


def find_smallest_path(coord_one: int, coord_two: int, find_multiple_paths: bool) -> int:
    queue = deque()
    queue.append([0, coord_one, coord_two])
    visited = {(coord_one, coord_two)}

    while queue:
        distance, r, c = queue.popleft()

        for new_row, new_col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if new_row >= GRID_LENGTH or new_col >= GRID_WIDTH or new_col < 0 or new_row < 0:
                continue
            if (new_row, new_col) in visited:
                continue

            if find_multiple_paths:
                if height_grid[new_row][new_col] - height_grid[r][c] < -1:  # find paths less than or equal to end
                    continue
            if not find_multiple_paths:
                if height_grid[new_row][new_col] - height_grid[r][c] > 1:
                    continue

            if find_multiple_paths:
                if height_grid[new_row][new_col] == 1:  # first 'a' found
                    return distance + 1
            if not find_multiple_paths:
                if new_row == end_row and new_col == end_col:  # path found
                    return distance + 1

            print(f"current: {new_row, new_col}")
            visualisation[new_row][new_col] = "X"
            display_grid(visualisation)
            visited.add((new_row, new_col))
            queue.append((distance + 1, new_row, new_col))


# part one:
print(find_smallest_path(start_row, start_col, find_multiple_paths=False))
# part two:
print(find_smallest_path(end_row, end_col, find_multiple_paths=True))
