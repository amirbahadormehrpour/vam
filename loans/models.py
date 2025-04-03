# loans/models.py
from django.db import models
from accounts.models import CustomUser

class Loan(models.Model):
    loan_number = models.CharField(max_length=20, unique=True, verbose_name='شماره وام')
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='مبلغ وام')
    installment_count = models.IntegerField(verbose_name='تعداد اقساط')
    start_date = models.DateField(verbose_name='تاریخ شروع')
    max_participants = models.IntegerField(verbose_name='حداکثر تعداد ثبت‌نام')
    current_participants = models.IntegerField(default=0, verbose_name='تعداد فعلی ثبت‌نام')
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.01, verbose_name='نرخ کارمزد')
    status = models.CharField(max_length=20, choices=[('open', 'باز'), ('closed', 'بسته'), ('completed', 'تکمیل‌شده')], default='open', verbose_name='وضعیت')

    def __str__(self):
        return self.loan_number
    
    # loans/models.py
class PromissoryNote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='مبلغ')
    issue_date = models.DateField(verbose_name='تاریخ صدور')
    due_date = models.DateField(verbose_name='تاریخ سررسید')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return f"{self.user.phone_number} - {self.amount}"
    
    
    # loans/models.py
class LoanRegistration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name='وام')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت‌نام')
    status = models.CharField(max_length=20, choices=[('pending', 'در انتظار'), ('approved', 'تایید شده')], default='pending', verbose_name='وضعیت')

    def __str__(self):
        return f"{self.user.phone_number} - {self.loan.loan_number}"
    
    # loans/models.py
class Installment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name='وام')
    installment_number = models.IntegerField(verbose_name='شماره قسط')
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='مبلغ قسط')
    due_date = models.DateField(verbose_name='تاریخ سررسید')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده')

    def __str__(self):
        return f"{self.loan.loan_number} - قسط {self.installment_number}"