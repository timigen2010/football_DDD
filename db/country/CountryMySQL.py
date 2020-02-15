from pymysql import escape_string


class CountryMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]
        if 'flag' in data:
            params.append("flag='{:s}'".format(escape_string(data['flag'])))

        query = "INSERT INTO country SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]
        if 'flag' in data:
            params.append("flag='{:s}'".format(escape_string(data['flag'])))

        where_case = "country_id='{:d}'".format(id)

        query = "UPDATE country SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "country_id='{:d}'".format(id)

        query = "DELETE FROM country WHERE " + where_case

        return self.db.execute(query)

    def get_all_countries(self):

        query = "SELECT country_id, name FROM country ORDER BY name"

        return self.db.execute(query)