class City:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.city.add(data)

    def edit(self, id, data):
        return self._dal.city.edit(id, data)

    def delete(self, id):
        return self._dal.city.delete(id)
    
    def get_city(self, id):
        return self._dal.city.get_city(id)

    def get_all_cities(self):
        return self._dal.city.get_all_cities()
