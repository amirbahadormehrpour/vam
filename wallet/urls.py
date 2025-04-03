# wallet/urls.py
from django.urls import path
from .views import WalletListCreateView, WalletDetailView, TransactionListCreateView, TransactionDetailView,TransferView,SelfDepositView,AdminDepositView

urlpatterns = [

    path('wallets/', WalletListCreateView.as_view(), name='wallet-list'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('deposit/self/', SelfDepositView.as_view(), name='self_deposit'),
    path('deposit/admin/', AdminDepositView.as_view(), name='admin_deposit'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    

]