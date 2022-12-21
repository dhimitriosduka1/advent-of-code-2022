import operator
from functools import reduce

from day11.model.Monkey import Monkey
from day11.model.Opertation import Operation
from day11.model.Test import Test

ROUNDS = 10000

file = open("./input/input.txt").read()
parts = file.split("\n\n")

monkeys = []

for part in parts:
    instructions = part.split("\n")
    starting_items = [float(item.strip()) for item in instructions[1].split(":")[1].split(",")]
    operation = instructions[2][23]
    value = instructions[2][24:]

    divisor = float(instructions[3][21:])
    true_index = int(instructions[4][29:])
    false_index = int(instructions[5][29:])

    monkeys.append(Monkey(
        starting_items=starting_items,
        operation=Operation(operation=operation, value=value),
        test=Test(divisor=divisor, true_index=true_index, false_index=false_index)
    ))

modulo = 1

for monkey in monkeys:
    modulo *= monkey.test.divisor

for _ in range(ROUNDS):
    for monkey in monkeys:

        starting_items_length = len(monkey.starting_items)

        for currently_inspection_item in monkey.starting_items:

            monkey.number_of_inspected_items += 1

            new_worry_level = monkey.operation.apply(currently_inspection_item)
            new_worry_level %= modulo

            if new_worry_level % monkey.test.divisor == 0:
                monkeys[monkey.test.true_index].starting_items.append(float(new_worry_level))
            else:
                monkeys[monkey.test.false_index].starting_items.append(float(new_worry_level))

        monkey.starting_items = monkey.starting_items[starting_items_length:]

monkeys.sort(key=lambda x: x.number_of_inspected_items, reverse=True)
print(monkeys[0].number_of_inspected_items * monkeys[1].number_of_inspected_items)
