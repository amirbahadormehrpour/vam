# referral/models.py
from django.db import models
from accounts.models import CustomUser

class ReferralCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='referral_code')
    code = models.CharField(max_length=10, unique=True, verbose_name='کد رفرال')
    invited_count = models.IntegerField(default=0, verbose_name='تعداد دعوت‌شده‌ها')

    def __str__(self):
        return f"{self.user.phone_number} - {self.code}"
    
    # referral/models.py
class ReferralInvitation(models.Model):
    referrer = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='invitations_sent', verbose_name='دعوت‌کننده')
    invited_user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='invitations_received', verbose_name='دعوت‌شده')
    referral_code = models.ForeignKey(ReferralCode, on_delete=models.CASCADE, related_name='invitations', verbose_name='کد رفرال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ دعوت')

    def __str__(self):
        return f"{self.referrer.phone_number} دعوت کرد {self.invited_user.phone_number}"