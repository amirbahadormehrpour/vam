# referral/views.py
from rest_framework import generics ,permissions
from .models import ReferralCode
from .serializers import ReferralCodeSerializer,ReferralInvitationSerializer,ReferralInvitation

class ReferralCodeListCreateView(generics.ListCreateAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer

class ReferralCodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReferralCode.objects.all()
    serializer_class = ReferralCodeSerializer
    
    # referral/views.py
class ReferralInvitationListView(generics.ListAPIView):
    serializer_class = ReferralInvitationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReferralInvitation.objects.filter(referrer=self.request.user)