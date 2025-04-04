# referral/urls.py
from django.urls import path
from .views import ReferralCodeListCreateView, ReferralCodeDetailView,ReferralInvitationListView

urlpatterns = [
    path('referral-codes/', ReferralCodeListCreateView.as_view(), name='referral-code-list'),
    path('referral-codes/<int:pk>/', ReferralCodeDetailView.as_view(), name='referral-code-detail'),
    path('invitations/', ReferralInvitationListView.as_view(), name='referral-invitation-list'),
]