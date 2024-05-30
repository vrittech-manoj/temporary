from django.http import HttpResponse

from django.shortcuts import render

def About(request):
    return render(request,"about.html")

def Contact(request):
    return HttpResponse("<html><marquee><h1 style='color:red'>WELCOME HERE,980808098098098 </h1></marquee></html>")