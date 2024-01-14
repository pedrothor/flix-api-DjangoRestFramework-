from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView


urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create-view'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail-view'),
]