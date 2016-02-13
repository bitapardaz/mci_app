from django.shortcuts import render
from django.http import HttpResponse
from models import Song

def list(request):

    song_list = Song.objects.all()
    context = {}
    context['songs'] = song_list

    return render(request,'rbt/list.html',context)
