from AMARAN.views import *
from django.urls import path

urlpatterns=[
    path('SK/',SK,name='SK'),
    path('SP/',SP,name='SP'),
]