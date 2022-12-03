file = open("./input/input.txt")
lines = file.readlines()

max_calories_sum = 0
current_calories_sum = 0


def update_max():
    global max_calories_sum
    if current_calories_sum > max_calories_sum:
        max_calories_sum = current_calories_sum


for index, line in enumerate(lines):
    line = line.removesuffix("\n")
    if len(line) == 0:
        update_max()
        current_calories_sum = 0
    else:
        current_calories_sum += int(line)
        update_max()

print(max_calories_sum)
