file = open("./input/input.txt")
lines = file.readlines()

max_calories_sum = 0
current_calories_sum = 0

for line in lines:
    line = line[:len(line) - 1]
    if len(line) == 0:
        if current_calories_sum > max_calories_sum:
            max_calories_sum = current_calories_sum
        current_calories_sum = 0
    else:
        current_calories_sum += int(line)

print(max_calories_sum)

