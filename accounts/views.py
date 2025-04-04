# accounts/views.py
from rest_framework import generics
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from accounts.models import CustomUser

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        
        print("Received phone_number:", phone_number)
        print("Received password:", password)

        if not phone_number or not password:
            return Response({'error': 'شماره تلفن و رمز عبور لازم است'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(phone_number=phone_number)
            print("User found:", user.phone_number)
            print("Stored password hash:", user.password)
            print("Password check result:", user.check_password(password))
        except CustomUser.DoesNotExist:
            return Response({'error': 'کاربری با این شماره تلفن وجود ندارد'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'error': 'رمز عبور اشتباه است'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'ورود با موفقیت انجام شد'}, status=status.HTTP_200_OK)
    
class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer