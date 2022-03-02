from unicodedata import name
from django.urls import path
from uygulama import views

app_name = 'uygulama'

urlpatterns = [
    path('', views.index, name='index'),
    path('kayit/', views.kayit, name='kayit'),
    path('giris/', views.giris, name='giris')
]