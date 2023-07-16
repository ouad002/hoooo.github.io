from django.shortcuts import render
from django import forms
from django.http import *
from django.urls import *

# Create your views here.
class newtaskform(forms.Form):
    task=forms.CharField(label="new task")


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
    return render(request,"tasks/index.html",{
        "tasks":request.session["tasks"]
    })
def add(request):
    if request.method=="POST":
        form=newtaskform(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    else:
        return render(request,"tasks/add.html",{
            "form":newtaskform()
        })