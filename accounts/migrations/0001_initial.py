# Generated by Django 3.2.16 on 2025-03-31 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(max_length=15, unique=True, verbose_name='شماره تلفن')),
                ('national_id', models.CharField(max_length=10, unique=True, verbose_name='کد ملی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('is_staff', models.BooleanField(default=False, verbose_name='کارمند')),
                ('is_approved_by_admin', models.BooleanField(default=False, verbose_name='تایید شده توسط مدیر')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='نام')),
                ('last_name', models.CharField(max_length=30, verbose_name='نام خانوادگی')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/', verbose_name='عکس پروفایل')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('father_name', models.CharField(max_length=30, verbose_name='نام پدر')),
                ('job', models.CharField(max_length=50, verbose_name='شغل')),
                ('front_national_card', models.ImageField(blank=True, null=True, upload_to='national_cards/front/', verbose_name='عکس روی کارت ملی')),
                ('back_national_card', models.ImageField(blank=True, null=True, upload_to='national_cards/back/', verbose_name='عکس پشت کارت ملی')),
                ('postal_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('credit_score', models.IntegerField(default=1, verbose_name='درجه خوش\u200cحسابی')),
                ('sheba_number', models.CharField(max_length=26, verbose_name='شماره شبا')),
                ('coins', models.IntegerField(default=0, verbose_name='سکه\u200cها')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
