file = open("./input/input.txt")
lines = map(lambda _: _.removesuffix("\n"), file.readlines())

NOOP = "noop"
ADDX = "addx"
CRT_WIDTH = 40
CRT_HEIGHT = 6

current_cycle_number = 0
x = 1

result = 0

interest_points = [20, 60, 100, 140, 180, 220]

crt_board = ["." for i in range(CRT_WIDTH * CRT_HEIGHT)]


def print_crt_board():
    for i in range(CRT_WIDTH * CRT_HEIGHT):
        if i != 0 and i % CRT_WIDTH == 0:
            print("")
        print(crt_board[i], end="")


def evaluate_crt_pixel():
    sprite = [x - 1, x, x + 1]
    if current_cycle_number % CRT_WIDTH in sprite:
        crt_board[current_cycle_number] = "#"


for line in lines:
    tokens = line.split(" ")

    if tokens[0] == NOOP:
        evaluate_crt_pixel()
        current_cycle_number += 1
    else:
        for _ in range(2):
            evaluate_crt_pixel()
            current_cycle_number += 1
        x += int(tokens[1])

print_crt_board()
