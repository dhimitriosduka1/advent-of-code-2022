file = open("./input/input.txt")
lines = file.readlines()


def get_coordinates(token: str) -> (int, int):
    coordinates = token.split("-")
    return int(coordinates[0]), int(coordinates[1])


def overlaps() -> bool:
    return (x1 == x2 and y1 == y2) or (x2 >= x1 and y2 <= y1) or (x1 >= x2 and y1 <= y2)


result = 0

for line in lines:
    line = line.removesuffix("\n")
    first_token, second_token = line.split(",")

    x1, y1 = get_coordinates(first_token)
    x2, y2 = get_coordinates(second_token)

    if overlaps():
        result += 1

print(result)
