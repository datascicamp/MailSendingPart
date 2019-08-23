from flask_mail import Message
from flask import render_template
from app import mail
from app import app
from threading import Thread
from config import Config


# send async email
def send_async_email(current_app, msg):
    with current_app.app_context():
        mail.send(msg)


# function of sending email
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()
    # mail.send(msg)


# send register confirm email
def send_register_email(account_dict):
    token = account_dict['token']
    register_url = 'http://' + Config.AUTH_UI_REGISTER_CONFIRM_URL + token
    send_email('Registration Verification',
               sender=app.config['ADMINS'][0],
               recipients=[account_dict['account_email']],
               text_body=render_template('email/register_template.txt', register_url=register_url),
               html_body=render_template('email/register_template.html', register_url=register_url))


# send password resetting email
def send_password_reset_email(account_dict):
    token = account_dict['token']
    reset_url = 'http://' + Config.AUTH_UI_RESET_PASSWORD_URL + str(token)
    send_email('Reset Password',
               sender=app.config['ADMINS'][0],
               recipients=[account_dict['account_email']],
               text_body=render_template('email/reset_password.txt', reset_url=reset_url),
               html_body=render_template('email/reset_password.html', reset_url=reset_url))

