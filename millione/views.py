from rest_framework.decorators import api_view

import json
from . import utilities

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST',])
def top_up(request,format=None):
    """
    Air time redemption
    """
    amount = request.data.get('amount')
    mobile_number = request.data.get('mobile_number')
    operator = request.data.get('operator')
    output = utilities.top_up_air_time(amount,mobile_number,operator)
    return Response(output)

@api_view(['POST',])
def sign_up(request):
    """
    sends verification sms that verifies users phone number.
    """
    mobile_number = request.data.get('mobile')
    verification_code = request.data.get('code')
    print verification_code
    output = utilities.send_sign_up_sms(mobile_number,verification_code)
    print output
    return Response(output)

class Top_up_edit(APIView):
    """
    test doc
    """
    def post(self,request,format=None):
        return Response({"message":"OK"})
