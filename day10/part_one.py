file = open("./input/input.txt")
lines = map(lambda _: _.removesuffix("\n"), file.readlines())

NOOP = "noop"
ADDX = "addx"

current_cycle_number = 0
x = 1

result = 0

interest_points = [20, 60, 100, 140, 180, 220]


def add_to_result():
    global result
    if current_cycle_number in interest_points:
        result += current_cycle_number * x


for line in lines:
    tokens = line.split(" ")

    if tokens[0] == NOOP:
        current_cycle_number += 1
        add_to_result()
    else:
        for _ in range(2):
            current_cycle_number += 1
            add_to_result()
        x += int(tokens[1])

print(result)
