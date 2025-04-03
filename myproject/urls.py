# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/loans/', include('loans.urls')),
    path('api/wallet/', include('wallet.urls')),
    path('api/referral/', include('referral.urls')),
]