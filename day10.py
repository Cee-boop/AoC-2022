with open('data.txt') as file:
    data = file.read().split("\n")


def draw_pixel():
    # IDK HOW ELSE TO GET THIS PART TO WORK LOL
    
    lst1 = [i for i in range(40)]
    lst2 = [i for i in range(40, 80)]
    lst3 = [i for i in range(80, 120)]
    lst4 = [i for i in range(120, 160)]
    lst5 = [i for i in range(160, 200)]
    lst6 = [i for i in range(200, 240)]

    column = 0
    if cycle_counter in lst1:
        column = lst1.index(cycle_counter)
    if cycle_counter in lst2:
        column = lst2.index(cycle_counter)
    if cycle_counter in lst3:
        column = lst3.index(cycle_counter)
    if cycle_counter in lst4:
        column = lst4.index(cycle_counter)
    if cycle_counter in lst5:
        column = lst5.index(cycle_counter)
    if cycle_counter in lst6:
        column = lst6.index(cycle_counter)

    if sprite_position[column - 1] == "#":
        crt[current_row][column - 1] = "#"


def check_cycle():
    global signal_strength
    if cycle_counter in [20, 60, 100, 140, 180, 220]:
        signal_strength += cycle_counter * signal_register


def move_sprite(starting_index: int):
    global sprite_position
    sprite_position = ["." for _ in range(40)]
    for _ in range(3):
        sprite_position[starting_index] = "#"
        starting_index += 1
        if starting_index > 39:
            break


def change_row():
    global current_row
    if cycle_counter in [40, 80, 120, 160, 200]:
        current_row += 1


def display(grid: list):
    string = [[str(e) for e in row] for row in grid]
    lengths = [max(map(len, col)) for col in zip(*string)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lengths)
    display = [fmt.format(*row) for row in string]
    print('\n'.join(display))
    print("\n")


signal_register = 1
cycle_counter = 0
signal_strength = 0

crt = [["."] * 40 for _ in range(6)]
col_length = current_row = 0
sprite_position = ["." for _ in range(40)]
move_sprite(0)

for command in data:
    if command == "noop":
        cycle_counter += 1
        check_cycle()
        draw_pixel()
        change_row()
        continue

    else:
        for _ in range(2):
            cycle_counter += 1
            check_cycle()
            draw_pixel()
            change_row()

        number = int(command.split(" ")[-1])
        signal_register += number
        move_sprite(signal_register - 1)


# part one:
print(signal_strength)
# part two:
display(crt)
