file = open("./input/input.txt")
lines = file.readlines()


def get_priority(c: str) -> int:
    lower_case_ascii_offset = 96
    upper_case_ascii_offset = 38
    return ord(c) - (upper_case_ascii_offset if c.isupper() else lower_case_ascii_offset)


def get_common_char(data: str) -> str:
    length = len(data)
    middle = int(length / 2)

    unique_chars_in_first_half = set(data[:middle])

    for i in range(middle, length):
        if unique_chars_in_first_half.__contains__(data[i]):
            return data[i]


score = 0

for line in lines:
    score += get_priority(get(line))

print(score)
