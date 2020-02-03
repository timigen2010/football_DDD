class Country:

    def __init__(self, dal):
        self._dal = dal

    def get_all_countries(self):
        return self._dal.country.get_all_countries()
