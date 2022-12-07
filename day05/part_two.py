file = open("./input/input.txt")
lines = file.readlines()


def parse_instruction(data: str) -> (int, int, int):
    tokens = data.split(" ")
    return int(tokens[1]), int(tokens[3]), int(tokens[5])


def format_crate(data: str) -> [str]:
    data = data.removesuffix("\n")[1::4]
    return [char for char in data]


def transpose() -> [[str]]:
    crate_stacks = []
    for i in range(len(crates[0])):
        crate_stacks.append([])
        for j in range(len(crates)):
            if crates[j][i].isalpha():
                crate_stacks[i].append(crates[j][i])
        crate_stacks[i] = crate_stacks[i][::-1]
    return crate_stacks


break_index = 0

for line in lines:
    if len(line.strip()) == 0:
        break
    break_index += 1

crates = lines[:break_index - 1]
crates = list(map(format_crate, crates))

instructions = lines[break_index + 1:]

crates = transpose()

for instruction in instructions:
    amount, origin, destination = parse_instruction(instruction)
    temp_stack = []
    for i in range(amount):
        temp_stack.append(crates[origin - 1].pop())

    for i in range(len(temp_stack)):
        crates[destination - 1].append(temp_stack[len(temp_stack) - 1 - i])

result = ''
for i in range(len(crates)):
    result += crates[i].pop()

print(result)
