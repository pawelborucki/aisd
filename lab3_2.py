class Triangle:
    side: int
    height: int

    def __init__(self, side, height) -> None:
        self.side = side
        self.height = height

    def area(self) -> float:
        return (self.side * self.height) / 2

    def perimeter(self) -> int:
        return 3 * self.side


t1 = Triangle(5,7)
print(t1.area())
print(t1.perimeter())