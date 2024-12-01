from django.shortcuts import render
from django.http import HttpResponse
def SK(request):
    return HttpResponse('<h1> siva karthikeya is hero of Amaran</h1>')
def SP(request):
    return HttpResponse('<h1> sai pallavi is heroine of Amaran</h1>')

# Create your views here.
