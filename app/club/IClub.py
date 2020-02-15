from app.club.Club import Club as Club


class IClub:

    def __init__(self, dal):
        self._dal = Club(dal)

    def add(self, data):
        return self._dal.add(data)

    def edit(self, id, data):
        return self._dal.edit(id, data)

    def delete(self, id):
        return self._dal.delete(id)

    def get_club(self, id):
        return self._dal.get_club(id)

    def get_all_clubs(self):
        return self._dal.get_all_clubs()