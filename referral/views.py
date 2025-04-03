# referral/views.py
from rest_framework import generics
from .models import ReferralCode
from .serializers import ReferralCodeSerializer

class ReferralCodeListCreateView(generics.ListCreateAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer

class ReferralCodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer