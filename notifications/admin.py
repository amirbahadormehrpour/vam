# notifications/admin.py
from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read', 'sent_via_sms')
    list_filter = ('is_read', 'sent_via_sms', 'created_at')
    search_fields = ('user__phone_number', 'message')