from day11.model.Opertation import Operation
from day11.model.Test import Test


class Monkey:
    def __init__(self, starting_items: [int], operation: Operation, test: Test):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.number_of_inspected_items = 0
