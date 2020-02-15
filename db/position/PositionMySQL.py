from pymysql import escape_string


class PositionMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'name' not in data\
                and 'abbreviation' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name'])),
                  "abbreviation='{:s}'".format(escape_string(data['abbreviation']))]

        query = "INSERT INTO position SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        params = ["name='{:s}'".format(escape_string(data['name'])),
                  "abbreviation='{:s}'".format(escape_string(data['abbreviation']))]

        where_case = "position_id='{:d}'".format(id)

        query = "UPDATE position SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "position_id='{:d}'".format(id)

        query = "DELETE FROM position WHERE " + where_case

        return self.db.execute(query)

    def get_all_positions(self):

        query = "SELECT position_id, name, abbreviation FROM position ORDER BY name"

        return self.db.execute(query)

    def get_position(self, id):

        where_case = "position_id='{:d}'".format(id)

        query = "SELECT position_id, name, abbreviation FROM position WHERE " + where_case

        return self.db.execute(query)