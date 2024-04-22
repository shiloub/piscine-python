class calculator:
    def __init__(self, V: list[float]):
        """Constructor of calculator class"""
        self.v = V

    def __add__(self, object) -> None:
        """Add the argument to each element in the vector"""
        self.v = [x + object for x in self.v]
        print(self.v)

    def __mul__(self, object) -> None:
        """mul the argument by each element in the vector"""
        self.v = [x * object for x in self.v]
        print(self.v)

    def __sub__(self, object) -> None:
        """Sub the argument to each element in the vector"""
        self.v = [x - object for x in self.v]
        print(self.v)

    def __truediv__(self, object) -> None:
        """Div all the elements of the vector by the argument given"""
        if object == 0:
            raise ZeroDivisionError
        self.v = [x // object for x in self.v]
        print(self.v)
