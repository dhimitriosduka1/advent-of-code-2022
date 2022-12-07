file = open("./input/input.txt")
data = file.readline()


def has_unique_chars(string: str) -> bool:
    return len(set(string)) == len(string)


marker_index = 0
marker_length = 4

for i in range(len(data) - marker_length - 1):
    marker = data[i:i + marker_length]
    if has_unique_chars(marker):
        marker_index = i + marker_length
        break

print(marker_index)
