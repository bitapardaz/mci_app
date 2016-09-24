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
from cryptography.hazmat.primitives.asymmetric import rsa


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

def pay_one_bill(mobile_no,bill_id,pay_id,pan,pin2):

    print "utilities - pay_one_bill - Starting .... "

    print "utilities - pay_one_bill - mobile_no:%s" % mobile_no
    print "utilities - pay_one_bill - bill_id:%s" % bill_id
    print "utilities - pay_one_bill - pay_id:%s" % pay_id
    print "utilities - pay_one_bill - pan:%s" % pan
    print "utilities - pay_one_bill - pin2:%s" % pin2

    pec_request = {}
    pec_request['MobileNo'] = mobile_no
    pec_request['PayInfo'] = generate_pay_info(pan,pin2)
    pec_request['Token'] = '0'
    pec_request['BillId'] = bill_id
    pec_request['PayId'] = pay_id
    pec_request['TerminalPin'] = "84y80M17HW810Y2j0434"
    data = json.dumps(pec_request)
    print "-------------------"
    print "pay_one_bill - json data sent to pec:"
    print "-------------------"
    print data
    print "----------------------------------"
    print "-------------------------------------"

    # Processing payment using pec_request
    print "pay_one_bill - Processing Payment Step"
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
    print "pay_one_bill - Header Items"
    print "-------------------"
    print request.header_items()

    # connection to pec server
    result = urllib2.urlopen(request,data)
    print "---------------------"
    print "pay_one_bill - result received from the server:"
    print result
    print "---------------------"

    j_result = json.loads(result.read().strip())
    status = j_result["Status"]
    message = j_result["Message"]
    Data = j_result["Data"]

    print "--------------------"
    print "pay_one_bill - Result turned into the format"
    print j_result
    print "--------------------"

    # Client Response
    client_response  = {}
    client_response['Status'] = status
    client_response['Message'] = message
    # if status = 0,
    # add payment verification request to the  using celery
    if status == 0 :
            score = Data['Score']
            print "pay_one_bill - score: %s" % score

            trace_no = Data['TraceNo']
            client_response['trace_no'] = trace_no
            print "pay_one_bill - trace_no: %s" % trace_no

            invoice_no = Data['InvoiceNumber']
            client_response['invoice_no'] = invoice_no
            print "pay_one_bill - invoice_no: %s" % invoice_no

            payment_confirmation(bill_id,pay_id,trace_no)
            # store a successful transaction in our database


    else:
        # store a failed transactoin into our database.
        # send appropriate message to the user
        # send a message to pec CRM
        print "***********************************************"
        print "pay_one_bill - Alert. Status: %s" % status
        print "pay_one_bill - Alert. Message: %s" % message
        print "***********************************************"


    # turn bill_info into json and return
    response =  Response(client_response)
    print "pay_one_bill - Payment Done!"
    return response

###################################################
### confirm payment
####################################################

def payment_confirmation(bill_id,pay_id,trace_no):

    print "payment_confirmation - bill_id: %s " % bill_id
    print "payment_confirmation - pay_id: %s " % pay_id
    print "payment_confirmation - trace_no: %s " % trace_no
    return "payment_confirmation - Done"

    url = 'https://Services.pec.ir/api/Telecom/Bill/SetPayInfo'
    username = 'aryan'
    password = '123123@'

    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    request.add_header("Content-Type","application/json")

    data = {}
    data['BillId'] = bill_id
    data['PayId'] = pay_id
    data['RRN'] = trace_no

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

###########################################################
### functions for creating client side (APP) ecryption ####
###########################################################

def extract_pin_pan(cipher_text):

    print "extract_pin_pan- cipher_text: %s" % cipher_text
    plaintext = decrypt(cipher_text)
    print "extract_pin_pan: %s" % plaintext

    pan = plaintext.split(":")[0][1:]
    pin = plaintext.split(":")[1][1:]
    return (pan,pin)

def decrypt(cipher_text):
    #cipher_text = "NJVx+CyzLiotD2zmOvASirKpuiXzdGte3n6/lY6DNGCYGqBqEJOO2ayGyduqHUubF23poxNpTFT+wNhhiJ5nghwNux1/0jf65K3fnnEdi8dE6RV13WIHcRZa1pT5sgHULy73fS8Gz3HGLkaKc/DJ+Cz0/eN9D1nYLLP+vVZEZyqeHFlbDIuiTsf6RbGOClassZWCth4Lv+kEW8aexXJOSRqyo/c+EK66Cqp16upLwI5Qu/039bK/xLWCcBiOTTyqZVUuMXK5PkCRqsNlzoCRhobOLgh/6ty6Xwi1aEjDTeP/CTV9yCHZwx2KQrjel2zXgLFYM777Uzr+oO4ikdS1TA=="
    ciphertext_byte = base64.b64decode(cipher_text)
    print "decrypt- ciphertext_byte:%s" % ciphertext_byte

    with open("private_key.pem", "rb") as private_key_file:
         private_key = serialization.load_pem_private_key(
             private_key_file.read(),
             password=None,
             backend=default_backend()
         )

    print "decrypt- ciphertext_byte: the actual decryption"
    plaintext = private_key.decrypt(
         ciphertext_byte,
         padding.OAEP(
             mgf=padding.MGF1(algorithm=hashes.SHA1()),
             algorithm=hashes.SHA1(),
             label=None
         )
    )

    print "decrypt- ciphertext_byte:%s" % plaintext
    return plaintext


def generate_public_private_pair():

    # generate private key
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=1024,backend=default_backend())
    pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())
    lines = pem.splitlines()
    private_key_file = open("private_key.pem", "w")
    for line in lines:
        private_key_file.write(line)
        private_key_file.write("\n")
    private_key_file.close()

    # generate public key
    public_key = private_key.public_key()
    pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
    lines = pem.splitlines()
    public_key_file = open("public_key.pem", "w")
    for line in lines:
        public_key_file.write(line)
        public_key_file.write("\n")
    public_key_file.close()

def test():


    with open("private_key.pem", "rb") as private_key_file:
         private_key = serialization.load_pem_private_key(
             private_key_file.read(),
             password=None,
             backend=default_backend()
         )

    with open("public_key.pem", "rb") as public_key_file:
         public_key = serialization.load_pem_public_key(
             public_key_file.read(),
             backend=default_backend()
         )

    message = "you can win"
    ciphertext = public_key.encrypt(
         message,
         padding.OAEP(
             mgf=padding.MGF1(algorithm=hashes.SHA1()),
             algorithm=hashes.SHA1(),
             label=None
         )
    )

    plaintext = private_key.decrypt(
         ciphertext,
         padding.OAEP(
             mgf=padding.MGF1(algorithm=hashes.SHA1()),
             algorithm=hashes.SHA1(),
             label=None
         )
    )

    print message == plaintext
