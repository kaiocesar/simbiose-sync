__author__ = 'Admin'

import sqlite3

class MakeDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('/tmp/db_sync.db')

    def create_table(self):
        try:
            self.conn.execute("SELECT * FROM configs")
        except Exception as err:
            try:
                self.conn.execute('''CREATE TABLE configs
                    (ID INT PRIMARY KEY NOT NULL,
                    URL_1 TEXT NOT NULL,
                    PORT_1 INT NOT NULL,
                    URL_2 TEXT NOT NULL,
                    PORT_2 INT NOT NULL)
                ''')
                self.conn.close()
            except Exception as err:
                return False

        return True

# configs = MakeDatabase()
# configs.create_table()