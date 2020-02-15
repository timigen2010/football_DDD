from pymysql import escape_string


class CityMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]

        query = "INSERT INTO city SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        if 'name' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name']))]

        where_case = "city_id='{:d}'".format(id)

        query = "UPDATE city SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "city_id='{:d}'".format(id)

        query = "DELETE FROM city WHERE " + where_case

        return self.db.execute(query)

    def get_all_cities(self):

        query = "SELECT city_id, name FROM city ORDER BY name"

        return self.db.execute(query)

    def get_city(self, id):

        where_case = "city_id='{:d}'".format(id)

        query = "SELECT city_id, name FROM city WHERE " + where_case

        return self.db.execute(query)