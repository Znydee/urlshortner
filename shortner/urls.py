from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="shortner-home"),
    path('create/',views.create_short_link, name="shortner-create"),
]
