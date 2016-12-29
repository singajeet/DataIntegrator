"""
.. module:: scripts.cli.manage_setup.py
        :platform: Unix, Windows
        :synopsis: Command Line interface (CLI) for the manage_setup module

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import click
from scripts.core.manage_setup.install import SetupManager


@click.group()
def main():
    """Command Line Interface (CLI) for Data Integrator setup support
    """
    print('Command Line Interface (CLI) for Data Integrator setup support\n')


@main.command()
def list():
    """List all the installed plugins for storing metadata in the database
    """
    print('Below is the list of installed database plugins:')
    print('------------------------------------------------')
    counter = 0
    for db in SetupManager().list():
        print('{}. {}'.format(counter, db))
        counter += 1


@main.command()
@click.argument('db_plugin_name')
def install(db_plugin_name):
    """Install and configure the selected database (passed as argument)
        for storing the metadata

    Args:
        db_plugin_name(str):  Name of db plugin that needs to be installed
    """
    SetupManager().install(db_plugin_name)


@main.command()
def testdb():
    """Tests the connectivity of existing database configured for storing metadata
    """
    SetupManager().test_database()


if __name__ == '__main__':
    main()
