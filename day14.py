#############################PART ONE###########################
with open(file='data.txt') as file:
    data = [line.split(" -> ") for line in file.read().split("\n")]
    cave_grid = [["."] * 20000 for _ in range(20000)]
    sand_source = cave_grid[0][500] = "+"


def display_grid(grid: list):
    string = [[str(e) for e in row] for row in grid]
    lengths = [max(map(len, col)) for col in zip(*string)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lengths)
    display = [fmt.format(*row) for row in string]
    print('\n'.join(display))
    print("\n")


# rock placement:
for coord_line in data:
    for i in range(len(coord_line) - 1):
        c, r = map(int, coord_line[i].split(","))  # current coordinates
        c_target, r_target = map(int, coord_line[i+1].split(","))  # target coordinates
        cave_grid[r][c] = "#"

        while True:
            if r == r_target and c == c_target:
                break

            if c < c_target:
                c += 1
            elif c == c_target:
                pass
            else:
                c -= 1

            if r < r_target:
                r += 1
            elif r == r_target:
                pass
            else:
                r -= 1

            cave_grid[r][c] = "#"


def sand_simulation_part_one():
    sand_count = 0
    for _ in range(5000):
        r, c = 0, 500
        new_pos_found = False

        while r < len(cave_grid) - 1:
            if cave_grid[r + 1][c] == "#" or cave_grid[r + 1][c] == "o":
                for nr, nc in [(r+1, c-1), (r+1, c+1)]:
                    if cave_grid[nr][nc] == ".":
                        r, c = nr, nc
                        new_pos_found = True
                        break

                if new_pos_found:
                    new_pos_found = False
                    continue
                cave_grid[r][c] = "o"
                sand_count += 1
                break

            elif cave_grid[r+1][c] == ".":
                r += 1

    return sand_count


print(sand_simulation_part_one())

############################PART TWO#############################
with open(file='data.txt') as file:
    data = [line.split(" -> ") for line in file.read().split("\n")]
    cave_grid = [["."] * 20000 for _ in range(20000)]
    sand_source = cave_grid[0][500] = "+"


def display_grid(grid: list):
    string = [[str(e) for e in row] for row in grid]
    lengths = [max(map(len, col)) for col in zip(*string)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lengths)
    display = [fmt.format(*row) for row in string]
    print('\n'.join(display))
    print("\n")


max_y_coord = float('-inf')

# rock placement:
for coord_line in data:
    for i in range(len(coord_line) - 1):
        c, r = map(int, coord_line[i].split(","))  # current coordinates
        c_target, r_target = map(int, coord_line[i+1].split(","))  # target coordinates
        cave_grid[r][c] = "#"
        max_y_coord = max(max_y_coord, r_target)

        while True:
            if r == r_target and c == c_target:
                break

            if c < c_target:
                c += 1
            elif c == c_target:
                pass
            else:
                c -= 1

            if r < r_target:
                r += 1
            elif r == r_target:
                pass
            else:
                r -= 1

            cave_grid[r][c] = "#"


def sand_simulation_part_two():
    global max_y_coord
    max_y_coord = max_y_coord + 2
    # sample input:
    for col, pos in enumerate(cave_grid[max_y_coord]):
        cave_grid[max_y_coord][col] = "#"

    sand_count = 0
    r = c = None

    for _ in range(30000):
        if (r, c) == (0, 500):
            return sand_count

        r, c = 0, 500
        new_pos_found = False

        while r < len(cave_grid[max_y_coord]) - 1:
            if cave_grid[r + 1][c] == "#" or cave_grid[r + 1][c] == "o":
                for nr, nc in [(r+1, c-1), (r+1, c+1)]:
                    if cave_grid[nr][nc] == ".":
                        r, c = nr, nc
                        new_pos_found = True
                        break

                if new_pos_found:
                    new_pos_found = False
                    continue
                cave_grid[r][c] = "o"
                sand_count += 1
                break

            elif cave_grid[r+1][c] == ".":
                r += 1


print(sand_simulation_part_two())
