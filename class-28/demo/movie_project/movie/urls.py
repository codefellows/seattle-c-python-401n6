from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieDeleteView, MovieUpdateView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('new/', MovieCreateView.as_view(), name='movie_create'),
    path('<int:pk>/delete', MovieDeleteView.as_view(), name='movie_delete'),
    path('<int:pk>/update', MovieUpdateView.as_view(), name='movie_update'),
]
