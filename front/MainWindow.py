from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

from front.country.CountryListWindow import CountryListWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, domain):

        super(MainWindow, self).__init__()
        self.ui = loadUi('front/main.ui', self)

        self.ui.setCentralWidget(CountryListWindow(domain))
