import sys
from PyQt5 import QtWidgets
from front.Front import Front

if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    front = Front()
    front.country_list_window.show()
    front.country_list_window.refresh_list()

    sys.exit(app.exec())