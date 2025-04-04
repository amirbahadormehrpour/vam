# referral/serializers.py
from rest_framework import serializers
from .models import ReferralCode,ReferralInvitation

class ReferralCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralCode
        fields = ['id', 'user', 'code', 'invited_count']
        
class ReferralInvitationSerializer(serializers.ModelSerializer):
    referrer = serializers.StringRelatedField(source='referrer.phone_number', read_only=True)
    invited_user = serializers.StringRelatedField(source='invited_user.phone_number', read_only=True)
    referral_code = serializers.StringRelatedField(source='referral_code.code', read_only=True)

    class Meta:
        model = ReferralInvitation
        fields = ['id', 'referrer', 'invited_user', 'referral_code', 'created_at']
        read_only_fields = ['referrer', 'invited_user', 'referral_code', 'created_at']