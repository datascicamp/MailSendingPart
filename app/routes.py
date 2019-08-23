from app import app
from flask import render_template, url_for
from func_pack import get_api_info
import requests


@app.route('/')
@app.route('/tutorial')
def usage():
    usages = [
        {'api_format': '/api/registration/email-sending-by-account-id', 'method': 'POST',
         'description': 'Send registration email by account_id fields'},
        {'api_format': '/api/registration/email-sending-by-account-email', 'method': 'POST',
         'description': 'Send registration email by account_email fields'},
        {'api_format': '/api/registration/token-receiving/<string:token>', 'method': 'GET',
         'description': 'Receive registration token'},
        {'api_format': '/api/reset-password/email-sending-by-account-id', 'method': 'POST',
         'description': 'Send reset password email by account_id fields'},
        {'api_format': '/api/reset-password/email-sending-by-account-email', 'method': 'POST',
         'description': 'Send reset password email by account_email fields'},
        {'api_format': '/api/reset-password/token-receiving/<string:token>', 'method': 'GET',
         'description': 'Receive reset password token'},
    ]

    return render_template('frontPage.html', usage_infos=usages)


