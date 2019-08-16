from app import app
from flask import render_template, url_for
from app.forms import ResetPasswordRequestForm, ResetPasswordForm
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


# reset password request template
@app.route('/reset-password-request', methods=['GET'])
def reset_password_request():
    form = ResetPasswordRequestForm()
    return render_template('auth/reset_password_request.html', form=form)


# reset password request Post
@app.route('/reset-password-request', methods=['POST'])
def reset_password_request_recevie_form():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        account_email = form.email.data
        dest_url = 'http://127.0.0.1:5000/api/reset-password/email-sending-by-account-email'
        result = requests.post(dest_url, data={'account_email': account_email})
        account_to_reset = get_api_info(result)
        return render_template('auth/inform_reset_email.html', account_email=account_email)


# reset password template
@app.route('/reset-password/<string:token>', methods=['GET'])
def reset_password(token):
    form = ResetPasswordForm()
    # dest_url = 'http://127.0.0.1:5000/api/reset-password/token-receiving/' +\
    #            str(token)
    return render_template('auth/reset_password.html', form=form)


# register email sending inform
@app.route('/register-email-sending', methods=['GET'])
def register_email_inform():
    return render_template('auth/inform_register_email.html')


# register confirmation
@app.route('/register-confirmation', methods=['GET'])
def register_confirmation():
    return render_template('auth/register_confirmation.html')

