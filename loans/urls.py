# loans/urls.py
from django.urls import path
from .views import LoanListCreateView, LoanDetailView

urlpatterns = [
    path('loans/', LoanListCreateView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
]