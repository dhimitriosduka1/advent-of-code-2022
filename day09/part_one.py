from day09.model.Instruction import Instruction
from day09.model.Head import Head
from day09.model.Tail import Tail

file = open("./input/input.txt")
lines = map(lambda x: x.removesuffix("\n"), file.readlines())

head = Head(0, 0)
tail = Tail(0, 0)

for line in lines:
    direction, amount = line.split(" ")
    instruction = Instruction(direction, int(amount))
    instruction.execute(head, tail)

print(len(tail.position_visited))
