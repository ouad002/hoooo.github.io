from django.shortcuts import render
from django.http import *

# Create your views here.
def index(request):
    return render(request,"app1/index.html")
def intro(request,name):
    return HttpResponse("hello "+name)
