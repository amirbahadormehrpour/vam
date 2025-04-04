# payments/admin.py
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'gateway_ref', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__phone_number', 'gateway_ref')