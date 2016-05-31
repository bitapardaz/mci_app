from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    return render(request,'website/homepage_responsive.html')

def google_index(request):
    return render(request,'website/google450805d50c86330d.html')
