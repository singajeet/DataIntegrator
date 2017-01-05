"""
.. module:: scripts.cli.manage_setup.py
        :platform: Unix, Windows
        :synopsis: Command Line interface (CLI) for the manage_setup module

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import click
from integrator.core.manage_setup.install import SetupManager


@click.group()
def main():
    """Command Line Interface (CLI) for Data Integrator setup support
    """
    print('Command Line Interface (CLI) for Data Integrator setup support\n')


@main.group()
def install():
    """Use to install DI components. See --help to see more options
    """
    pass


@main.group()
def list():
    """Shows the list of DI components. See --help to see more options
    """
    pass


@main.group()
def test():
    """Test a DI component. See --help to see more options
    """
    pass


@list.command()
def list_db():
    """List all the installed plugins for storing metadata in the database
    """
    print('Below is the list of installed database plugins:')
    print('------------------------------------------------')
    counter = 0
    for db in SetupManager().list_db():
        print('{}. {}'.format(counter, db))
        counter += 1


@install.command()
@click.option('--db_plugin_name', help='The db_plugin_name for database. See \'list\' command for more info')
def install_db(db_plugin_name):
    """Install and configure the selected database for storing the metadata
    """
    setup_manager = SetupManager()
    if setup_manager.count_db() > 0:
        if db_plugin_name in [db for db in setup_manager.list_db()]:
            setup_manager.install_db(db_plugin_name)
        else:
            print('Invalid database plugin name. Please check the \'list\' command for valid name')
    else:
        print('No database plugins found installed. Please check with your admin!')


@test.command()
def test_db():
    """Tests the connectivity of existing database configured for storing metadata
    """
    SetupManager().test_db()


if __name__ == '__main__':
    main()
