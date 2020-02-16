from db.player.PlayerMySQL import PlayerMySQL as Player


class IPlayer:

    def __init__(self, db):
        self._db = Player(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_player(self, id):
        return self._db.get_player(id)

    def get_all_players(self):
        return self._db.get_all_players()

    def get_old_players(self, club_id):
        return self._db.get_old_players(club_id)

    def get_players_by_club(self, club_id):
        return self._db.get_players_by_club(club_id)

    def get_players_contract_above_avg(self):
        return self._db.get_players_contract_above_avg()