from django.urls import path
from . import views

app_name = 'newsletter'

urlpatterns = [
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('about/', views.about, name='about'),
]
