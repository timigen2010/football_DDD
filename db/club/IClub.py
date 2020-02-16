from db.club.ClubMySQL import ClubMySQL as Club


class IClub:

    def __init__(self, db):
        self._db = Club(db)

    def add(self, data):
        return self._db.add(data)

    def edit(self, id, data):
        return self._db.edit(id, data)

    def delete(self, id):
        return self._db.delete(id)

    def get_club(self, id):
        return self._db.get_club(id)

    def get_all_clubs(self):
        return self._db.get_all_clubs()

    def get_all_clubs_data(self):
        return self._db.get_all_clubs_data()

    def get_clubs_by_city(self, club_id):
        return self._db.get_clubs_by_city(club_id)

    def get_avg_goals(self):
        return self._db.get_avg_goals()

    def get_avg_win_goals(self):
        return self._db.get_avg_win_goals()