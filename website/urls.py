#  hello/urls.py

from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('search', views.search_page_view, name='search'),
    path('explore', views.explore_page_view, name='explore'),
]
