class Square:
    side: int

    def __init__(self, side: int) -> None:
        self.side = side

    def area(self) -> int:
        return self.side * self.side
    def perimeter(self) -> int:
        return 4 * self.side

s1 = Square(5)
print(s1.area())
print(s1.perimeter())