from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'photo_ap/home.html')


def pictures(request):
    return HttpResponse("Your Pictures are here...")