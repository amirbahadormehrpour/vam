# referral/models.py
from django.db import models
from accounts.models import CustomUser

class ReferralCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='referral_code')
    code = models.CharField(max_length=10, unique=True, verbose_name='کد رفرال')
    invited_count = models.IntegerField(default=0, verbose_name='تعداد دعوت‌شده‌ها')

    def __str__(self):
        return f"{self.user.phone_number} - {self.code}"