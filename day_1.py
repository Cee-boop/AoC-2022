with open(file='data.txt') as file:
    data = file.read().split("\n\n")

# part one:
print(max([sum(map(int, entry.split("\n"))) for entry in data]))
# part two:
print(sum(sorted([sum(map(int, entry.split("\n"))) for entry in data])[-3:]))
