import logging

# https://docs.python.org/ko/3.7/library/logging.handlers.html#modul3-logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logtest.log')
logger.addHandler(h)

def do_something():
    logger.info('from logging handler')
    logger.debug('from logging handler debug')