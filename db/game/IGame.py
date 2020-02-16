from db.game.GameMySQL import GameMySQL as Game


class IGame:

    def __init__(self, db):
        self._db = Game(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_game(self, id):
        return self._db.get_game(id)

    def get_all_games(self):
        return self._db.get_all_games()

    def get_all_games_data(self):
        return self._db.get_all_games_data()

    def get_club_games_by_period(self, club_id, period_date_start, period_date_end):
        return self._db.get_club_games_by_period(club_id, period_date_start, period_date_end)