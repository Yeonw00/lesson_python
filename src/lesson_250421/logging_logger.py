import logging
import logtest
import logging_handler

logging.basicConfig(level=logging.INFO)

logging.info('info')

logger = logging.getLogger(__name__)
logger.info('from main')
logger.setLevel(logging.DEBUG)
logger.debug('debug')

logtest.do_something()
logging_handler.do_something()