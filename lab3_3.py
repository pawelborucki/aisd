class Square:
    side: int

    def __init__(self, side: int) -> None:
        self.side = side

    def area(self) -> int:
        return self.side * self.side

    def perimeter(self) -> int:
        return 4 * self.side


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


kw = [None] * 10
for x in range(0, 10):
    kw[x] = Square(x + 11)

for x in range(0, 10):
    print(kw[x].side)

tr = []

for i in range(6, 10):
    for j in range(15, 19):
        tr.append(Triangle(i, j))

for z in range(0,25):
    print(f'Pole: {tr[z].area()}')
    print(f'Obw: {tr[z].perimeter()}')