from pymysql import escape_string


class ClubMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'name' not in data\
                or 'city_id' not in data\
                or 'year' not in data\
                or 'liga_id' not in data\
                or 'president' not in data\
                or 'phone' not in data:
            return False

        params = ["name='{:s}'".format(escape_string(data['name'])),
                  "city_id='{:d}'".format(int(data['city_id'])),
                  "year='{:d}'".format(int(data['year'])),
                  "liga_id='{:d}'".format(int(data['liga_id'])),
                  "president='{:s}'".format(escape_string(data['president'])),
                  "phone='{:s}'".format(escape_string(data['phone']))]
        if 'logo' in data:
            params.append("logo='{:s}'".format(escape_string(data['logo'])))

        query = "INSERT INTO club SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        params = []
        if 'name' in data:
            params.append("name='{:s}'".format(escape_string(data['name'])))
        if 'city_id' in data:
            params.append("city_id='{:d}'".format(int(data['city_id'])))
        if 'year' in data:
            params.append("year='{:d}'".format(int(data['year'])))
        if 'liga_id' in data:
            params.append("liga_id='{:d}'".format(int(data['liga_id'])))
        if 'president' in data:
            params.append("president='{:s}'".format(escape_string(data['president'])))
        if 'phone' in data:
            params.append("phone='{:s}'".format(escape_string(data['phone'])))
        if 'logo' in data:
            params.append("logo='{:s}'".format(escape_string(data['logo'])))

        where_case = "club_id='{:d}'".format(id)

        query = "UPDATE club SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "club_id='{:d}'".format(id)

        query = "DELETE FROM club WHERE " + where_case

        return self.db.execute(query)

    def get_all_clubs(self):

        query = "SELECT club_id, name, city_id, year, liga_id, president, phone, logo FROM club ORDER BY name"

        return self.db.execute(query)

    def get_club(self, id):

        where_case = "club_id='{:d}'".format(id)

        query = "SELECT club_id, name, city_id, year, liga_id, president, phone, logo FROM club WHERE " + where_case

        return self.db.execute(query)

    def get_clubs_by_city(self, city_id):

        where_case = " WHERE cl.city_id='{:d}'".format(int(city_id))
        order_case = " ORDER BY cl.name"

        query = "SELECT cl.name as club, c.name as city, cl.year, l.name, cl.president, cl.phone, cl.logo FROM club AS cl"
        query += " INNER JOIN city AS c ON (cl.city_id = c.city_id)"
        query += " INNER JOIN liga AS l ON (cl.liga_id = l.liga_id)"
        query += where_case + order_case

        return self.db.execute(query)

    def get_all_clubs_data(self):

        order_case = " ORDER BY l.name, c.name, cl.name"

        query = "SELECT cl.name, c.name as city, cl.year, l.name as liga, cl.president, cl.phone, cl.logo FROM club AS cl"
        query += " INNER JOIN city AS c ON (cl.city_id = c.city_id)"
        query += " INNER JOIN liga AS l ON (cl.liga_id = l.liga_id)"
        query += order_case

        return self.db.execute(query)

    def get_avg_goals(self):

        group_case = " GROUP BY cl.name"
        order_case = " ORDER BY cl.name"

        query = "SELECT cl.name, AVG(g.home_score - g.guest_score) as avg_goals FROM club AS cl"
        query += " INNER JOIN game AS g ON (g.club_id = cl.club_id)"

        query += group_case + order_case

        return self.db.execute(query)