from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('pictures', views.pictures, name='access_photos'),
    path('about_us', views.about_us, name='about_us'),
]
