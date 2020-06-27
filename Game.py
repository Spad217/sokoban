def swap(array2d, first_y, first_x, second_y, second_x):
    array2d[first_y][first_x], array2d[second_y][second_x] = \
        array2d[second_y][second_x], array2d[first_y][first_x]


class Cell:
    def __init__(self, y, x, val):
        self.y = y
        self.x = x
        self.val = val


class Log:
    def __init__(self):
        pass


class Game:
    def __init__(self, state):
        self.logs = []
        self.pos_log = -1
        self.height = len(state)
        max_width = self.width = max(len(i) for i in state)
        self.state = [[*row] + [' '] * (max_width - len(row)) for row in state]  # make "state" rectangle

    def __iter__(self):
        for iy in enumerate(self.state):
            for ix in enumerate(iy[1]):
                yield Cell(iy[0], ix[0], ix[1])

    def move(self, x=0, y=0):
        for cell in self:
            if cell.val == '@':
                if self.state[cell.y + y][cell.x + x] in (' ', '.'):  # empty
                    swap(self.state, cell.y, cell.x, cell.y + y, cell.x + x)
                elif self.state[cell.y + y][cell.x + x] in ('*', '$') and \
                        self.state[cell.y + y * 2][cell.x + x * 2] in (' ', '.'):  # box
                    swap(self.state, cell.y + y * 2, cell.x + x * 2, cell.y + y, cell.x + x)
                    swap(self.state, cell.y, cell.x, cell.y + y, cell.x + x)
                else:
                    return False
                return True
        return False

    def undo(self):
        pass

    def redo(self):
        pass

    def is_win(self):
        pass
