from db.IDb import IDb
from db.country.ICountry import ICountry
from db.city.ICity import ICity
from db.liga.ILiga import ILiga
from db.club.IClub import IClub
from db.contestant.IContestant import IContestant
from db.foul.IFoul import IFoul


class DAL:
    def __init__(self):
        self._db = IDb()
        self.country = ICountry(self._db)
        self.city = ICity(self._db)
        self.liga = ILiga(self._db)
        self.club = IClub(self._db)
        self.contestant = IContestant(self._db)
        self.foul = IFoul(self._db)
