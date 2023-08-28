from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def home_page(request):
    context = {
        'today_date': date.today().strftime("%B %d, %Y")
    }
    return render(request, 'photo_ap/home.html', context)


def pictures(request):
    return HttpResponse("Your Pictures are here...")