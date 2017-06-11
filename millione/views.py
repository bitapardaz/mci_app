from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from . import utilities

@api_view(['POST',])
def top_up(request,format=None):

    amount = request.data.get('amount')
    mobile_number = request.data.get('mobile_number')
    operator = request.data.get('operator')
    output = utilities.top_up_air_time(amount,mobile_number,operator)
    return Response(output)

@api_view(['POST',])
def sign_up(request):
    
    mobile_number = request.data.get('mobile_number')
    output = utilities.send_sign_up_sms(mobile_number)
    return Response(output)
