with open(file='data.txt') as file:
    tree_map = [list(map(int, line)) for line in file.read().split("\n")]


GRID_LENGTH = len(tree_map)
GRID_WIDTH = len(tree_map[0])
EDGES_COUNT = (GRID_LENGTH * 2) + (GRID_WIDTH - 2) * 2


def look_up(r: int, c: int, current_tree: int) -> int:
    global visible_trees
    view_line = [row[c] for row in tree_map[:r]][::-1]
    score = current_direction_tree_count(view_line, current_tree)

    if (r, c) in indices_checked or r == 0 or r == GRID_LENGTH - 1 or c == 0 or c == GRID_WIDTH - 1:
        return score

    if max([row[c] for row in tree_map][:r]) < current_tree:
        indices_checked.append((r, c))
        visible_trees += 1

    return score


def look_down(r: int, c: int, current_tree: int) -> int:
    global visible_trees
    view_line = [row[c] for row in tree_map[r+1:]]
    score = current_direction_tree_count(view_line, current_tree)

    if (r, c) in indices_checked or r == 0 or r == GRID_LENGTH - 1 or c == 0 or c == GRID_WIDTH - 1:
        return score

    if max([row[c] for row in tree_map][r+1:]) < current_tree:
        indices_checked.append((r, c))
        visible_trees += 1

    return score


def look_left(r: int, c: int, current_tree: int) -> int:
    global visible_trees
    view_line = [row for row in tree_map[r][:c]][::-1]
    score = current_direction_tree_count(view_line, current_tree)

    if (r, c) in indices_checked or r == 0 or r == GRID_LENGTH - 1 or c == 0 or c == GRID_WIDTH - 1:
        return score

    if max(tree_map[r][:c]) < current_tree:
        indices_checked.append((r, c))
        visible_trees += 1

    return score


def look_right(r: int, c: int, current_tree: int) -> int:
    global visible_trees
    view_line = [row for row in tree_map[r][c+1:]]
    score = current_direction_tree_count(view_line, current_tree)

    if (r, c) in indices_checked or r == 0 or r == GRID_LENGTH - 1 or c == 0 or c == GRID_WIDTH - 1:
        return score

    if max(tree_map[r][c+1:]) < current_tree:
        indices_checked.append((r, c))
        visible_trees += 1

    return score


def current_direction_tree_count(view_line: list, current_tree: int) -> int:
    tree_count = 0
    for tree in view_line:
        if tree >= current_tree:
            tree_count += 1
            break
        else:
            tree_count += 1

    return tree_count


visible_trees = 0
scenic_score = 0
indices_checked = []

for r, row in enumerate(tree_map):
    for c, col in enumerate(row):
        sum_one, sum_two, sum_three, sum_four = look_up(r, c, tree_map[r][c]), look_down(r, c, tree_map[r][c]), look_right(r, c, tree_map[r][c]), look_left(r, c, tree_map[r][c])
        new_scenic_score = sum_one * sum_two * sum_three * sum_four
        scenic_score = max(scenic_score, new_scenic_score)


# part one:
print(visible_trees + EDGES_COUNT)
# part two:
print(scenic_score)
