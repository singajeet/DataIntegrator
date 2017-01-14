"""
.. module:: integrator.log.logger
        :platform: Unix, Windows
        :synopsis: Utility class to create logger

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import logging


def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
