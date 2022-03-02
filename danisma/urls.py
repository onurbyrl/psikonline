from os import name
from django import views
from django.urls import path
from danisma import views

app_name = 'danisma'

urlpatterns = [
    path('', views.danisma, name='danisma')
]