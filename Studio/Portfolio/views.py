from django.shortcuts import render
from .models import *
# Create your views here.

def photo_list(request):
    photo_list = Photos.objects.all()
    context = {
        'photos':photo_list
    }
    return render(request,'Portfolio/photo_list.html',context)