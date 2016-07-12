import datetime


def row2event(row):
    return {'id': row[0],
            'ts': row[1],
            'name': row[2],
            'type': row[3],
            'quantity': row[4],
            'value': row[5],
            'details': row[6]}


def event_list(db, offset, count):
    result = db.execute('SELECT id, ts, name, type, quantity, value, details FROM event ORDER BY id DESC LIMIT ?, ?',
                        (offset, count))
    events = [row2event(row) for row in result]
    return events


def last_event(db):
    events = event_list(db, 0, 1)
    if len(events) == 0:
        return None
    else:
        return events[0]


def event2html(event):
    dt = datetime.datetime.fromtimestamp(event['ts']).strftime('%Y-%m-%d %H:%M:%S')
    return '<p>[%s] %s x%s (%s) %s</p>' % (dt, event['name'], event['quantity'], event['value'], event['details'])
