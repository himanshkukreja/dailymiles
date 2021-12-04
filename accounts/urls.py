
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.home, name='accounts'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('data', views.data, name='data'),
    path('dashboard', views.dashboard, name='dashboard'),
]