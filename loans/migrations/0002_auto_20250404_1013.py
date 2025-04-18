# Generated by Django 3.2.16 on 2025-04-04 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_auto_20250404_1013'),
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='installment',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='installment_payments', to='wallet.transaction'),
        ),
        migrations.AddField(
            model_name='loan',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='promissorynote',
            name='loan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promissory_notes', to='loans.loan'),
        ),
    ]
