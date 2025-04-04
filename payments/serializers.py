# payments/serializers.py
from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'status', 'gateway_ref', 'created_at']
        read_only_fields = ['user', 'status', 'gateway_ref', 'created_at']