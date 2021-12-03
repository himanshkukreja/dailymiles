
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='accounts'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('data', views.data, name='data'),
]