# Generated by Django 3.2.16 on 2025-03-31 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferralCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='کد رفرال')),
                ('invited_count', models.IntegerField(default=0, verbose_name='تعداد دعوت\u200cشده\u200cها')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='referral_code', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
