import time


def html():
    return """
    <form action='/new_event' method='post'>
        <h3>NAME</h3>
        <input type="text" name="name"><br>
        <h3>QUANTITY</h3>
        <input type="text" name="quantity"><br>
        <h3>VALUE</h3>
        <input type="text" name="value"><br>
        <h3>DETAILS</h3>
        <input type="text" name="details"><br>
        <input type="submit" value="ADD">
    </form>
    """


def add(db, name, quantity, value, details):
    ts = int(time.time())
    name = name.lower()
    if len(quantity) > 0:
        quantity = int(quantity)
    else:
        quantity = None
    if len(value) > 0:
        value = float(value)
    else:
        value = None
    details = details.lower()
    db.execute('INSERT INTO event (ts, name, type, quantity, value, details) VALUES (?, ?, ?, ?, ?, ?)',
               (ts, name, 0, quantity, value, details))
    db.commit()
