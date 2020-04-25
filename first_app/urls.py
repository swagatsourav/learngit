from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('first_app/', views.index2, name='index2'),
    path('', views.first, name='first_page'),


]
