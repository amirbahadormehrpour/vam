# notifications/models.py
from django.db import models
from accounts.models import CustomUser

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications', verbose_name='کاربر')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_read = models.BooleanField(default=False, verbose_name='خوانده‌شده')
    sent_via_sms = models.BooleanField(default=False, verbose_name='ارسال‌شده با اس‌ام‌اس')

    def __str__(self):
        return f"اعلان برای {self.user.phone_number}"