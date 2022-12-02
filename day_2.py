with open(file='data.txt') as file:
    strategy_guide = file.read().split("\n")


ELF_SHAPES = {"A": 'r', "B": 'p', "C": 's'} 
USER_SHAPES = {"X": 'r', "Y": 'p', "Z": 's'}
SHAPE_POINTS = {'r': 1, 'p': 2, 's': 3}
IF_WINNING = {'A': "p", "B": "s", "C": "r"}
IF_LOSING = {'A': "s", "B": "r", "C": "p"}


total_score_a = 0
total_score_b = 0

for current_round in strategy_guide:
    elf_hand, user_hand = current_round.split(" ")

    # part one:
    if ELF_SHAPES[elf_hand] == USER_SHAPES[user_hand]:
        total_score_a += SHAPE_POINTS[USER_SHAPES[user_hand]] + 3
    elif ELF_SHAPES[elf_hand] == 'r' and USER_SHAPES[user_hand] == 'p' or ELF_SHAPES[elf_hand] == 'p' and USER_SHAPES[user_hand] == 's' \
        or ELF_SHAPES[elf_hand] == 's' and USER_SHAPES[user_hand] == 'r':
        total_score_a += SHAPE_POINTS[USER_SHAPES[user_hand]] + 6
    else:
        total_score_a += SHAPE_POINTS[USER_SHAPES[user_hand]]

    # part two:
    if user_hand == "X":
        total_score_b += SHAPE_POINTS[IF_LOSING[elf_hand]]
    elif user_hand == "Y":
        total_score_b += SHAPE_POINTS[ELF_SHAPES[elf_hand]] + 3
    else:
        total_score_b += SHAPE_POINTS[IF_WINNING[elf_hand]] + 6


# part one:
print(total_score_a)
# part two:
print(total_score_b)
