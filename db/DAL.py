from db.IDb import IDb
from db.country.ICountry import ICountry


class DAL:
    def __init__(self):
        self._db = IDb()
        self.country = ICountry(self._db)
