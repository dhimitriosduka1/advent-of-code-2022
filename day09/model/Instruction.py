from day09.model import Head
from day09.model.Tail import Tail


class Instruction:
    def __init__(self, direction: str, amount: int):
        self.direction = direction
        self.amount = amount

    def execute(self, head: Head, tail: Tail):
        for _ in range(self.amount):
            head.move(self.direction)

            x_difference = abs(head.x - tail.x)
            y_difference = abs(head.y - tail.y)

            if x_difference == 2 or y_difference == 2:
                if head.x != tail.x and head.y != tail.y:
                    if head.x > tail.x:
                        tail.move("RU" if head.y > tail.y else "RD")
                    else:
                        tail.move("LU" if head.y > tail.y else "LD")
                else:
                    if x_difference:
                        tail.move("R" if head.x > tail.x else "L")
                    else:
                        tail.move("U" if head.y > tail.y else "D")
