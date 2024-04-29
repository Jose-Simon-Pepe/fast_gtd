import click
from os import chdir
from revision_semanal import run_past_revision, run_long_future_revision, run_short_future_revision

@click.command()
@click.option('--type',default=None, help='Tipo de revision a realizar')
def init(type):
    """
    Simple revision init
    1 = Past Revision 
    2 = Future Revision
    """
    chdir("/home/peace/fast_gtd/")
    if type is None:
        click.echo("Debe indicar un tipo de revision")
    else:
        if type=='1':
            run_past_revision()
        elif type=='2':
            run_short_future_revision()
        elif type=='3':
            run_long_future_revision()
        else:
            click.echo("Opcion incorrecta")

if __name__ == '__main__':
    init()
