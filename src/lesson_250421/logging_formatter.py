import logging

# https://docs.python.org/ko/3/library/logging.html#logrecord-attributes

# formatter = '%(levelname)s:%(message)s'
formatter = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# logging.critical('critical')
# logging.error('error')
# logging.warning('warning')
# logging.info('info')
# logging.debug('debug')

# logging.info('info {}'.format('test'))
# logging.info('info %s %s' % ('test', 'test2'))
logging.info('info %s %s', 'test', 'test2')