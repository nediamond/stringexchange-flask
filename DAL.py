from config import *
import MySQLdb
from random import choice

class DAL:
    def __init__(self):
        self.db = MySQLdb.connect(
            host= MYSQL_HOST,
            user=MYSQL_USER,
            passwd=MYSQL_PASS,
            db=MYSQL_DB,
            )

    def get_random_entry(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM shared_strings')
        result = cursor.fetchall()
        return choice(result)

    def add_entry(self, entry):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO shared_strings (string) VALUES (%s)',(entry,))
        cursor.execute('INSERT INTO shared_strings_ro (string) VALUES (%s)',(entry,))
        self.db.commit()
        return

    def remove_entry(self, id):
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM shared_strings WHERE id=%s',(str(id),))
        self.db.commit()
        return