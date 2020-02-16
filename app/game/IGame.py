from app.game.Game import Game as Game


class IGame:

    def __init__(self, dal):
        self._dal = Game(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_game(self, id):
        return self._dal.get_game(id)

    def get_all_games(self):
        return self._dal.get_all_games()

    def get_club_games_by_period(self, club_id, period_date_start, period_date_end):
        return self._dal.get_club_games_by_period(club_id, period_date_start, period_date_end)