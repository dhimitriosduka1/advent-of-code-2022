from day09.model.Instruction import Instruction
from day09.model.Head import Head
from day09.model.Point import Point
from day09.model.Tail import Tail

file = open("./input/input.txt")
lines = map(lambda x: x.removesuffix("\n"), file.readlines())

nodes = []
head = Head(0, 0)
nodes.append(head)

nodes.extend([Point(0, 0) for _ in range(8)])

tail = Tail(0, 0)
nodes.append(tail)

for line in lines:
    direction, amount = line.split(" ")
    instruction = Instruction(direction, int(amount))
    instruction.execute(nodes)

print(len(tail.position_visited))
