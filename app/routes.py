from app import app
from flask import render_template, url_for
from app.forms import ResetPasswordRequestForm, ResetPasswordForm
from func_pack import get_api_info
import requests


@app.route('/')
@app.route('/tutorial')
def usage():
    usages = [
        {'api_format': '/api/competition/all-competitions', 'method': 'GET',
         'description': 'Get all competition infos'},
        {'api_format': '/api/competition/competition-name/<string:competition_name>', 'method': 'GET',
         'description': 'Get competitions info by its competition name'},
        {'api_format': '/api/competition/contributor-id/<string:contributor_id>', 'method': 'GET',
         'description': 'Get competitions by its owner(contributor_id)'},
        {'api_format': '/api/competition/hostname/<string:hostname>', 'method': 'GET',
         'description': 'Get competitions by its hostname'},
        {'api_format': '/api/competition/scenario/<string:scenario>', 'method': 'GET',
         'description': 'Get competitions by its scenario'},
        {'api_format': '/api/competition/data-feature/<string:data_feature>', 'method': 'GET',
         'description': 'Get competitions by its data feature'},
        {'api_format': '/api/competition/rid/<string:rid>', 'method': 'GET',
         'description': 'Get one competition info by its _id'},
        {'api_format': '/api/competition', 'method': 'POST',
         'description': 'Insert new competition infos'},
        {'api_format': '/api/competition/<string:rid>', 'method': 'PUT',
         'description': 'Modify an existed competition info'},
        {'api_format': '/api/competition/<string:rid>', 'method': 'DELETE',
         'description': 'Delete an existed competition info'},
        {'api_format': '/api/competition/comp-search/fuzzy/<string:keyword>', 'method': 'GET',
         'description': 'Fuzzy Search by comp_title, comp_host_name, comp_scenario or data_feature'},
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

