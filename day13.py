from functools import cmp_to_key


with open(file='data.txt') as file:
    data = list(map(str.splitlines, file.read().strip().split("\n\n")))


def compare(left, right):
    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left > right:
            return -1

    if isinstance(left, list) and isinstance(right, list):
        if not left and right:
            return 1
        if left and not right:
            return -1

        i = j = 0  # i = left pointer, j = right pointer
        while i < len(left):
            if i == len(right):
                return -1

            comparison = compare(left[i], right[j])
            if comparison == 1:
                return 1
            if comparison == -1:
                return -1

            i += 1
            j += 1

        if i < len(right):
            return 1


total = 0
for index, (l, r) in enumerate(data):
    if compare(eval(l), eval(r)) == 1:
        total += index + 1

# part one:
print(total)


# part two:
with open(file='data.txt') as file:
    data = [line for line in file.read().strip().split("\n") if line]
    test = []  # not working with list comprehension for some reason
    for line in data:
        x = eval(line)
        test.append(x)

    sorted_order = sorted(test + [[[2]]] + [[[6]]], key=cmp_to_key(compare), reverse=True)
    print((sorted_order.index([[2]]) + 1) * (sorted_order.index([[6]]) + 1))
