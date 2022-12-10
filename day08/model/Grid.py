from day08.model.Tree import Tree


def is_edge_cell(tree, row_length, column_length):
    return tree.x == 0 or tree.x == row_length - 1 or tree.y == 0 or tree.y == column_length - 1


class Grid:
    def __init__(self, data):
        self.grid = None
        self.generate_grid(data)
        self.visible_trees = 0

    def generate_grid(self, data):
        self.grid = [
            [
                Tree(x=j, y=i, height=height)
                for i, height in enumerate(line)
            ]
            for j, line in enumerate(data)
        ]

    def evaluate_visibility(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tree = self.grid[i][j]
                self._set_visibility(tree)
                if tree.visible:
                    self.visible_trees += 1

    def _set_visibility(self, tree):
        left_visible = True
        right_visible = True
        top_visible = True
        bottom_visible = True

        row_length = len(self.grid[0])
        column_length = len(self.grid)

        if is_edge_cell(tree, row_length, column_length):
            tree.visible = True
            return

        # Left visibility
        for y in range(0, tree.y):
            if self.grid[tree.x][y].height >= tree.height:
                left_visible = False
                break

        # Right visibility
        for y in range(tree.y + 1, row_length):
            if self.grid[tree.x][y].height >= tree.height:
                right_visible = False
                break

        # Top visibility
        for x in range(0, tree.x):
            if self.grid[x][tree.y].height >= tree.height:
                top_visible = False
                break

        # Bottom visibility
        for x in range(tree.x + 1, column_length):
            if self.grid[x][tree.y].height >= tree.height:
                bottom_visible = False
                break

        tree.visible = left_visible or right_visible or top_visible or bottom_visible
