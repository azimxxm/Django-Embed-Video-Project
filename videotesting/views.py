from django.shortcuts import render
from .models import *

def index(request):
    video = Video.objects.all()
    return render(request, 'base.html', {'video':video})