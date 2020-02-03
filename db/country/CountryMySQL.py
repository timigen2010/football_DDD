class CountryMySQL:

    def __init__(self, db):
        self.db = db

    def get_all_countries(self):
        query = "SELECT country_id, name FROM country"
        return self.db.execute(query)