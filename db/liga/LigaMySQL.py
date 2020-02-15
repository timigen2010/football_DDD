from pymysql import escape_string


class LigaMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]

        query = "INSERT INTO liga SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]

        where_case = "liga_id='{:d}'".format(id)

        query = "UPDATE liga SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "liga_id='{:d}'".format(id)

        query = "DELETE FROM liga WHERE " + where_case

        return self.db.execute(query)

    def get_all_ligas(self):

        query = "SELECT liga_id, name FROM liga ORDER BY name"

        return self.db.execute(query)

    def get_liga(self, id):

        where_case = "liga_id='{:d}'".format(id)

        query = "SELECT liga_id, name FROM liga WHERE " + where_case

        return self.db.execute(query)