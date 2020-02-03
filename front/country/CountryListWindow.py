from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class CountryListWindow(QtWidgets.QMainWindow):
    def __init__(self, domain):
        self._domain = domain.country

        super(CountryListWindow, self).__init__()
        self.ui = loadUi('front/country/CountryList.ui', self)

        self.ui.table_list.setRowCount(0)
        self.ui.table_list.setColumnCount(1)

        self.ui.table_list.setHorizontalHeaderLabels(["Название"])
        self.ui.table_list.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)

    def refresh_list(self):
        countries = self._domain.get_all_countries()

        for country in countries:

            rows = self.ui.table_list.rowCount()
            self.ui.table_list.insertRow(rows)

            self.ui.table_list.setItem(rows, 0, QtWidgets.QTableWidgetItem(country['name']))
