import configparser
# or any other dbengine
import pymysql as DbEngine


class IDb:
    def __init__(self):
        # need to be equal to config parameter
        self._engine = 'MySQL'
        self._connection = False
        self._connection_parameters = False

    def _read_config(self):
        config = configparser.ConfigParser()
        config.read('config')
        self._connection_parameters = dict(config.items(self._engine))
        self._connection_parameters['cursorclass'] = DbEngine.cursors.DictCursor

    def _connect(self):
        if not self._connection_parameters:
            self._read_config()
        self._connection = DbEngine.connect(**self._connection_parameters)

    def execute(self, query):
        result = False
        if not (self._connection and self._connection.ping(True)):
            self._connect()
        with self._connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            self._connection.commit()
        return result

    def __del__(self):
        if self._connection and self._connection.ping(True):
            self._connection.close()
