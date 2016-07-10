import sqlite3


def exec_or_ignore(cur, query):
    print('Executing query: %s' % query)
    try:
        cur.execute(query)
        print('executed.')
    except:
        print('ignored.')


def create_db(file_path):
    conn = sqlite3.connect(file_path)
    cur = conn.cursor()

    # create event table
    exec_or_ignore(cur, 'CREATE TABLE event (id BIGINT PRIMARY KEY)')
    exec_or_ignore(cur, 'ALTER TABLE event MODIFY id BIGINT AUTO_INCREMENT')
    exec_or_ignore(cur, 'ALTER TABLE event ADD COLUMN ts INTEGER')
    exec_or_ignore(cur, 'ALTER TABLE event ADD COLUMN name TEXT')
    exec_or_ignore(cur, 'ALTER TABLE event ADD COLUMN type INTEGER')
    exec_or_ignore(cur, 'ALTER TABLE event ADD COLUMN quantity INTEGER')
    exec_or_ignore(cur, 'ALTER TABLE event ADD COLUMN value REAL')
    exec_or_ignore(cur, 'ALTER TABLE event ADD COLUMN details TEXT')

    exec_or_ignore(cur, 'CREATE INDEX event_ts ON event (ts)')
    exec_or_ignore(cur, 'CREATE INDEX event_name ON event (name)')

    conn.commit()
    cur.close()
    conn.close()
