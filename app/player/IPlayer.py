from app.player.Player import Player as Player


class IPlayer:

    def __init__(self, dal):
        self._dal = Player(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_player(self, id):
        return self._dal.get_player(id)

    def get_all_players(self):
        return self._dal.get_all_players()

    def get_old_players(self, club_id):
        return self._dal.get_old_players(club_id)

    def get_players_by_club(self, club_id):
        return self._dal.get_players_by_club(club_id)