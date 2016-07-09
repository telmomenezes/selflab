import click
from selflab.db import DB


@click.group()
@click.option('--db', help='Database name.')
@click.pass_context
def cli(ctx, db):
    ctx.obj = {
        'dbname': db
    }


@cli.command()
@click.pass_context
def create_db(ctx):
    db_name = ctx.obj['dbname']
    click.echo('Creating database %s' % db_name)
    db = DB(db_name)
    db.create_db()
    db.close()


if __name__ == '__main__':
    cli()
