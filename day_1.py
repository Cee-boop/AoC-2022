with open(file='data.txt') as file:
    data = file.read().split("\n\n")
    all_calorie_counts = [sum(map(int, entry.split("\n"))) for entry in data]

# part one:
print(max(all_calorie_counts))
# part two:
print(sum(sorted(all_calorie_counts)[-3:]))
