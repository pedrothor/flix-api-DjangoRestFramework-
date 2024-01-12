from django.urls import path
from reviews.views import ReviewListCreateView, ReviewRetrieverUpdateDestroyView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews-create-list-view'),
    path('reviews/<int:pk>', ReviewRetrieverUpdateDestroyView.as_view(), name='reviews-detail-view'),
]