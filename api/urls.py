from django.urls import path
from api import views

urlpatterns = [
    path('home', views.home),
    path('', views.home),
    path('about', views.about),
    path('help', views.help),
]
