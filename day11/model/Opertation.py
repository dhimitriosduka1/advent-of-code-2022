import math


class Operation:
    def __init__(self, operation: str, value: str):
        self.operation = operation.strip()
        self.value = value.strip()

    def apply(self, item_value):
        other_value = None
        if self.value == "old":
            other_value = int(item_value)
        else:
            other_value = int(self.value)

        if self.operation == "+":
            return item_value + other_value
        elif self.operation == "-":
            return item_value - other_value
        elif self.operation == "*":
            return item_value * other_value
        elif self.operation == "/":
            return math.floor(item_value / other_value)
