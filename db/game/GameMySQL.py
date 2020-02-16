from pymysql import escape_string
import datetime

class GameMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'club_id' not in data\
                or 'contestant_id' not in data\
                or 'date' not in data\
                or 'home_score' not in data\
                or 'guest_score' not in data:
            return False

        params = ["club_id='{:d}'".format(int(data['club_id'])),
                  "contestant_id='{:d}'".format(int(data['contestant_id'])),
                  "date='{:s}'".format(escape_string(str(data['date']))),
                  "home_score='{:d}'".format(int(data['home_score'])),
                  "guest_score='{:d}'".format(int(data['guest_score']))]

        query = "INSERT INTO game SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        params = []
        if 'club_id' in data:
            params.append("club_id='{:d}'".format(int(data['club_id'])))
        if 'contestant_id' in data:
            params.append("contestant_id='{:d}'".format(int(data['contestant_id'])))
        if 'date' in data:
            params.append("date='{:s}'".format(str(data['date'])))
        if 'home_score' in data:
            params.append("home_score='{:d}'".format(int(data['home_score'])))
        if 'guest_score' in data:
            params.append("guest_score='{:d}'".format(int(data['guest_score'])))

        where_case = "game_id='{:d}'".format(id)

        query = "UPDATE game SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "game_id='{:d}'".format(id)

        query = "DELETE FROM game WHERE " + where_case

        return self.db.execute(query)

    def get_all_games(self):

        query = "SELECT game_id, club_id, contestant_id, date, home_score, guest_score FROM game"

        return self.db.execute(query)

    def get_game(self, id):

        where_case = "game_id='{:d}'".format(id)

        query = "SELECT game_id, club_id, contestant_id, date, home_score, guest_score FROM game WHERE " + where_case

        return self.db.execute(query)

    def get_club_games_by_period(self, club_id, period_date_start, period_date_end):

        where_case = " WHERE g.club_id='{:d}'".format(int(club_id))
        where_case += " AND g.date BETWEEN '{:s}' AND '{:s}'".format(escape_string(str(period_date_start)), escape_string(str(period_date_end)))

        group_case = " GROUP BY cl.name, ct.name, g.date, g.home_score, g.guest_score"
        order_case = " ORDER BY cl.name, ct.name, g.date"

        query = "SELECT cl.name, ct.name, g.date, g.home_score, g.guest_score FROM game AS g"
        query += " INNER JOIN club AS cl ON (g.club_id = cl.club_id)"
        query += " INNER JOIN contestant AS ct ON (g.contestant_id = ct.contestant_id)"
        query += where_case + group_case + order_case

        return self.db.execute(query)