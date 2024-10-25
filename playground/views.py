from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    x=1
    context = {'fnames':"cyiza", 'lname':'debrice'}
    return render(request,"hello.html",context)
