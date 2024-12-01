"""
URL configuration for MOVIES project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import KA.urls
from PUSHPA.views import *
from PUSHPA2.views import *
import AMARAN,KA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hero/',hero,name='hero'),
    path('heroine1/',heroine1,name='heroine1'),
    path('Hero/',Hero,name='Hero'),
    path('Heroine1/',Heroine1,name='Heroine1'),
    path('AMARAN/',include('AMARAN.urls')),
    path('KA/',include('KA.urls')),
         
]
