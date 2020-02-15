from db.DAL import DAL
from app.country.ICountry import ICountry
from app.city.ICity import ICity
from app.liga.ILiga import ILiga
from app.club.IClub import IClub


class Domain:
    def __init__(self):
        self._dal = DAL()
        self.country = ICountry(self._dal)
        self.city = ICity(self._dal)
        self.liga = ILiga(self._dal)
        self.club = IClub(self._dal)
