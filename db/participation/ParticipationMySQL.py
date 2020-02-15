from pymysql import escape_string


class ParticipationMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'player_id' not in data\
                or 'game_id' not in data \
                or 'prize' not in data \
                or 'foul_id' not in data:
            return False

        params = ["player_id='{:d}'".format(int(data['player_id'])),
                  "game_id='{:d}'".format(int(data['game_id'])),
                  "prize='{:d}'".format(int(data['prize'])),
                  "foul_id='{:d}'".format(int(data['foul_id']))]

        query = "INSERT INTO participation SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        params = []
        if 'player_id' in data:
            params.append("player_id='{:d}'".format(int(data['player_id'])))
        if 'game_id' in data:
            params.append("game_id='{:d}'".format(int(data['game_id'])))
        if 'prize' in data:
            params.append("prize='{:d}'".format(int(data['prize'])))
        if 'foul_id' in data:
            params.append("foul_id='{:d}'".format(int(data['foul_id'])))

        where_case = "participation_id='{:d}'".format(id)

        query = "UPDATE participation SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "participation_id='{:d}'".format(id)

        query = "DELETE FROM participation WHERE " + where_case

        return self.db.execute(query)

    def get_all_participations(self):

        query = "SELECT participation_id, player_id, game_id, prize, foul_id FROM participation"

        return self.db.execute(query)

    def get_participation(self, id):

        where_case = "participation_id='{:d}'".format(id)

        query = "SELECT participation_id, player_id, game_id, prize, foul_id FROM participation WHERE " + where_case

        return self.db.execute(query)