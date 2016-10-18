from django.shortcuts import render,redirect
from django.http import HttpResponse

from models import DownloadCounter,UserDownload

# Create your views here.
from .forms import MobileForm

def pfm_download(request):

    if request.method=="POST":
        pass

        form = MobileForm(request.POST)
        if form.is_valid():

            #check the counter
            counter_obj = DownloadCounter.objects.all()[0]

            if counter_obj.counter < 5000:

                mobile_no = form.cleaned_data['mobile_no']
                print "----------------"
                print mobile_no

                user = UserDownload(mobile_number = mobile_no)
                user.save()

                counter_obj.counter = counter_obj.counter + 1
                print counter_obj.counter
                counter_obj.save()
                return redirect("/pfm_promotion/download_page/")

            else:

                return HttpResponse("Promotion is Over. Keep checking this page :)")


    if request.method=="GET":
        print "-------------"
        print "you are here: GET"
        print "-------------"

        return render(request,'pfm_promotion/pfm_download_2.html')


def download_page(request):

    print "-------------"
    print "you are here: final download page"
    print "-------------"

    return render(request,'pfm_promotion/pfm_download_final_2.html')
