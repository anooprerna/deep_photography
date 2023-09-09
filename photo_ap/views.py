from django.shortcuts import render
from datetime import date

from django.http import HttpResponseRedirect

def pictures(request):
    google_drive_url = 'https://drive.google.com/drive/folders/1WOc8WxDqNQNhGHMRg_v7x6P3JvJnZn1X?usp=sharing'
    return HttpResponseRedirect(google_drive_url)


def home_page(request):
    context = {
        'today_date': date.today().strftime("%B %d, %Y")
    }
    return render(request, 'photo_ap/home.html', context)

def about_us(request):
    return render(request, 'photo_ap/about_us.html')
