from db.DAL import DAL
from app.country.ICountry import ICountry


class Domain:
    def __init__(self):
        self._dal = DAL()
        self.country = ICountry(self._dal)
