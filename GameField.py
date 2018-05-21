from Drawing import Drawing
from Checker import Checker


class GameField:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.checkers_count = 20
        self.back_field = Drawing(self.width, self.height, 30)

        self.checkers_field = []
        self.fill_checkers_field()
        print(self.checkers_field[0].x + self.checkers_field[0].y)
        self.back_field.draw_checkers(self.checkers_field)
        self.back_field.main()

    def fill_checkers_field(self):
        white_checkers = self.checkers_count
        black_checkers = self.checkers_count
        for x in range(self.width):
            for y in range(self.height):
                if black_checkers == 0:
                    break
                if not (x + y) % 2 == 0:
                    self.checkers_field.append(Checker(y, x, "blue"))
                    black_checkers -= 1

        for x in range(self.width-1, -1, -1):
            for y in range(self.height-1, -1, -1):
                if white_checkers == 0:
                    break
                if not (x + y) % 2 == 0:
                    self.checkers_field.append(Checker(y, x, "green"))
                    white_checkers -= 1

