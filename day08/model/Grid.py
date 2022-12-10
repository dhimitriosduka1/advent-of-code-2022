from functools import reduce

from day08.model.Tree import Tree


def is_edge_cell(tree, row_length, column_length):
    return tree.x == 0 or tree.x == row_length - 1 or tree.y == 0 or tree.y == column_length - 1


class Grid:
    def __init__(self, data):
        self.grid = None
        self.row_length = 0
        self.column_length = 0
        self.generate_grid(data)
        self.visible_trees = 0
        self.max_scenic_score = 0

    def generate_grid(self, data):
        self.grid = [
            [
                Tree(x=j, y=i, height=height)
                for i, height in enumerate(line)
            ]
            for j, line in enumerate(data)
        ]
        self.row_length = len(self.grid[0])
        self.column_length = len(self.grid)

    def evaluate_visibility(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                tree = self.grid[i][j]
                self._set_visibility(tree)
                if tree.visible:
                    self.visible_trees += 1

    def evaluate_scenic_scores(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                scenic_score = self._evaluate_scenic_score(self.grid[i][j])
                self.grid[i][j].scenic_score = scenic_score
                if scenic_score > self.max_scenic_score:
                    self.max_scenic_score = scenic_score

    def _set_visibility(self, tree):
        left_visible = True
        right_visible = True
        top_visible = True
        bottom_visible = True

        if is_edge_cell(tree, self.row_length, self.column_length):
            tree.visible = True
            return

        # Left visibility
        for y in range(0, tree.y):
            if self.grid[tree.x][y].height >= tree.height:
                left_visible = False
                break

        # Right visibility
        for y in range(tree.y + 1, self.row_length):
            if self.grid[tree.x][y].height >= tree.height:
                right_visible = False
                break

        # Top visibility
        for x in range(0, tree.x):
            if self.grid[x][tree.y].height >= tree.height:
                top_visible = False
                break

        # Bottom visibility
        for x in range(tree.x + 1, self.column_length):
            if self.grid[x][tree.y].height >= tree.height:
                bottom_visible = False
                break

        tree.visible = left_visible or right_visible or top_visible or bottom_visible

    def _evaluate_scenic_score(self, tree):

        if is_edge_cell(tree, self.row_length, self.column_length):
            return 0

        scenic_scores: [int] = [0, 0, 0, 0]

        # Left scenic score
        for y in range(tree.y - 1, -1, -1):
            current_tree_height = self.grid[tree.x][y].height
            if current_tree_height >= tree.height:
                scenic_scores[0] += 1
                break
            scenic_scores[0] += 1

        # Right scenic score
        for y in range(tree.y + 1, self.row_length):
            current_tree_height = self.grid[tree.x][y].height
            if current_tree_height >= tree.height:
                scenic_scores[1] += 1
                break
            scenic_scores[1] += 1

        # Top scenic score
        for x in range(tree.x - 1, -1, -1):
            current_tree_height = self.grid[x][tree.y].height
            if current_tree_height >= tree.height:
                scenic_scores[2] += 1
                break
            scenic_scores[2] += 1

        # Bottom scenic score
        for x in range(tree.x + 1, self.column_length):
            current_tree_height = self.grid[x][tree.y].height
            if current_tree_height >= tree.height:
                scenic_scores[3] += 1
                break
            scenic_scores[3] += 1

        return reduce((lambda a, b: a * b), scenic_scores)
