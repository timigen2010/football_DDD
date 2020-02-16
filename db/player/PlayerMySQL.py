from pymysql import escape_string


class PlayerMySQL:

    def __init__(self, db):
        self.db = db

    def add(self, data):

        if 'club_id' not in data\
                or 'fio' not in data\
                or 'position_id' not in data\
                or 'nationality_id' not in data\
                or 'dob' not in data \
                or 'height' not in data \
                or 'weight' not in data \
                or 'year' not in data \
                or 'contract' not in data:
            return False

        params = ["club_id='{:d}'".format(int(data['club_id'])),
                  "fio='{:s}'".format(escape_string(data['fio'])),
                  "position_id='{:d}'".format(int(data['position_id'])),
                  "nationality_id='{:d}'".format(int(data['nationality_id'])),
                  "dob='{:s}'".format(escape_string(str(data['dob']))),
                  "height='{:d}'".format(int(data['height'])),
                  "weight='{:d}'".format(int(data['weight'])),
                  "year='{:d}'".format(int(data['year'])),
                  "contract='{:d}'".format(int(data['contract']))]
        if 'photo' in data:
            params.append("photo='{:s}'".format(escape_string(data['photo'])))

        query = "INSERT INTO player SET " + ", ".join(params)

        return self.db.execute(query)

    def edit(self, id, data):

        params = []
        if 'club_id' in data:
            params.append("club_id='{:d}'".format(int(data['club_id'])))
        if 'fio' in data:
            params.append("fio='{:s}'".format(escape_string(data['fio'])))
        if 'position_id' in data:
            params.append("position_id='{:d}'".format(int(data['position_id'])))
        if 'nationality_id' in data:
            params.append("nationality_id='{:d}'".format(int(data['nationality_id'])))
        if 'dob' in data:
            params.append("dob='{:s}'".format(escape_string(str(data['dob']))))
        if 'height' in data:
            params.append("height='{:d}'".format(int(data['height'])))
        if 'weight' in data:
            params.append("weight='{:d}'".format(int(data['weight'])))
        if 'year' in data:
            params.append("year='{:d}'".format(int(data['year'])))
        if 'contract' in data:
            params.append("contract='{:d}'".format(int(data['contract'])))
        if 'photo' in data:
            params.append("photo='{:s}'".format(escape_string(data['photo'])))

        where_case = "player_id='{:d}'".format(id)

        query = "UPDATE player SET " + ", ".join(params) + " WHERE " + where_case

        return self.db.execute(query)

    def delete(self, id):

        where_case = "player_id='{:d}'".format(id)

        query = "DELETE FROM player WHERE " + where_case

        return self.db.execute(query)

    def get_all_players(self):

        query = "SELECT player_id, club_id, fio, position_id, nationality_id, dob, height, weight, year, contract, photo FROM player ORDER BY fio"

        return self.db.execute(query)

    def get_player(self, id):

        where_case = "player_id='{:d}'".format(id)

        query = "SELECT player_id, club_id, fio, position_id, nationality_id, dob, height, weight, year, contract, photo FROM player WHERE " + where_case

        return self.db.execute(query)

    def get_old_players(self, club_id):

        where_case = "club_id='{:d}'".format(int(club_id))
        where_case += " AND (CURRENT_DATE-dob) >= 30 * 365"
        order_clause = " ORDER BY fio"
        query = "SELECT fio FROM player WHERE " + where_case + order_clause

        return self.db.execute(query)

    def get_players_by_club(self, club_id):

        where_case = " WHERE pl.club_id='{:d}'".format(int(club_id))
        order_clause = " ORDER BY p.name, pl.fio"
        query = "SELECT pl.fio, p.name as position, cn.name as nationality, pl.dob, pl.height, pl.weight, pl.year, pl.contract, pl.photo FROM player as pl"
        query += "  INNER JOIN position AS p ON (pl.position_id = p.position_id)"
        query += "  INNER JOIN country AS cn ON (pl.nationality_id = cn.country_id)"
        query += where_case + order_clause

        return self.db.execute(query)

    def get_players_contract_above_avg(self):

        where_case = " WHERE pl.contract > (SELECT AVG(contract) FROM player)"
        order_clause = " ORDER BY p.name, pl.fio"
        query = "SELECT pl.fio, p.name as position, cn.name as nationality, pl.dob, pl.height, pl.weight, pl.year, pl.contract, pl.photo FROM player as pl"
        query += "  INNER JOIN position AS p ON (pl.position_id = p.position_id)"
        query += "  INNER JOIN country AS cn ON (pl.nationality_id = cn.country_id)"
        query += where_case + order_clause

        return self.db.execute(query)
