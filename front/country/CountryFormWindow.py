from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

import front.country.CountryListWindow as CountryListWindow


class CountryFormWindow(QtWidgets.QWidget):
    def __init__(self, domain, data):
        self._domain = domain.country

        super(CountryFormWindow, self).__init__()
        self.ui = loadUi('front/country/CountryForm.ui', self)

        if data.is_edit:
            self.ui.h1_label.setText("Добавление страны")
            self.ui.save_btn.clicked.connect(self.add)
        else:
            self.ui.h1_label.setText("Редактирование страны")
            self.ui.save_btn.clicked.connect(self.add)

        self.ui.back_btn.setText("Назад")
        self.ui.save_btn.setText("Сохранить")

    def add(self):
        data = {
            'name': self.ui.name.text()
        }
        result = self._domain.add(data)
        if result:
            CountryListWindow.CountryListWindow(self._domain)
            self.close()
