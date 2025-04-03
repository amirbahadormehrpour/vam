# accounts/urls.py
from django.urls import path
from .views import UserListCreateView, UserDetailView,LoginView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginView.as_view(), name='login'),
]