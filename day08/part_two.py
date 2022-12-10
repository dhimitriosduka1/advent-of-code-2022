from day08.model.Grid import Grid

file = open("./input/input.txt")
lines = map(lambda x: x.removesuffix("\n"), file.readlines())

grid = Grid(lines)
grid.evaluate_scenic_scores()
print(grid.max_scenic_score)
