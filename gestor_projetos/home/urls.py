
from django.contrib import admin
from django.urls import path, include
from .views import home
from .views import my_logout


urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='logout'),
]
