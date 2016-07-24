from django.shortcuts import render
import urllib2
import base64
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers



@api_view(['POST'])
def pay_one_bill(request):

    if request.method == "POST":

        mobile_no = request.data.get('mobile_no')
        print "mobile_no:%s" % mobile_no

        bill_id = request.data.get('bill_id')
        print "bill_id:%s" % bill_id

        pay_id = request.data.get('pay_id')
        print "pay_id:%s" % pay_id

        pan = request.data.get('card_number')
        print "pan:%s" % pan

        pin2 = request.data.get('pin2')
        print "pin2:%s" % pin2

        pec_request = {}
        pec_request['MobileNo'] = mobile_no
        pec_request['PayInfo'] = generate_pay_info(pan,pin2)
        pec_request['Token'] = ' '
        pec_request['BillId'] = bill_id
        pec_request['PayId'] = pay_id
        pec_request['TerminalPin'] = ' Get from mr Mohammadi'

        # processing payment using pec_request
        print "-------------------------------------"
        print "Processing Payment Step"
        print "-------------------------------------"

        # based on the response from pec, send these
        client_response  = {}
        client_response['Status'] = ' '
        client_response['Message'] = ' '
        client_response['Score'] = ' '
        client_response['TraceNo'] = ' '
        client_response['InvoiceNumber'] = ' '

        # turn bill_info into json and return
        response =  Response(client_response)
        return response


    else:
        return Response("POST REQUESTS ONLY",status=status.HTTP_400_BAD_REQUEST)


def generate_pay_info():
    return "pay_info_content"


@api_view(['POST'])
def get_bill_info_single_number(request):

    if request.method=="POST":

        output = {}

        tel_no = request.data.get('tel_no')
        bill_info = get_bill_info_internal_query(tel_no)

        output['bill_info'] = bill_info

        # turn bill_info into json and return
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
    output['billId'] = j_response['BillId']
    output['payId'] = j_response['PayId']
    output['amount'] = j_response['Amount']
    output['status'] = j_response['Status']
    output['message'] = j_response['Message']

    return output
