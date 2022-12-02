with open(file='data.txt') as file:
    strategy_guide = file.read().split("\n")


SHAPES = {"A": "X", "B": "Y", "C": "Z"}
SHAPE_POINTS = {"X": 1, "Y": 2, "Z": 3}
BEATS = {'A': "Y", "B": "Z", "C": "X"}
YIELDS_TO = {'A': "Z", "B": "X", "C": "Y"}


total_score = 0
updated_total_score = 0

for current_round in strategy_guide:
    elf_shape, user_shape = current_round.split(" ")

    # part one:
    if user_shape == BEATS[elf_shape]:
        total_score += SHAPE_POINTS[user_shape] + 6
    elif user_shape == SHAPES[elf_shape]:  # draw
        total_score += SHAPE_POINTS[user_shape] + 3
    elif user_shape == YIELDS_TO[elf_shape]:
        total_score += SHAPE_POINTS[user_shape]

    # part two:
    if user_shape == "X":
        updated_total_score += SHAPE_POINTS[YIELDS_TO[elf_shape]]
    elif user_shape == "Y":  # draw
        updated_total_score += SHAPE_POINTS[SHAPES[elf_shape]] + 3
    elif user_shape == "Z":
        updated_total_score += SHAPE_POINTS[BEATS[elf_shape]] + 6


# part one:
print(total_score)
# part two:
print(updated_total_score)

