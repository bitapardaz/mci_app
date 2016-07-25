from django.shortcuts import render
import urllib2
import base64
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
import json

from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15



@api_view(['POST'])
def pay_one_bill(request):

    if request.method == "POST":

        mobile_no = request.data.get('mobile_no')
        print "mobile_no:%s" % mobile_no

        bill_id = request.data.get('bill_id')
        print "bill_id:%s" % bill_id

        pay_id = request.data.get('pay_id')
        print "pay_id:%s" % pay_id

        pan = request.data.get('pan')
        print "pan:%s" % pan

        pin2 = request.data.get('pin2')
        print "pin2:%s" % pin2



        print "-------------------------------------"
        # Processing payment using pec_request
        print "Processing Payment Step"
        print "-------------------------------------"

        pec_request = {}
        pec_request['MobileNo'] = mobile_no
        pec_request['PayInfo'] = generate_pay_info(pan,pin2)
        pec_request['Token'] = '0'
        pec_request['BillId'] = bill_id
        pec_request['PayId'] = pay_id
        pec_request['TerminalPin'] = "84y80M17HW810Y2j0434"

        print "___________"
        print "you are here"
        print "-----------"
        return Request("you are here")


        url = "https://app.pec.ir/api/Payment/BillPaymentGeneral"
        username = 'Pishahang'
        password = 'P!$h@h@ng0502'
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        request.add_header("Content-Type","application/json")

        data = json.dumps(pec_request)
        print "-------------------"
        print "json data sent to pec:"
        print "-------------------"
        print data
        print "----------------------------------"

        #result = urllib2.urlopen(request,data)




        #parse the result and get the components out.
        # Client Response
        client_response  = {}
        client_response['Status'] = 0
        client_response['Message'] = 'Successful Payment'
        client_response['Score'] = ' '
        client_response['TraceNo'] = '12312432432'
        client_response['InvoiceNumber'] = '0982093842'

        # turn bill_info into json and return
        response =  Response(client_response)
        return response


    else:
        return Response("POST REQUESTS ONLY",status=status.HTTP_400_BAD_REQUEST)



def generate_pay_info(pan,pin2):

    message = {}
    message['PAN'] = pan
    message['Pin2'] = pin2
    message['ExpY'] = "0000"
    message['ExpM'] = "0000"
    message['CV'] = "0000"

    print "Generating encrypted pay info"

    j_message = json.dumps(message)

    public_key_file = open("key.pem","rb")
    public_key = serialization.load_pem_public_key(public_key_file.read(),default_backend())

    ciphertext = public_key.encrypt(j_message,PKCS1v15())
    ciphertext_base_64 = base64.encodestring(ciphertext)

    print "Ciphertext in base 64 \n%s" % ciphertext_base_64
    return ciphertext_base_64



@api_view(['POST'])
def get_bill_info_single_number(request):

    if request.method=="POST":

        output = {}
        tel_no_string = request.data.get('tel_no')
        tel_no = long(tel_no_string)

        bill_info = get_bill_info_internal_query(tel_no)
        print bill_info

        output['bill_info'] = bill_info
        response =  Response(output)
        return response


    else:
        return Response("POST REQUESTS ONLY",status=status.HTTP_400_BAD_REQUEST)



def get_bill_info_internal_query(number):

    url = 'https://Services.pec.ir/api/Telecom/Bill/GetBillInfo'

    username = 'aryan'
    password = '123123@'

    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    request.add_header("Content-Type","application/json")

    data = json.dumps({'TelNo':number})
    result = urllib2.urlopen(request,data)

    j_response = json.loads(result.read().strip())

    output = {}
    output['telNo'] = j_response['TelNo']
    output['billId'] = j_response['BillID']
    output['payId'] = j_response['PayID']
    output['amount'] = j_response['Amount']
    output['status'] = j_response['Status']
    output['message'] = j_response['Message']

    return output


def generate_rsa_representation():
    key_string = "sDUFxOscSdkJmarPjvsQRe9mNuEVR2Y4rz7YAlHFFypCcjYPrlu27kIxh2i3HVihR+O+Qi68nwFPVcgOTFUL5A6MEW2kjMl9YnKHZCxXHyEoPrC2cFN61+yQ317hzGcUFPmYu1u85gNDOYtdXDI/tyl6zWZhhTzEIqhBo1O74qc="
    key = RSA.importKey(key_string,passphrase=None)
    #Encrypt something with public key and print to console
    encrypted = pub_key.encrypt('hello world', None) # the second param None here is useless
    print(encrypted)

def test_RAS(text):

    #private_key = RSA.generate(1024)
    #print(private_key.exportKey())

    private_key_string = 'sDUFxOscSdkJmarPjvsQRe9mNuEVR2Y4rz7YAlHFFypCcjYPrlu27kIxh2i3HVihR+O+Qi68nwFPVcgOTFUL5A6MEW2kjMl9YnKHZCxXHyEoPrC2cFN61+yQ317hzGcUFPmYu1u85gNDOYtdXDI/tyl6zWZhhTzEIqhBo1O74qc='
    private_key = RSA.importKey(private_key_string,passphrase=None)

    public_key = private_key.publickey()
    print(public_key.exportKey())

    encrypted = public_key.encrypt('hello world', None)
    print("Encrypted Text is: %s" % encrypted)

    text2 = private_key.decrypt(encrypted)
    print("original decrypted file was: %s" % text)
