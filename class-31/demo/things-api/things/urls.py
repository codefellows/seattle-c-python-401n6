from django.urls import path
from .views import ThingsDetail, ThingsList
# http://127.0.0.1:8000/api/v1/ from project urls.py
urlpatterns = [

    path('', ThingsList.as_view(), name='things_list'),
    path('<int:pk>/', ThingsDetail.as_view(), name='things_detail')
]
