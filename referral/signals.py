from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import ReferralCode
import uuid

@receiver(post_save, sender=CustomUser)
def create_referral_code(sender, instance, created, **kwargs):
    if created:
        ReferralCode.objects.create(user=instance, code=generate_unique_code())
        
def generate_unique_code():
    return str(uuid.uuid4())[:8]