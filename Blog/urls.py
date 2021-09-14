from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', bloglist, name="bloglist"),
    path('details/<int:id>', blogdetails, name="blogdetails"),
]
