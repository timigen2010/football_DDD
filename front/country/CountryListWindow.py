from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

import front.country.CountryFormWindow as CountryFormWindow


class CountryListWindow(QtWidgets.QWidget):
    def __init__(self, domain):
        self._domain = domain.country

        super(CountryListWindow, self).__init__()
        self.ui = loadUi('front/country/CountryList.ui', self)

        self.ui.table_list.setRowCount(0)
        self.ui.table_list.setColumnCount(1)

        self.ui.table_list.setHorizontalHeaderLabels(["Название"])
        self.ui.table_list.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)

        self.ui.first_title.setText("Страны/национальности")

        self.ui.refresh_btn.clicked.connect(self.refresh_list)
        self.ui.add_btn.clicked.connect(self.add)

    def add(self):
        data = {
            'is_edit': False
        }
        # cfw = CountryFormWindow.CountryFormWindow(self._domain, data)
        self.ui.setLayout(CountryFormWindow.CountryFormWindow(self._domain, data))
        # self.setLayout()

    def refresh_list(self):
        countries = self._domain.get_all_countries()

        self.ui.table_list.setRowCount(0)

        for country in countries:

            rows = self.ui.table_list.rowCount()
            self.ui.table_list.insertRow(rows)

            item = QtWidgets.QTableWidgetItem(country['name'])
            item.setData(Qt.UserRole, country["country_id"])
            self.ui.table_list.setItem(rows, 0, item)
