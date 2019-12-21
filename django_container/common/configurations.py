from configurations.values import Value


class StringValue(Value):
    """
    Стандартный Value сыпется при запуске тестов.
        * TypeError: must be str, not Value
    """
    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def __hash__(self):
        return hash(self.value)

    def __len__(self):
        return len(self.value)
