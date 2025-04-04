# wallet/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import serializers
from .models import Wallet, Transaction
from .serializers import (
    WalletSerializer, TransactionSerializer,
    TransferSerializer, SelfDepositSerializer, AdminDepositSerializer
)
from accounts.models import CustomUser
from decimal import Decimal
from notifications.models import Notification


class WalletListCreateView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransferView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransferSerializer

    def perform_create(self, serializer):
        sender_wallet = self.request.user.wallet
        receiver_id = self.request.data.get('receiver')
        try:
            receiver_id = int(receiver_id)
            receiver = CustomUser.objects.get(id=receiver_id)
            receiver_wallet = receiver.wallet
        except (ValueError, TypeError):
            raise serializers.ValidationError({'receiver': 'شناسه گیرنده نامعتبر است'})
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'error': 'گیرنده پیدا نشد'})

        if self.request.user.id == receiver_id:
            raise serializers.ValidationError({'error': 'شما نمی‌توانید به خودتان انتقال دهید'})

        amount = Decimal(self.request.data.get('amount'))
        if sender_wallet.balance < amount:
            raise serializers.ValidationError({'error': 'موجودی کافی نیست'})

        sender_wallet.balance -= amount
        receiver_wallet.balance += amount
        sender_wallet.save()
        receiver_wallet.save()

        serializer.save(sender=self.request.user, receiver=receiver, amount=amount, transaction_type='transfer')

        # ارسال نوتیفیکیشن
        Notification.objects.create(
            user=self.request.user,
            message=f"شما {amount} تومان به {receiver.phone_number} منتقل کردید"
        )
        Notification.objects.create(
            user=receiver,
            message=f"{self.request.user.phone_number} مبلغ {amount} تومان به شما منتقل کرد"
        )
        # return Response({'message': 'انتقال با موفقیت انجام شد'}, status=status.HTTP_201_CREATED)
    
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            receiver = CustomUser.objects.get(id=request.data.get('receiver'))
            amount = Decimal(request.data.get('amount'))
            response.data = {'message': f'{amount} تومان به {receiver.phone_number} منتقل شد'}
            return response
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class SelfDepositView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SelfDepositSerializer

    def perform_create(self, serializer):
        wallet = self.request.user.wallet
        amount = Decimal(self.request.data.get('amount'))
        wallet.balance += amount
        wallet.save()

        serializer.save(sender=self.request.user, amount=amount, transaction_type='deposit')

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            amount = Decimal(request.data.get('amount'))
            response.data = {'message': f'کیف پول شما با {amount} تومان شارژ شد'}
            return response
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)


class AdminDepositView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = AdminDepositSerializer

    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id')
        if not user_id:
            raise serializers.ValidationError({'error': 'شناسه کاربر لازم است'})

        try:
            target_user = CustomUser.objects.get(id=user_id)
            wallet = target_user.wallet
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({'error': 'کاربر پیدا نشد'})

        amount = Decimal(self.request.data.get('amount'))
        wallet.balance += amount
        wallet.save()

        serializer.save(sender=self.request.user, amount=amount, transaction_type='deposit')

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            target_user = CustomUser.objects.get(id=request.data.get('user_id'))
            amount = Decimal(request.data.get('amount'))
            response.data = {'message': f'کیف پول {target_user.phone_number} با {amount} تومان شارژ شد'}
            return response
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)