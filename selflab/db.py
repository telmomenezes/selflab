import sqlite3


class DB:
    def __init__(self):
        self.conn = None
        self.cur = None

    def open(self):
        self.conn = sqlite3.connect('selflab.db')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def query(self, q):
        self.cur = self.conn.cursor()
        self.cur.execute(q)
        res = self.cur.fetchall()
        self.cur.close()
        return res

    def __exec_or_ignore(self, query):
        print('Executing query: %s' % query)
        try:
            self.cur.execute(query)
            print('executed.')
        except:
            print('ignored.')

    def create_db(self):
        # create tables
        self.open()

        # create event table
        self.__exec_or_ignore("CREATE TABLE event (id BIGINT PRIMARY KEY)")
        self.__exec_or_ignore("ALTER TABLE event MODIFY id BIGINT AUTO_INCREMENT")
        self.__exec_or_ignore("ALTER TABLE event ADD COLUMN ts INTEGER")
        self.__exec_or_ignore("ALTER TABLE event ADD COLUMN name TEXT")
        self.__exec_or_ignore("ALTER TABLE event ADD COLUMN type INTEGER")
        self.__exec_or_ignore("ALTER TABLE event ADD COLUMN quantity INTEGER")
        self.__exec_or_ignore("ALTER TABLE event ADD COLUMN value REAL")
        self.__exec_or_ignore("ALTER TABLE event ADD COLUMN details TEXT")

        self.__exec_or_ignore("CREATE INDEX event_ts ON event (ts)")
        self.__exec_or_ignore("CREATE INDEX event_name ON event (name)")

        self.conn.commit()
        self.close()
