
from django.contrib import admin
from django.urls import path
from .views import service

urlpatterns = [
    path('', service, name='service'),

]

