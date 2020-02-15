class Position:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.position.add(data)

    def edit(self, id, data):
        return self._dal.position.edit(id, data)

    def delete(self, id):
        return self._dal.position.delete(id)
    
    def get_position(self, id):
        return self._dal.position.get_position(id)

    def get_all_positions(self):
        return self._dal.position.get_all_positions()
