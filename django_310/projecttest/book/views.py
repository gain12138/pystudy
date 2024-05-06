from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
import time


# Create your views here.
def index(request):
    context = {
        'time' : time.ctime()
    }
    return render(request, 'book/index.html',context=context)
def index1(request):
    context = {
        'time' : time.ctime()
    }
    return render(request, 'book/index1.html',context=context)
