from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def myapp_view(request):
    return HttpResponse("myapp_view")