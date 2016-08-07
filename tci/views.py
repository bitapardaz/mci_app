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

from tci import utilities

from django.http import HttpResponse

from models import Phone

def my_bill(request):

    if request.method=='GET':

        phones = Phone.objects.all()

        # prepare the context
        context = {}
        counter = 0

        for phone in phones:
            tel_no_string = phone.tel_no
            tel_no = long(tel_no_string)

            bill_details = get_bill_info_internal_query(tel_no)
            print bill_details
            return HttpResponse(bill_details)

    if request.method='POST':
        return HttpResponse("You are here in the post section.")

    return render(request,'tci/my_bill.html')

class SafeString(str):
    def title(self):
        return self

    def capitalize(self):
        return self

def kitchen(request):
    return render(request,'tci/kitchen.html')


def web_homepage(request):
    return render(request,'tci/homepage.html')


@api_view(['POST'])
def pay_one_bill(request):

    if request.method == "POST":


        mobile_no = request.data.get('mobile_no')
        print "pay_one_bill - mobile_no:%s" % mobile_no

        bill_id = request.data.get('bill_id')
        print "pay_one_bill - bill_id:%s" % bill_id

        pay_id = request.data.get('pay_id')
        print "pay_one_bill - pay_id:%s" % pay_id

        pan = request.data.get('pan')
        print "pay_one_bill - pan:%s" % pan

        pin2 = request.data.get('pin2')
        print "pay_one_bill - pin2:%s" % pin2
        print "you are here"


        # validation step. Check if the data is validation
        #is_data_valid = validate_payment_info()

        response = utilities.pay_one_bill(mobile_no,bill_id,pay_id,pan,pin2)
        return response


    else:
        return Response("POST REQUESTS ONLY",status=status.HTTP_400_BAD_REQUEST)


def payment_confirmation(bill_id,pay_id,rrn):

    print "payment confirmation - starting ....."

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

    # do something with the error returned on this RRN

    return Output


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




def generate_pay_info(pan,pin2):

    message = {}
    message['PAN'] = pan
    message['Pin2'] = pin2
    message['ExpY'] = "0000"
    message['ExpM'] = "0000"
    message['CV'] = "0000"

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
    print "generate_pay_info- ciphertext_base_64 \n%s" % ciphertext_base_64

    print "Generating Pay Info Completed."
    return ciphertext_base_64.rstrip()
