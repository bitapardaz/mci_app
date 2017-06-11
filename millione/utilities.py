import json
import requests
from rest_framework import status

def top_up_air_time(amount,mobile_number,operator):

    secret = "23497c89-35c4-4a81-be10-ed8fa68b6983"
    data = {}
    data['secret'] = secret
    data['amount'] = amount
    data['mobileNumber'] = mobile_number
    data['operator'] = operator

    ddata = json.dumps(data)

    url = 'https://m.paygear.org/api/TopUp/'
    headers = {'Content-Type': 'application/json'}
    result = requests.post(url,ddata,headers=headers)

    output = {}
    output['message'] = json.loads(result.text)['message']
    output['status'] = json.loads(result.text)['status']
    output['id'] = json.loads(result.text)['id']

    return output

def send_sign_up_sms(phone_number,verification_code):

    data = {}
    data['mobile'] = phone_number
    data['code'] = verification_code

    ddata = json.dumps(data)

    url = 'https://m.paygear.org/api/Account/RegisterByMobile/'
    headers = {'Content-Type': 'application/json'}
    result = requests.post(url,ddata,headers=headers)

    output = {}

    if result.status_code == status.HTTP_200_OK:
        output['status'] = "True"
    else:
        output['status'] = "False"

    return output
