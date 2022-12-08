with open(file='data.txt') as file:
    terminal_output = file.read().split("\n")


DISK_SPACE = 70000000
UNUSED_SPACE = 30000000


def get_directory_sizes(directory: dict) -> tuple:
    if type(directory) is int:  # file, not directory
        return directory, 0

    directory_size, output = 0, 0
    for next_directory in directory.values():
        ds, o = get_directory_sizes(next_directory)  # ds == directory_size, o == output
        directory_size += ds
        output += o

    if directory_size <= 100000:
        output += directory_size
    return directory_size, output


def individual_directory_size(directory: dict) -> int:
    if type(directory) is int:
        return directory
    return sum(map(individual_directory_size, directory.values()))


def calculate_free_space(directory: dict) -> int:
    output = float('inf')
    if individual_directory_size(directory) >= target_size:
        output = individual_directory_size(directory)

    for new_directory in directory.values():
        if type(new_directory) is int:
            continue
        smallest_directory = calculate_free_space(new_directory)
        output = min(output, smallest_directory)

    return output


def build_filesystem():
    current_directory = filesystem = {}  # current directory starts at the beginning of filesystem
    previous_directories = []

    for line in terminal_output:
        if "$ ls" == line:
            continue

        if "$ cd" == line[:4]:
            directory = line.split(" ")[-1]

            if directory == "/":
                current_directory = filesystem  # move back to root
                previous_directories = []
            elif directory == "..":
                current_directory = previous_directories.pop()  # move up a directory
            else:
                if directory not in current_directory:
                    current_directory[directory] = {}  # create new directory
                previous_directories.append(current_directory)
                current_directory = current_directory[directory]  # move into new directory

        else:
            if line.split(" ")[0] == "dir" and line.split(" ")[-1] not in current_directory:
                current_directory[line.split(" ")[-1]] = {}
            else:
                file_size, file_name = line.split(" ")
                current_directory[file_name] = int(file_size)

    return filesystem


new_filesystem = build_filesystem()
target_size = individual_directory_size(new_filesystem) - (DISK_SPACE - UNUSED_SPACE)

# part one:
print(get_directory_sizes(new_filesystem)[1])
# part two:
print(calculate_free_space(new_filesystem))
