with open('data.txt') as file:
    data = file.read().split("\n\n")
    monkeys = []

    for entry in data:
        parse_info = entry.split("\n")[1:]
        monkey_stats = {
            "items": list(map(int, parse_info[1].split("Starting items: ")[1].split(","))),
            "op": parse_info[2].split(" ")[-2:],
            "test": int(parse_info[3].split(" ")[-1]),
            "true": int(parse_info[4].split(" ")[-1]),
            "false": int(parse_info[5].split(" ")[-1])
        }

        monkeys.append(monkey_stats)


def indentify_operator(symbol: str, item: int, op_number: str) -> int:
    if op_number == "old":
        op_number = item
    if symbol == "*":
        return item * int(op_number)
    if symbol == "+":
        return item + int(op_number)


def product_of_all_tests() -> int:
    product = 1
    for monkey in monkeys:
        product *= monkey['test']
    return product


def initiate_monkey_business(number_of_rounds: int, stress_reliever_activated: bool) -> int:
    for _ in range(number_of_rounds):
        for i, monkey in enumerate(monkeys):
            for j, item in enumerate(monkeys[i]['items']):
                monkey_inspection_tally[i] += 1
                symbol, op_number = monkey['op'][0], monkey['op'][-1]
                worry_level = indentify_operator(symbol, item, op_number)

                if stress_reliever_activated:
                    worry_level //= 3
                modified_worry_level = worry_level % PRODUCT

                if worry_level % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(modified_worry_level)
                else:
                    monkeys[monkey['false']]['items'].append(modified_worry_level)

            monkey['items'] = []

    sorted_monkey_tallies = sorted(monkey_inspection_tally.values())
    return sorted_monkey_tallies[-2] * sorted_monkey_tallies[-1]


PRODUCT = product_of_all_tests()
monkey_inspection_tally = {i: 0 for i in range(len(monkeys))}

# part one:
print(initiate_monkey_business(20, stress_reliever_activated=True))
# part two:
print(initiate_monkey_business(10000, stress_reliever_activated=False))
