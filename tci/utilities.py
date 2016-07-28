from django.shortcuts import render
import urllib2
import base64
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

from django.conf import settings

from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

def generate_pay_info(pan,pin2):

    message = {}
    message['PAN'] = pan
    message['Pin2'] = pin2
    message['ExpY'] = "00"
    message['ExpM'] = "00"
    message['CV'] = "000"

    print "Generating encrypted pay info"

    j_message = json.dumps(message)
    print "generate_pay_info- j_message: %s " % j_message

    public_key_file_path = settings.MEDIA_ROOT + "key.pem"
    print "generate_pay_info- public key file path: %s " % public_key_file_path

    public_key_file = open(public_key_file_path,"rb")
    print "generate_pay_info- public key file: %s " % public_key_file

    public_key_content = public_key_file.read()
    print "generate_pay_info- public key content: %s " % public_key_content
    public_key_file.close()

    public_key = serialization.load_pem_public_key(public_key_content,default_backend())
    print "generate_pay_info- public key : %s " % public_key

    ciphertext = public_key.encrypt(j_message,PKCS1v15())
    print "generate_pay_info- cypher text : %s " % ciphertext

    ciphertext_base_64 = base64.encodestring(ciphertext)
    ciphertext_base_64_updated = ''.join(ciphertext_base_64.strip().split("\n"))
    #base64_path = settings.MEDIA_ROOT + "base64.txt"
    #base64_file = open(base64_path,'w')
    #base64_file.write(ciphertext_base_64_updated)
    #base64_file.close()

    print "generate_pay_info- ciphertext_base_64 \n%s" % ciphertext_base_64_updated

    print "Generating Pay Info Completed."
    return ciphertext_base_64_updated


class SafeString(str):
    def title(self):
        return self

    def capitalize(self):
        return self

def pay():

    mobile_no = "09125498004"
    print "mobile_no:%s" % mobile_no

    bill_id = "4445152300146"
    print "bill_id:%s" % bill_id

    pay_id = "250110"
    print "pay_id:%s" % pay_id

    pan = "6219861024245069"
    print "pan:%s" % pan

    pin2 = "14725"
    print "pin2:%s" % pin2


    pec_request = {}
    pec_request['MobileNo'] = mobile_no
    pec_request['PayInfo'] = generate_pay_info(pan,pin2)
    pec_request['Token'] = '0'
    pec_request['BillId'] = bill_id
    pec_request['PayId'] = pay_id
    pec_request['TerminalPin'] = "84y80M17HW810Y2j0434"

    data = json.dumps(pec_request)
    print "-------------------"
    print "json data sent to pec:"
    print "-------------------"
    print data
    print "----------------------------------"

    print "-------------------------------------"
    # Processing payment using pec_request
    print "Processing Payment Step"
    print "-------------------------------------"

    #url = "https://app.pec.ir/api/Payment/BillPaymentGeneral"
    url = "https://testapp.pec.ir/api/Payment/BillPaymentGeneral"
    username = 'Pishahang'
    password = 'P!$h@h@ng0502'

    request = urllib2.Request(url)
    base64string = base64.encodestring('%s|%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    request.add_header("Content-Type","application/json")
    request.add_header(SafeString("appVersion"),"1.7")

    print "-------------------"
    print "Header Items"
    print "-------------------"
    print request.header_items()


    result = urllib2.urlopen(request,data)
    print "---------------------"
    print "result received from the server:"
    print result
    print "---------------------"

    j_result = json.loads(result.read().strip())
    status = j_result["Status"]
    message = j_result["Message"]
    Data = j_result["Data"]

    print "--------------------"
    print "Result turned into the format"
    print j_result
    print "--------------------"

    # Client Response
    client_response  = {}
    client_response['Status'] = status
    client_response['Message'] = message

    # turn bill_info into json and return
    response =  Response(client_response)
    print "Done"


####################################################
### confirm payment
####################################################

def verify_payment():

    url = 'https://Services.pec.ir/api/Telecom/Bill/SetPayInfo'
    username = 'aryan'
    password = '123123@'

    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    request.add_header("Content-Type","application/json")

    data = {}
    data['BillId'] = "4445152300146"
    data['PayId'] = "150166"
    data['RRN'] = "703529447612"

    j_data = json.dumps(data)
    result = urllib2.urlopen(request,j_data)

    # analysis of the response
    j_response = json.loads(result.read().strip())

    output = {}
    output['status'] = j_response['Status']
    output['message'] = j_response['Message']

    print "payment confirmation - output status: %s" % output['status']
    print "payment confirmation - output message: %s" % output['message']
    print output
