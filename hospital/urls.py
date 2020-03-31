from django.urls import path

from . import views

app_name = 'hospital'

urlpattern = [
    path('', views.KeywordView.as_view(), name='keyword')
]