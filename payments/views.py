# payments/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from wallet.models import Wallet, Transaction
import requests

class PaymentRequestView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        payment = Payment.objects.create(user=request.user, amount=amount)

        # درخواست به زرین‌پال
        data = {
            "merchant_id": "your-merchant-id",
            "amount": int(amount * 10),  # به ریال
            "description": f"شارژ کیف پول {request.user.phone_number}",
            "callback_url": "http://yourdomain.com/api/payments/verify/",
        }
        response = requests.post("https://api.zarinpal.com/pg/v4/payment/request.json", json=data)
        result = response.json()

        if result['data']['code'] == 100:
            payment.gateway_ref = result['data']['authority']
            payment.save()
            return Response({"url": f"https://www.zarinpal.com/pg/StartPay/{payment.gateway_ref}"}, status=status.HTTP_200_OK)
        else:
            payment.status = 'failed'
            payment.save()
            return Response({"error": "خطا در اتصال به درگاه"}, status=status.HTTP_400_BAD_REQUEST)

class PaymentVerifyView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        payment = Payment.objects.get(gateway_ref=authority)

        if status == 'OK':
            verify_data = {
                "merchant_id": "your-merchant-id",
                "authority": authority,
                "amount": int(payment.amount * 10),
            }
            response = requests.post("https://api.zarinpal.com/pg/v4/payment/verify.json", json=verify_data)
            result = response.json()

            if result['data']['code'] == 100:
                payment.status = 'success'
                payment.save()
                wallet = payment.user.wallet
                wallet.balance += payment.amount
                wallet.save()
                Transaction.objects.create(
                    sender=payment.user,
                    amount=payment.amount,
                    transaction_type='deposit',
                    status='success',
                    reference_id=result['data']['ref_id']
                )
                return Response({"message": "پرداخت موفق بود"}, status=status.HTTP_200_OK)
            else:
                payment.status = 'failed'
                payment.save()
                return Response({"error": "خطا در تایید پرداخت"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            payment.status = 'failed'
            payment.save()
            return Response({"error": "پرداخت لغو شد"}, status=status.HTTP_400_BAD_REQUEST)