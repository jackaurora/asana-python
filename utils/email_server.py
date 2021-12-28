import yagmail
from parse_config import *

MAIL = yagmail.SMTP('development@digitalsix.com.au', parse_config.parse_config()['EMAIL']['token'])
