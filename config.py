import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('WEB_SERVER_SECRET_KEY') or 'abcdef020301abc8c86f'

    # for Mail Server
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [os.environ.get('ADMIN')]

    # for account info handling api
    ACCOUNT_SERVICE_IP = os.environ.get('DSC_LOGIN_REGISTER_PART_SERVICE_HOST')
    ACCOUNT_SERVICE_PORT = os.environ.get('DSC_LOGIN_REGISTER_PART_SERVICE_PORT')
    ACCOUNT_SERVICE_URL = ACCOUNT_SERVICE_IP + ':' + ACCOUNT_SERVICE_PORT

    # for Auth UI sending API location
    AUTH_UI_SERVICE_IP = os.environ.get('WEBUI_HOST')
    AUTH_UI_SERVICE_PORT = os.environ.get('WEBUI_PORT')
    AUTH_UI_RESET_PASSWORD_API = '/auth/reset-password/'
    AUTH_UI_REGISTER_CONFIRM_API = '/auth/register-confirmation/'
    AUTH_UI_RESET_PASSWORD_URL = AUTH_UI_SERVICE_IP + ':' + AUTH_UI_SERVICE_PORT + AUTH_UI_RESET_PASSWORD_API
    AUTH_UI_REGISTER_CONFIRM_URL = AUTH_UI_SERVICE_IP + ':' + AUTH_UI_SERVICE_PORT + AUTH_UI_REGISTER_CONFIRM_API
