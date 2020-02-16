from pymysql import escape_string


class ContestantMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'name' not in data\
                or 'country_id' not in data\
                or 'coach' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name'])),
                  "country_id='{:d}'".format(int(data['country_id'])),
                  "coach='{:s}'".format(escape_string(data['coach']))]
        if 'logo' in data:
            params.append("logo='{:s}'".format(escape_string(data['logo'])))

        query = "INSERT INTO contestant SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        params = []
        if 'name' in data:
            params.append("name='{:s}'".format(escape_string(data['name'])))
        if 'country_id' in data:
            params.append("country_id='{:d}'".format(int(data['country_id'])))
        if 'coach' in data:
            params.append("coach='{:s}'".format(escape_string(data['coach'])))
        if 'logo' in data:
            params.append("logo='{:s}'".format(escape_string(data['logo'])))

        where_case = "contestant_id='{:d}'".format(id)

        query = "UPDATE contestant SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "contestant_id='{:d}'".format(id)

        query = "DELETE FROM contestant WHERE " + where_case

        return self.db.execute(query)

    def get_all_contestants(self):

        query = "SELECT contestant_id, name, country_id, coach, logo FROM contestant ORDER BY name"

        return self.db.execute(query)

    def get_played_contestants(self):

        order_case = " ORDER BY cn.name, ct.name"

        query = "SELECT ct.name, cn.name, ct.coach, ct.logo FROM contestant as ct"
        query += " LEFT JOIN country AS cn ON (ct.country_id = cn.country_id)"
        query += " INNER JOIN game AS g ON (g.contestant_id = ct.contestant_id)"

        query += order_case

        return self.db.execute(query)

    def get_contestant(self, id):

        where_case = "contestant_id='{:d}'".format(id)

        query = "SELECT contestant_id, name, country_id, coach, logo FROM contestant WHERE " + where_case

        return self.db.execute(query)