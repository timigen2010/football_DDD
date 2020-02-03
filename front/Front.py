from app.Domain import Domain
from front.country.CountryListWindow import CountryListWindow


class Front:

    def __init__(self):
        self._domain = Domain()
        self.country_list_window = CountryListWindow(self._domain)