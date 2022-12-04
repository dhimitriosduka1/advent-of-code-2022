file = open("./input/input.txt")
lines = file.readlines()


def get_coordinates(token: str) -> (int, int):
    coordinates = token.split("-")
    return int(coordinates[0]), int(coordinates[1])


def does_overlap() -> bool:
    return (y1 >= x2) and (x1 <= y2)


result = 0

for line in lines:
    line = line.removesuffix("\n")
    first_token, second_token = line.split(",")

    x1, y1 = get_coordinates(first_token)
    x2, y2 = get_coordinates(second_token)

    if does_overlap():
        result += 1

print(result)
