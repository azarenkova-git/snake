class Coordinates:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: "Coordinates") -> bool:
        return self.x == other.x and self.y == other.y

    def copy(self) -> "Coordinates":
        """Возвращает копию координат"""

        return Coordinates(self.x, self.y)

    def to_tuple(self) -> tuple:
        """Возвращает координаты в виде кортежа"""

        return self.x, self.y
