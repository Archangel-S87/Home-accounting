import sqlite3


class DB:

    con = None
    cursor = None

    def __init__(self):
        # или :memory: чтобы сохранить в RAM
        self.con = sqlite3.connect("data.db")
        self.cursor = self.con.cursor()
        self.create()

    def create(self):
        tables = {
            'users': (
                'id integer PRIMARY KEY',
                'email text',
                'login text',
                'password text',
                'bill double'
            ),
            'categories': (
                'id integer PRIMARY KEY',
                'name text',
                'capacity integer',
                'author integer'
            ),
            'events': (
                'id integer PRIMARY KEY',
                'type text',
                'amount double',
                'category integer',
                'date numeric',
                'description text',
                'author integer'
            )
        }

        for name, columns in tables.items():
            columns = ', '.join(map(str, columns))
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {name} ({columns})')

        self.con.commit()
        pass

    def getCount(self, table, where):
        sql = f'SELECT COUNT(*) FROM {table} WHERE {where}'
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result[0]


