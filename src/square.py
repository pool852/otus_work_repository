from src.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError("side_a must be above zero")
        super().__init__(side_a, side_a)
