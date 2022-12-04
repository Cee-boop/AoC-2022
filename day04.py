with open(file='data.txt') as file:
    assignment_pairs = [line.split(",") for line in file.read().split("\n")]


def part_one(list_a, list_b):
    global first_total
    streak_a, streak_b = 0, 0

    for num in list_a:
        if num in list_b:
            streak_a += 1

    if streak_a == len(list_a):
        first_total += 1
        return

    for num in list_b:
        if num in list_a:
            streak_b += 1

    if streak_b == len(list_b):
        first_total += 1
        return


first_total = 0
second_total = 0

for pair in assignment_pairs:
    first_elf_start, first_elf_end = map(int, pair[0].split("-"))
    second_elf_start, second_elf_end = map(int, pair[1].split("-"))
    first_elf_assignments = [i for i in range(first_elf_start, first_elf_end + 1)]
    second_elf_assignments = [i for i in range(second_elf_start, second_elf_end + 1)]
    # part one:
    part_one(first_elf_assignments, second_elf_assignments)

    # part two:
    if first_elf_assignments[0] in second_elf_assignments or second_elf_assignments[0] in first_elf_assignments:
        second_total += 1


# part one:
print(first_total)
# part two:
print(second_total)
