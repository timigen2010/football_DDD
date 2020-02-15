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