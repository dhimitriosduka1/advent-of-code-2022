from day09.model.Point import Point


class Tail(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.position_visited = set()

        # Setting initial position as visited
        self.position_visited.add((0, 0))
