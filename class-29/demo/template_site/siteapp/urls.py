from django.urls import path
from .views import ThingListView, ThingDetailView, ThingCreateView, ThingUpdateView, ThingDeleteView, ThingAboutView

urlpatterns = [
    path('', ThingListView.as_view(), name='thing_list'),
    path('create/', ThingCreateView.as_view(), name='thing_create'),
    path('about/', ThingAboutView.as_view(), name='thing_about'),
    path('<int:pk>/', ThingDetailView.as_view(), name='thing_detail'),
    path('<int:pk>/delete/', ThingDeleteView.as_view(), name='thing_delete'),
    path('<int:pk>/update', ThingUpdateView.as_view(), name='thing_update'),
]
