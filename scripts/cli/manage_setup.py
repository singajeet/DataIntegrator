"""
.. module:: scripts.cli.manage_setup.py
        :platform: Unix, Windows
        :synopsis: Command Line interface (CLI) for the manage_setup module

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import plac
from scripts.core.manage_setup.install import SetupManager

@plac.annotations(install = ('activate the install process for Data Integrator','flag', 'i'),
                  testdb = ('Test stored database settings','flag', 't'),
                  help = ('show help','flag'))
def main(install, testdb, help):
    if not any([install, testdb, help]):
        yield('no arguments passed, use .help to see the available commands')
    elif help:
        yield 'Commands: .install, .testdb, .help'
    elif install:
        SetupManager().install()
    elif testdb:
        SetupManager().test_database()

# main.add_help = False # there is a custom help, remove the default one
main.prefix_chars = '.' # use dot-prefixed commands

if __name__ == '__main__':
    for output in plac.call(main):
        print(output)
