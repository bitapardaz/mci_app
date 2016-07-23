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



    return Response("here you are ")


def get_bill_info_internal_query(number):

    output = {}
    output['TelNo'] = number
    output['BillID'] = '2222222'
    output['PayID'] = '333333'
    output['Amount'] = '444444'
    output['Status'] = '1'
    output['Message'] = "Hello TCI"
    return output

    url = 'https://Services.pec.ir/api/Telecom/BillGetBillInfo'

    username = 'aryan'
    password = '123123@'

    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)

    data = json.dumps({'number':number})
    print data

    result = urllib2.urlopen(request,data,{'Content-Type': 'application/json'})
    print result

    #return JSON
