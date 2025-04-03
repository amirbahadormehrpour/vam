# referral/serializers.py
from rest_framework import serializers
from .models import ReferralCode

class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ['id', 'user', 'code', 'invited_count']