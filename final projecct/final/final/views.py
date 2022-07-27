from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    return render(request,"index.html")

def aboutUS(request):

    return HttpResponse("welcome to baljinder shop")
    
def courseDetail(request,courseid):

    return HttpResponse("courseid")