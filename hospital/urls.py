from django.urls import path

from . import views

app_name = 'hospital'

urlpatterns = [
    # path('', views.KeywordView.as_view(), name='keyword'),
    path('', views.keywordview, name='keyword_fbv')
]