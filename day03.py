with open(file='data.txt') as file:
    data = file.read().split("\n")


PRIORITY_INDEX = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part_one():
    priority_total = 0
    
    for entry in data:
        mid_point = len(entry) // 2
        compartment_a, compartment_b = entry[:mid_point], entry[mid_point:]
        for character in compartment_a:
            if character in compartment_b:
                priority_total += PRIORITY_INDEX.index(character) + 1
                break

    return priority_total


def part_two():
    start, end = 0, 3  # starting index positions
    priority_total = 0
    
    while end <= len(data):
        compartment_a, compartment_b, compartment_c = data[start:end]
        for character in compartment_a:
            if character in compartment_b and character in compartment_c:
                priority_total += PRIORITY_INDEX.index(character) + 1
                break
        
        start += 3
        end += 3

    return priority_total


print(part_one())
print(part_two())
