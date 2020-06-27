from PyQt5.QtWidgets import QApplication
import sys

from Game import Game
from Window import Window
from window_design import Ui_MainWindow


def settings(window):
    pass


def draw_state():
    pass


if __name__ == '__main__':

    _map = '''
   ####
####  ##
#   $  #
#  *** #
#  . . ##
## * *  #
 ##***  #
  # $ ###
  # @ #
  #####
'''
    state = [list(i) for i in _map.split('\n')[1:-1]]

    app = QApplication([])

    win = Window(Ui_MainWindow, Game(state))
    win.show()
    sys.exit(app.exec())
