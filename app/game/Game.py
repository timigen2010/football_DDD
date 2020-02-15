class Game:

    def __init__(self, dal):
        self._dal = dal

    def add(self, data):
        return self._dal.game.add(data)

    def edit(self, id, data):
        return self._dal.game.edit(id, data)

    def delete(self, id):
        return self._dal.game.delete(id)
    
    def get_game(self, id):
        return self._dal.game.get_game(id)

    def get_all_games(self):
        return self._dal.game.get_all_games()
