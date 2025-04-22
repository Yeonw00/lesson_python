import logging
import logging.handlers
from ctypes import create_unicode_buffer

import config

smtp_host = 'smtp.gmail.com'
smtp_port = 587
from_email = config.from_email
to_email = config.to_email
username = config.username
password = config.password

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(),
    timeout=20
))

logger.info('test')
logger.critical('critical')
