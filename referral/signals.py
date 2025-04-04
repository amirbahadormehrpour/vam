from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import ReferralCode
import uuid


from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import ReferralCode, ReferralInvitation

@receiver(post_save, sender=CustomUser)
def create_referral_code(sender, instance, created, **kwargs):
    if created:
        ReferralCode.objects.create(user=instance, code=generate_unique_code())
    if created and instance.referred_by_code:
        try:
            referral = ReferralCode.objects.get(code=instance.referred_by_code)
            ReferralInvitation.objects.create(
                referrer=referral.user,
                invited_user=instance,
                referral_code=referral
            )
            referral.invited_count += 1
            referral.save()
        except ReferralCode.DoesNotExist:
            pass  # اگه کد رفرال اشتباه باشه، نادیده بگیر

def generate_unique_code():
    while True:
        code = str(uuid.uuid4())[:8]
        if not ReferralCode.objects.filter(code=code).exists():
            return code