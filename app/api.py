from app import app
from flask import jsonify
from flask import request
from werkzeug.http import HTTP_STATUS_CODES
from email_pack import send_password_reset_email, send_register_email
from func_pack import get_api_info
from config import Config
import requests


# ---------------- registration ----------------- #
# send registration email by account_id fields
@app.route('/api/registration/email-sending-by-account-id', methods=['POST'])
def send_registration_email_by_account_id():
    account_id = request.form.get('account_id')
    destin_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                 '/api/registration/token-creating/account-id/' + str(account_id)
    account_unverify = get_api_info(requests.get(destin_url))[0]
    send_register_email(account_unverify)
    data = [{'account_id': account_id, 'email_sending_status': 'success'}]
    return jsonify(data)


# send registration email by account_email fields
@app.route('/api/registration/email-sending-by-account-email', methods=['POST'])
def send_registration_email_by_account_email():
    account_email = request.form.get('account_email')
    destin_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                 '/api/registration/token-creating/account-email/' + str(account_email)
    account_unverify = get_api_info(requests.get(destin_url))[0]
    send_register_email(account_unverify)
    data = [{'account_email': account_email, 'email_sending_status': 'success'}]
    return jsonify(data)


# receive registration token
@app.route('/api/registration/token-receiving/<string:token>', methods=['GET'])
def receive_registration_token(token):
    data = list()
    destin_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                 '/api/registration/token-receiving/' + str(token)
    result = requests.get(destin_url)
    # Incorrect operations with error response
    if result.status_code == 400:
        return result.content
    # change account_status
    else:
        account_verified = get_api_info(result)[0]
        if account_verified['account_status'] == 'unverify':
            account_verified['account_status'] = 'verified'
        # update account_status in db
        update_account_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                             '/api/account/account-updating'
        requests.put(update_account_url, data=account_verified)
        data.append(account_verified)
        return jsonify(data)


# ---------------- reset password ----------------- #
# send reset password email by account_id fields
@app.route('/api/reset-password/email-sending-by-account-id', methods=['POST'])
def send_reset_password_email_by_account_id():
    account_id = request.form.get('account_id')
    destin_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                 '/api/reset-password/token-creating/account-id/' + str(account_id)
    account_to_reset = get_api_info(requests.get(destin_url))[0]
    send_password_reset_email(account_to_reset)
    data = [{'account_id': account_id, 'email_status': 'success'}]
    return jsonify(data)


# send reset password email by account_email fields
@app.route('/api/reset-password/email-sending-by-account-email', methods=['POST'])
def send_reset_password_email_by_account_email():
    account_email = request.form.get('account_email')
    destin_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                 '/api/reset-password/token-creating/account-email/' + str(account_email)
    account_to_reset = get_api_info(requests.get(destin_url))[0]
    send_password_reset_email(account_to_reset)
    data = [{'account_email': account_email, 'email_status': 'success'}]
    return jsonify(data)


# receive reset password token
@app.route('/api/reset-password/token-receiving/<string:token>', methods=['GET'])
def receive_reset_password_token(token):
    data = list()
    destin_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                 '/api/reset-password/token-receiving/' + str(token)
    result = requests.get(destin_url)
    # Incorrect operations with error response
    if result.status_code == 400:
        return result.content
    # change account_status
    else:
        account_to_reset = get_api_info(result)[0]
        data.append(account_to_reset)
        return jsonify(data)


# ---------------- functional defines ----------------- #
# bad requests holder
def bad_request(message):
    return error_response(400, message)


# error response
def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response



