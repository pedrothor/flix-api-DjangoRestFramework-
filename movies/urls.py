from django.urls import path
from .views import MoviesListCreateView, MoviesRetrieveUpdateDestroyView

urlpatterns = [
    path('movies/', MoviesListCreateView.as_view(), name='movies-create-list-view'),
    path('movies/<int:pk>', MoviesRetrieveUpdateDestroyView.as_view(), name='movies-detail-view'),
]