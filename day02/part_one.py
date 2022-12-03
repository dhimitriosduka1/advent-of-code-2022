# A -> Rock -> 1
# B -> Paper -> 2
# C -> Scissors -> 3

# X -> Rock -> 1
# Y -> Paper -> 2
# Z -> Scissors -> 3

# Win -> 6
# Draw -> 3
# Lose -> 0

file = open("./input/input.txt")
lines = file.readlines()

points = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6
}

score = 0

for line in lines:
    line = line.replace(" ", "").removesuffix("\n")
    score += points[line]

print(score)



