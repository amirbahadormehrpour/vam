# wallet/models.py
from django.db import models
from accounts.models import CustomUser

class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='موجودی')
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"کیف پول {self.user.phone_number} - موجودی: {self.balance}"
    
    # wallet/models.py
# wallet/models.py
class Transaction(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_transactions', verbose_name='فرستنده')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_transactions', null=True, blank=True, verbose_name='گیرنده')
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='مبلغ')
    transaction_type = models.CharField(max_length=10, choices=[('deposit', 'شارژ'), ('withdraw', 'برداشت'), ('transfer', 'انتقال')], verbose_name='نوع تراکنش')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    status = models.CharField(max_length=10, choices=[('success', 'موفق'), ('failed', 'ناموفق')], default='success', verbose_name='وضعیت')
    reference_id = models.CharField(max_length=100, null=True, blank=True)  # برای درگاه بانکی
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.sender.phone_number} - {self.transaction_type} - {self.amount}"