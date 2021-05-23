from django.shortcuts import render

# Create your views here.

#  hello/views.py

from django.shortcuts import render


def home_page_view(request):
    return render(request, 'website/home.html')


def search_page_view(request):
    return render(request, 'website/search.html')


def explore_page_view(request):
    return render(request, 'website/explore.html')
