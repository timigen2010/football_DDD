from db.DAL import DAL
from app.country.ICountry import ICountry
from app.city.ICity import ICity


class Domain:
    def __init__(self):
        self._dal = DAL()
        self.country = ICountry(self._dal)
        self.city = ICity(self._dal)
