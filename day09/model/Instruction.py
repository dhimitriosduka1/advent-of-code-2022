from day09.model import Head
from day09.model.Point import Point
from day09.model.Tail import Tail


class Instruction:
    def __init__(self, direction: str, amount: int):
        self.direction = direction
        self.amount = amount

    def execute(self, nodes: [Point]):
        head: Head = nodes[0]

        for _ in range(self.amount):
            head.move(self.direction)

            for i in range(1, len(nodes)):
                prev_node = nodes[i - 1]
                current_node = nodes[i]

                x_difference = abs(prev_node.x - current_node.x)
                y_difference = abs(prev_node.y - current_node.y)

                if x_difference == 2 or y_difference == 2:
                    if prev_node.x != current_node.x and prev_node.y != current_node.y:
                        if prev_node.x > current_node.x:
                            current_node.move("RU" if prev_node.y > current_node.y else "RD")
                        else:
                            current_node.move("LU" if prev_node.y > current_node.y else "LD")
                    else:
                        if x_difference:
                            current_node.move("R" if prev_node.x > current_node.x else "L")
                        else:
                            current_node.move("U" if prev_node.y > current_node.y else "D")
