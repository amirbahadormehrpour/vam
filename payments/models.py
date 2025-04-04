# payments/models.py
from django.db import models
from accounts.models import CustomUser
from wallet.models import Transaction

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments', verbose_name='کاربر')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True, blank=True, related_name='payment', verbose_name='تراکنش')
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='مبلغ')
    status = models.CharField(max_length=20, choices=[('pending', 'در انتظار'), ('success', 'موفق'), ('failed', 'ناموفق')], default='pending', verbose_name='وضعیت')
    gateway_ref = models.CharField(max_length=100, null=True, blank=True, verbose_name='شناسه درگاه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f"پرداخت {self.amount} - {self.user.phone_number}"