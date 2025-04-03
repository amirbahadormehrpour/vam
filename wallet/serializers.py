# wallet/serializers.py
from rest_framework import serializers
from accounts.models import CustomUser
from .models import Transaction, Wallet

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'receiver', 'amount', 'transaction_type', 'date', 'status']
        read_only_fields = ['sender', 'date', 'status']

class TransferSerializer(TransactionSerializer):
    receiver = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=True)
    
    def validate(self, data):
        if data.get('transaction_type') != 'transfer':
            raise serializers.ValidationError({'transaction_type': 'نوع تراکنش باید "transfer" باشد'})
        return data

class SelfDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'amount', 'transaction_type', 'date', 'status']
        read_only_fields = ['sender', 'date', 'status','transaction_type']

    def validate_transaction_type(self, value):
        if value != 'deposit':
            raise serializers.ValidationError('نوع تراکنش باید "deposit" باشد')
        return value

class AdminDepositSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
            queryset=CustomUser.objects.all(),  # لیست کاربران از اینجا میاد
            write_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'sender', 'user_id', 'amount', 'transaction_type', 'date', 'status']
        read_only_fields = ['sender', 'date', 'status', 'transaction_type']

    def validate_transaction_type(self, value):
        if value != 'deposit':
            raise serializers.ValidationError('نوع تراکنش باید "deposit" باشد')
        return value

    def create(self, validated_data):
        # user_id رو از validated_data حذف کن و تراکنش رو بساز
        validated_data.pop('user_id', None)  # user_id رو بردار
        return Transaction.objects.create(**validated_data)
    
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'balance']
        read_only_fields = ['user']


class TransferSerializer(TransactionSerializer):
    transaction_type = serializers.ChoiceField(choices=[('transfer', 'انتقال')], default='transfer')

class DepositSerializer(TransactionSerializer):
    transaction_type = serializers.ChoiceField(choices=[('deposit', 'شارژ')], default='deposit')