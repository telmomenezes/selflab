import click
import selflab.db as db
import selflab.web.server as webserv


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
    dbname = ctx.obj['dbname']
    click.echo('Creating database %s' % dbname)
    db.create_db(dbname)


@cli.command()
@click.pass_context
def webserver(ctx):
    dbname = ctx.obj['dbname']
    click.echo('Using database %s' % dbname)
    webserv.start(dbname)


if __name__ == '__main__':
    cli()
