from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from .forms import MobileForm

def pfm_download(request):

    if request.method=="POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            return redirect("/pfm_promotion/download_page/")

    if request.method=="GET":
        return render(request,'pfm_promotion/pfm_download.html')


def download_page(request):

    return render(request,'pfm_promotion/pfm_download_final.html')
