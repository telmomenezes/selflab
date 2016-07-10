def html():
    return """
    <form action='/new_event' method='post'>
        Name:<br>
        <input type="text" name="name"><br>
        Quantity:<br>
        <input type="text" name="quantity"><br>
        Value:<br>
        <input type="text" name="value"><br>
        Details:<br>
        <input type="text" name="details"><br>
        <input type="submit" value="Add">
    </form>
    """


def add(db, name, quantity, value, details):
    print('%s %s %s %s' % (name, quantity, value, details))
    db.execute('INSERT INTO event (name, quantity, value, details) VALUES (?, ?, ?, ?)',
               (name, int(quantity), float(value), details))
    db.commit()
