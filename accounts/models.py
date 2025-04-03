# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, national_id, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('شماره تلفن الزامی است')
        if not national_id:
            raise ValueError('کد ملی الزامی است')
        user = self.model(phone_number=phone_number, national_id=national_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, national_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_approved_by_admin', True)
        return self.create_user(phone_number, national_id, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='شماره تلفن')
    national_id = models.CharField(max_length=10, unique=True, verbose_name='کد ملی')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')
    is_approved_by_admin = models.BooleanField(default=False, verbose_name='تایید شده توسط مدیر')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت‌نام')  # اضافه شده
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['national_id']

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number
    
    
    
    # accounts/models.py
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='عکس پروفایل')
    address = models.TextField(verbose_name='آدرس')
    father_name = models.CharField(max_length=30, verbose_name='نام پدر')
    job = models.CharField(max_length=50, verbose_name='شغل')
    front_national_card = models.ImageField(upload_to='national_cards/front/', null=True, blank=True, verbose_name='عکس روی کارت ملی')
    back_national_card = models.ImageField(upload_to='national_cards/back/', null=True, blank=True, verbose_name='عکس پشت کارت ملی')
    postal_code = models.CharField(max_length=10, verbose_name='کد پستی')
    credit_score = models.IntegerField(default=1, verbose_name='درجه خوش‌حسابی')
    sheba_number = models.CharField(max_length=26, verbose_name='شماره شبا')
    coins = models.IntegerField(default=0, verbose_name='سکه‌ها')

    def __str__(self):
        return f"پروفایل {self.user.phone_number}"