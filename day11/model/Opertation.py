class Operation:
    def __init__(self, operation: str, value: str):
        self.operation = operation.strip()
        self.value = value.strip()

    def apply(self, item_value):
        other_value = None
        if self.value == "old":
            other_value = float(item_value)
        else:
            other_value = float(self.value)

        if self.operation == "+":
            return item_value + other_value
        elif self.operation == "-":
            return item_value - other_value
        elif self.operation == "*":
            return item_value * other_value
        elif self.operation == "/":
            return item_value / other_value
