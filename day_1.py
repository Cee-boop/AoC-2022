with open(file='data.txt') as file:
    data = file.read().split("\n\n")

most_calories = 0
all_calorie_totals = []
for i, entry in enumerate(data):
    curr_calories = sum(map(int, entry.split("\n")))
    all_calorie_totals.append(curr_calories)
    most_calories = max(most_calories, curr_calories)

# part one:
print(most_calories)
# part two:
print(sum(sorted(all_calories_totals)[-3:]))
