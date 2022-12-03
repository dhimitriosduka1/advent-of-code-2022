import heapq

heap = []

file = open("./input/input.txt")
lines = file.readlines()

current_calories_sum = 0


def heap_push():
    heapq.heappush(heap, current_calories_sum)


def update_current_calories_sum():
    global current_calories_sum
    current_calories_sum += int(line)


for index, line in enumerate(lines):
    line = line.removesuffix("\n")
    if len(line) == 0:
        heap_push()
        current_calories_sum = 0
    elif index == len(lines) - 1:
        update_current_calories_sum()
        heap_push()
    else:
        update_current_calories_sum()

print(sum(heapq.nlargest(3, heap)))
