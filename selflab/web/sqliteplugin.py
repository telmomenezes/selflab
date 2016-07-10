import sqlite3
import inspect
from bottle import HTTPError


class SQLitePlugin(object):
    """ This plugin passes an sqlite3 database handle to route callbacks
    that accept a `db` keyword argument. If a callback does not expect
    such a parameter, no connection is made. You can override the database
    settings on a per-route basis. """

    name = 'sqlite'
    api = 2

    def __init__(self, dbfile=':memory:', autocommit=True, dictrows=True, keyword='db'):
        self.dbfile = dbfile
        self.autocommit = autocommit
        self.dictrows = dictrows
        self.keyword = keyword

    # def setup(self, app):
    #    ''' Make sure that other installed plugins don't affect the same
    #        keyword argument.'''
    #    for other in app.plugins:
    #        if not isinstance(other, SQLitePlugin):
    #            continue
    #        if other.keyword == self.keyword:
    #            raise PluginError("Found another sqlite plugin with "\
    #            "conflicting settings (non-unique keyword).")

    def apply(self, callback, context):
        # Override global configuration with route-specific values.
        conf = context.config.get('sqlite') or {}
        dbfile = conf.get('dbfile', self.dbfile)
        autocommit = conf.get('autocommit', self.autocommit)
        dictrows = conf.get('dictrows', self.dictrows)
        keyword = conf.get('keyword', self.keyword)

        # Test if the original callback accepts a 'db' keyword.
        # Ignore it if it does not need a database handle.
        callback_args = inspect.signature(context.callback).parameters
        if keyword not in callback_args:
            return callback

        def wrapper(*args, **kwargs):
            # Connect to the database
            db = sqlite3.connect(dbfile)
            # This enables column access by name: row['column_name']
            if dictrows:
                db.row_factory = sqlite3.Row
            # Add the connection handle as a keyword argument.
            kwargs[keyword] = db

            try:
                rv = callback(*args, **kwargs)
                if autocommit:
                    db.commit()
            except sqlite3.IntegrityError as e:
                db.rollback()
                raise HTTPError(500, "Database Error", e)
            finally:
                db.close()
            return rv

        # Replace the route callback with the wrapped one.
        return wrapper
