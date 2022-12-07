file = open("./input/input.txt")
data = file.readline()


def has_unique_chars(string: str) -> bool:
    return len(set(string)) == len(string)


marker_index = 0

for i in range(len(data) - 3):
    marker = data[i:i + 4]
    if has_unique_chars(marker):
        marker_index = i + 4
        break

print(marker_index)
