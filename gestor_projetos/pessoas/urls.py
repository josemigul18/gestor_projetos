from django.contrib import admin
from django.urls import path, include
from .views import persons_list
from .views import person_new
from .views import person_decide

urlpatterns = [
    path('list/', persons_list, name="persons_list"),
    path('new/', person_new, name="person_new"),
    path('decide/', person_decide, name="person_decide"),
]
