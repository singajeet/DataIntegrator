"""
.. module:: scripts.cli.manage_setup.py
        :platform: Unix, Windows
        :synopsis: Command Line interface (CLI) for the manage_setup module

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import plac
from scripts.core.manage_setup.install import SetupManager


@plac.annotations(install=('activate the install process for Data Integrator', 'flag', 'i'),
                  testdb=('Test stored database settings', 'flag', 't'),
                  list=('List all available databases', 'flag', 'l'),
                  help=('show help', 'flag'))
def main(install, testdb, list, help):
    if not any([install, testdb, list, help]):
        yield('no arguments passed, use .help to see the available commands')
    elif help:
        yield 'Commands: .install, .testdb, .list, .help'
    elif install:
        SetupManager().install()
    elif testdb:
        SetupManager().test_database()
    elif list:
        print('List of available databases:')
        print('----------------------------')
        count = 0
        for db in SetupManager().list():
            print('{}. {}'.format(count, db))
            count += 1


main.prefix_chars = '.'

if __name__ == '__main__':
    for output in plac.call(main):
        print(output)
