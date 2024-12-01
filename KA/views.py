from django.shortcuts import render
from django.http import HttpResponse
def kiran(request):
    return HttpResponse('<h1> kiran is hero of KA</h1>')
def heroine1(request):
    return HttpResponse('<h1> Anjali is heroine of Ka</h1>')

# Create your views here.
