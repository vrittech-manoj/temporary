
from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    # return HttpResponse("")
    return render(request,"index.html")


def About(request):
    # return HttpResponse("")
    return render(request,"about.html")


def Contact(request):
    # return HttpResponse("")
    return render(request,"contact.html")


