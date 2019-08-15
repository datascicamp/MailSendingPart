import os
import requests

if __name__ == '__main__':

    # result = requests.post('http://localhost:5000/api/registration/email-sending-by-account-id', data={'account_id': '1'})
    # print(result.content)

    # result = requests.post('http://localhost:5000/api/registration/email-sending-by-account-email', data={'account_email': 'xinyaotian@yeah.net'})
    # print(result.content)

    result = requests.post('http://localhost:5000/api/reset-password/email-sending-by-account-id', data={'account_id': '1'})
    print(result.content)

    pass


