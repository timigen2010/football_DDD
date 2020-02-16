class Club:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.club.add(data)

    def edit(self, id, data):
        return self._dal.club.edit(id, data)

    def delete(self, id):
        return self._dal.club.delete(id)
    
    def get_club(self, id):
        return self._dal.club.get_club(id)

    def get_all_clubs(self):
        return self._dal.club.get_all_clubs()

    def get_all_clubs_data(self):
        return self._dal.club.get_all_clubs_data()

    def get_clubs_by_city(self, city_id):
        return self._dal.club.get_clubs_by_city(city_id)
