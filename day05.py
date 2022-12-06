class StackGenerator:
    def __init__(self, parsing_data: list, grid_size: int):
        self.final_output = {}
        self.parsing_data = parsing_data
        self.grid_size = grid_size
        self.build_crate_grid()

    def build_crate_grid(self):
        # 4 empty strings equates to 1 space
        crate_grid = [[""] * self.grid_size for _ in range(self.grid_size)]
        for r, row in enumerate(self.parsing_data):
            c, empty_string_counts = 0, 0
            for element in row:
                if not element:
                    empty_string_counts += 1
                    if empty_string_counts % 4 == 0:
                        c += 1
                else:
                    crate_grid[r][c] = element
                    c += 1

        self.convert_to_dict(crate_grid)

    def convert_to_dict(self, grid: list):
        for c in range(len(grid[0])):
            self.final_output[c + 1] = []
            for r in range(len(grid)):
                if grid[r][c]:
                    self.final_output[c + 1].append(grid[r][c])

            if self.final_output[c + 1]:
                self.final_output[c + 1] = self.final_output[c + 1][::-1]
            else:
                del self.final_output[c + 1]


class CrateMover9001:
    def __init__(self, crate_stacks: dict):
        self.crate_stacks = crate_stacks

    def display_stacks(self):
        print(self.crate_stacks)

    def move_single_crate(self, rearrangement_instructions: list):
        crates_to_move, current_stack, new_stack = rearrangement_instructions
        for _ in range(crates_to_move):
            current_crate = self.crate_stacks[current_stack].pop()
            self.crate_stacks[new_stack].append(current_crate)

    def move_multiple_crates_at_once(self, rearrangement_instructions: list):
        crates_to_move, current_stack, new_stack = rearrangement_instructions
        crane_load = [self.crate_stacks[current_stack].pop() for _ in range(crates_to_move)]
        self.crate_stacks[new_stack] += crane_load[::-1]

    def identify_top_crates(self) -> str:
        return "".join([stack[-1] for stack in self.crate_stacks.values()])


if __name__ == "__main__":
    from copy import deepcopy
    with open(file='data.txt') as file:
        data = file.read()
        splice_point = [i for i in range(len(data.split("\n"))) if len(data.split("\n")[i]) == 0][0]
        stack_data = [line.split(" ") for line in data.split("\n")][:splice_point - 1]
        instructions = [list(map(int, line.replace("move ", "").replace("from ", " ").replace("to ", " ").split("  "))) for line in data.split("\n")[splice_point + 1:]]

    crate_stacks = StackGenerator(stack_data, splice_point).final_output
    muddy_crane = CrateMover9001(crate_stacks)
    shiny_new_crane = CrateMover9001(deepcopy(crate_stacks))

    for entry in instructions:
        muddy_crane.move_single_crate(entry)
        shiny_new_crane.move_multiple_crates_at_once(entry)

    # part one:
    print(muddy_crane.identify_top_crates())
    # part two:
    print(shiny_new_crane.identify_top_crates())
