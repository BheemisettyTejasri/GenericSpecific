from django.shortcuts import render
from django.http import HttpResponse
def Hero(request):
    return HttpResponse('<h1> Alluarjun is hero of KA</h1>')
def Heroine1(request):
    return HttpResponse('<h1> Rashmika is heroine of Ka</h1>')

# Create your views here.
