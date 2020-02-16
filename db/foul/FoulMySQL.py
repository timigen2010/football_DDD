from pymysql import escape_string


class FoulMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]

        query = "INSERT INTO foul SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]

        where_case = "foul_id='{:d}'".format(id)

        query = "UPDATE foul SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "foul_id='{:d}'".format(id)

        query = "DELETE FROM foul WHERE " + where_case

        return self.db.execute(query)

    def get_all_fouls(self):

        query = "SELECT foul_id, name FROM foul ORDER BY name"

        return self.db.execute(query)

    def get_foul(self, id):

        where_case = "foul_id='{:d}'".format(id)

        query = "SELECT foul_id, name FROM foul WHERE " + where_case

        return self.db.execute(query)

    def get_foul(self, id):

        where_case = "foul_id='{:d}'".format(id)

        query = "SELECT foul_id, name FROM foul WHERE " + where_case

        return self.db.execute(query)

    def get_last_month_foul(self):

        group_case = " GROUP BY cl.name, ct.name, g.date"
        having_case = " HAVING CURRENT_DATE - g.date <= 30"

        query = "SELECT cl.name as club, ct.name as contestant, g.date, COUNT(pt.game_id) FROM game AS g"
        query += " LEFT JOIN club AS cl ON (g.club_id = cl.club_id)"
        query += " LEFT JOIN contestant AS ct ON (g.contestant_id = ct.contestant_id)"
        query += " INNER JOIN participation AS pt ON (pt.game_id = g.game_id)"

        query += group_case + having_case

        return self.db.execute(query)

    def get_win_last_month_foul(self):

        where_case = " WHERE g.home_score > g.guest_score"
        group_case = " GROUP BY cl.name, ct.name, g.date"
        having_case = " HAVING CURRENT_DATE - g.date <= 30"

        query = "SELECT cl.name as club, ct.name as contestant, g.date, COUNT(pt.game_id) FROM game AS g"
        query += " LEFT JOIN club AS cl ON (g.club_id = cl.club_id)"
        query += " LEFT JOIN contestant AS ct ON (g.contestant_id = ct.contestant_id)"
        query += " INNER JOIN participation AS pt ON (pt.game_id = g.game_id)"

        query += where_case + group_case + having_case

        return self.db.execute(query)