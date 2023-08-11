from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

from .serializers import CustomUserSerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            return Response({
                'userid': user.id,
                'access_token': access_token,
                'refresh_token': str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to log in

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({
                    'userid': user.id,
                    'access_token': access_token,
                    'refresh_token': str(refresh),
                },status=status.HTTP_200_OK)

            return Response({
                    'message':'unauthorized'
                },status=status.HTTP_200_OK)