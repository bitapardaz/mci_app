from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

from models import UserProfile,MobileDevice
from django.utils import timezone
import datetime

@api_view(['POST'])
def register(request,format=None):
    """
    creates a new user by having her mobile number
    """
    if request.method == 'POST':

        mobile_number = request.data.get('mobile_no')
        imei = request.data.get('imei')
        token_string = request.data.get('token')

        import pdb; pdb.set_trace()

        if is_mobile_valid(mobile_number):

            result = {}

            try:


                import pdb; pdb.set_trace()
                new_user = User.objects.get(username=mobile_number)

            except User.DoesNotExist:
                # this is a new user
                print "register - the user is new"
                (user_profile,mobile_device) = set_up_user(mobile_number,imei,token_string)

                import pdb; pdb.set_trace()

                result['outcome'] = "new_customer"
                result['sms_code'] = mobile_device.sms_verification_code
                return Response(result,status=status.HTTP_201_CREATED)

            else:
                # the user already exists. check if there is a new token.
                try:
                    print "register - the user already exists. Checking the token"
                    existing_user = new_user

                    print "register - get user profile"


                    import pdb; pdb.set_trace()
                    user_profile = UserProfile.objects.get(user=existing_user)

                    print "register - get user mobile device"
                    mobile_device = MobileDevice.objects.get(user_profile=user_profile,imei=imei)

                except MobileDevice.DoesNotExist:
                    # user exists, imei does not
                    # the user has changed his phone
                    # and then new imei and token must be stored.
                    mobile_device = MobileDevice(user_profile = user_profile,
                                                 imei = imei,
                                                 token_string = token_string,
                                                 sms_verification_code = generate_sms_verification_code(imei),
                                                 sms_code_expiery = timezone.now() + datetime.timedelta(minutes=5)
                                                 )
                    mobile_device.save()
                    result['outcome'] = "returning_customer with new imei (new phone)"
                    result['sms_code'] = mobile_device.sms_verification_code

                else:
                    # new token for the same mobile phone and user
                    # and has uninstalled/installed the program.


                    import pdb; pdb.set_trace()
                    mobile_device.token_string = token_string
                    mobile_device.sms_verification_code = generate_sms_verification_code(imei)
                    mobile_device.sms_code_expiery = timezone.now() + datetime.timedelta(minutes=5)
                    mobile_device.save()
                    import pdb; pdb.set_trace()
                    result['outcome'] = "returning_customer who has unistalled and installed the program (same imei new token)"
                    result['sms_code'] = mobile_device.sms_verification_code


                finally:
                    return Response(result, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



def registeration_verification():
    return Response("customer verified")

def is_mobile_valid(mobile_number):
    return True


def set_up_user(mobile_number,imei,token_string):


    print "set_up_user - setting up a user started."
    print "set_up_user - creating a new user."
    new_user = User.objects.create_user(username = mobile_number)

    print "set_up_user - creating a new profile."

    new_profile = UserProfile(user=new_user)

    if imei != None:
        new_profile.imei = imei

    new_profile.last_visit = timezone.now()
    new_profile.is_active = True
    new_profile.save()

    print "set_up_user - user profile set up completed. user profile id: %d" % new_profile.id
    print "set_up_user - creating MobileDevice"

    mobile_device = MobileDevice(user_profile = new_profile,
                                 imei = imei,
                                 token_string = token_string,
                                 sms_verification_code = generate_sms_verification_code(imei),
                                 sms_code_expiery = timezone.now() + datetime.timedelta(minutes=5)
                                )

    mobile_device.save()
    print "set_up_user - creating MobileDevice done, imei:%s" % imei

    return (new_profile,mobile_device)

def generate_sms_verification_code(imei):
    # generate the code based on "Erfan, time and imei"
    return "123"
