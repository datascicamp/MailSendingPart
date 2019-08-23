import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('WEB_SERVER_SECRET_KEY') or 'abcdef020301abc8c86f'

    # for Mail Server
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = '1'
    MAIL_USERNAME = 'leontian1024'
    MAIL_PASSWORD = ''

    ADMINS = ['leontian1024@gmail.com']

    # for account info handling api
    ACCOUNT_SERVICE_IP = '127.0.01'
    ACCOUNT_SERVICE_PORT = '4998'
    ACCOUNT_SERVICE_URL = ACCOUNT_SERVICE_IP + ':' + ACCOUNT_SERVICE_PORT

    # for Auth UI sending API location
    AUTH_UI_SERVICE_IP = '127.0.0.1'
    AUTH_UI_SERVICE_PORT = '5000'
    AUTH_UI_RESET_PASSWORD_API = '/reset-password/'
    AUTH_UI_REGISTER_CONFIRM_API = '/register-confirmation/'
    AUTH_UI_RESET_PASSWORD_URL = AUTH_UI_SERVICE_IP + ':' + AUTH_UI_SERVICE_PORT + AUTH_UI_RESET_PASSWORD_API
    AUTH_UI_REGISTER_CONFIRM_URL = AUTH_UI_SERVICE_IP + ':' + AUTH_UI_SERVICE_PORT + AUTH_UI_REGISTER_CONFIRM_API
