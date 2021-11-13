class Tree:
    name: str
    height: float
    leafs: int

    def __init__(self, name, height, leafs):
        self.name = name
        self.height = height
        self.leafs = leafs

    def grow_up(self, add_height: float) -> None:
        self.height += add_height

    def grow_wide(self, add_leafs) -> None:
        self.leafs += add_leafs

    def show(self) -> str:
        return f'Imie: {self.name}, wysokosc: {self.height}, liczba lisci: {self.leafs}'


t1 = Tree('D1', 100, 2000)
t1.grow_wide(80)
print(t1.show())

t2 = Tree('D2', 80.5, 1888)
t3 = Tree('D3', 73.8, 3213)
t4 = Tree('D4', 12.2, 1122)
t5 = Tree('D5', 44.3, 9000)
print(t2.show())
print(t3.show())
print(t4.show())
print(t5.show())
