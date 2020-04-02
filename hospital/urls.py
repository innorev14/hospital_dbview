from django.urls import path

from . import views

app_name = 'hospital'

urlpatterns = [
    path('cbv', views.KeywordView.as_view(), name='keyword'),
    path('', views.keywordview, name='keyword_fbv'),
    path('naverapi/', views.naverAPIListView, name='naverapi'),
]