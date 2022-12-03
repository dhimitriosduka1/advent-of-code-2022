file = open("./input/input.txt")
lines = file.readlines()


def get_priority(c: str) -> int:
    lower_case_ascii_offset = 96
    upper_case_ascii_offset = 38
    return ord(c) - (upper_case_ascii_offset if c.isupper() else lower_case_ascii_offset)


def get_common_char(data: list[str]) -> str:
    common_char = set(data[0])
    for i in range(1, len(data)):
        entry = set(data[i])
        common_char = entry.intersection(common_char)
    return common_char.pop()


score = 0

temp_list = []

for index, line in enumerate(lines):
    temp_list.append(line.removesuffix("\n"))
    if len(temp_list) == 3:
        score += get_priority(get_common_char(temp_list))
        temp_list = []

print(score)
