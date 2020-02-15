from db.DAL import DAL
from app.country.ICountry import ICountry
from app.city.ICity import ICity
from app.liga.ILiga import ILiga
from app.club.IClub import IClub
from app.contestant.IContestant import IContestant
from app.foul.IFoul import IFoul
from app.game.IGame import IGame
from app.position.IPosition import IPosition
from app.player.IPlayer import IPlayer
from app.participation.IParticipation import IParticipation


class Domain:
    def __init__(self):
        self._dal = DAL()
        self.country = ICountry(self._dal)
        self.city = ICity(self._dal)
        self.liga = ILiga(self._dal)
        self.club = IClub(self._dal)
        self.contestant = IContestant(self._dal)
        self.foul = IFoul(self._dal)
        self.game = IGame(self._dal)
        self.position = IPosition(self._dal)
        self.player = IPlayer(self._dal)
        self.participation = IParticipation(self._dal)
