from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
# Create your views here.

def viewIt(request):
    return render(request, 'home/index.html', {})
