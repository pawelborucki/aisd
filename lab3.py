class House:
    windows_count: int
    area: float

    def __init__(self, windows_count: int, area: float) -> None:
        self.windows_count = windows_count
        self.area = area

    def change_area(self, area_to_add: float) -> None:
        self.area += area_to_add

    def __str__(self) -> str:
        return f'liczba okien: {self.windows_count}, powierzchnia: {self.area}'


h1 = House(15, 120.5)
h2 = House(10, 90)

print(h1.windows_count)
print(h1.area)


h1.change_area(10.5)
print(h1.area)
print(h1)
print(h2)

