from PyQt5.QtWidgets import QMainWindow

from Game import Game
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self, ui, game=None, size_grid=15):
        super(Window, self).__init__()
        self.ui = ui()
        self.ui.setupUi(self)
        self.brush = QBrush()
        self.game = game
        self.size_grid = size_grid
        self.ui.actionUndo.triggered.connect(game.undo)
        self.ui.actionRedo.triggered.connect(game.redo)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.NoPen)
        self.clear(qp, QColor(139, 69, 19))
        try:
            self.draw_state(qp)
        except Exception as e:
            print(e)
        qp.end()

    def clear(self, qp, fill):
        size = self.size()
        qp.setBrush(fill)
        qp.drawRect(0, 0, size.width(), size.height())

    def draw_state(self, qp):
        size = self.size()
        center = ((size.width() - self.size_grid) // 2, (size.height() - self.size_grid) // 2)
        if self.game.state:
            colors = {' ': QColor(139, 69, 19), '#': Qt.black,
                      '*': Qt.red, '.': Qt.gray, '@': Qt.yellow,
                      '$': Qt.blue}
            start = (center[0] - self.game.height * self.size_grid // 2,
                     center[1] - self.game.width * self.size_grid // 2)
            for cell in self.game:
                self.draw_block(qp, (start[0] + cell.x * self.size_grid,
                                     start[1] + cell.y * self.size_grid),
                                colors.get(cell.val))
            # for row in enumerate(self.game.state):
            #     for point in enumerate(row[1]):
            #         self.draw_block(qp, (start[0] + point[0] * self.size_grid,
            #                              start[1] + row[0] * self.size_grid),
            #                         self.size_grid, colors[point[1]])

    def update_map(self, state):
        self.game = Game(state)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
            self.game.move(x=-1)
        elif e.key() == Qt.Key_S:
            self.game.move(y=1)
        elif e.key() == Qt.Key_D:
            self.game.move(x=1)
        elif e.key() == Qt.Key_W:
            self.game.move(y=-1)
        self.update()

    def draw_block(self, qp, coord, fill=None):
        """
        :param qp: QPainter
        :param coord: (int, int)
        :param fill: {isPic: bool [, style: qt_style] [, pic: string]}, optional
        """
        if fill:
            qp.setBrush(fill)
        qp.drawRect(coord[0], coord[1], self.size_grid, self.size_grid)
