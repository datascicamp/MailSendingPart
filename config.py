import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('WEB_SERVER_SECRET_KEY') or 'abcdef020301abc8c86f'

    # for Mail Server
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = '1'
    MAIL_USERNAME = 'leontian1024'
    MAIL_PASSWORD = '@last007'

    ADMINS = ['leontian1024@gmail.com']

    # for account info handling api
    ACCOUNT_SERVICE_IP = '174.137.53.253'
    ACCOUNT_SERVICE_PORT = '30501'
    ACCOUNT_SERVICE_URL = ACCOUNT_SERVICE_IP + ':' + ACCOUNT_SERVICE_PORT
