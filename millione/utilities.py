import json
import urllib2
import requests

def top_up_air_time(amount,mobile_number,operator,):

    secret = "23497c89-35c4-4a81-be10-ed8fa68b6983"
    data = {}
    data['secret'] = secret
    data['amount'] = amount
    data['mobileNumber'] = mobile_number
    data['operator'] = operator

    ddata = json.dumps(data)

    url = 'http://m.paygear.org/api/TopUp/'
    headers = {'Content-Type': 'application/json'}
    result = requests.post(url,ddata,headers=headers)

    output = {}
    output['message'] = json.loads(result.text)['message']
    output['status'] = json.loads(result.text)['status']
    output['id'] = json.loads(result.text)['id']

    return output
