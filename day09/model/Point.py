class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "RU":
            self.x += 1
            self.y += 1
        elif direction == "RD":
            self.x += 1
            self.y -= 1
        elif direction == "LU":
            self.x -= 1
            self.y += 1
        else:
            self.x -= 1
            self.y -= 1

        if self.__class__.__name__ == "Tail":
            self.position_visited.add((self.x, self.y))
