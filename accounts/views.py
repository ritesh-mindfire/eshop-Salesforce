from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return HttpResponse(" <h1>All Set ! It's Working</h1>")