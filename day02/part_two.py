# A -> Rock -> 1
# B -> Paper -> 2
# C -> Scissors -> 3

# X -> Lose
# Y -> Draw
# Z -> Win

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

lose_mapping = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

win_mapping = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draw_mapping = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

score = 0

for line in lines:
    opponent, player = line.removesuffix("\n").split(" ")
    if player == "X":
        player = lose_mapping[opponent]
    elif player == "Y":
        player = draw_mapping[opponent]
    else:
        player = win_mapping[opponent]

    line = opponent + player
    score += points[line]

print(score)



