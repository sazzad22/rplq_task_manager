from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view

from .models import Company
from .serializers import CustomUserSerializer,CompanySerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request, *args, **kwargs):
        data = request.data
        if not data['company_name']:
            return Response({'message':"provide proper company name"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            company = Company.objects.get(name=data['company_name'])
        except company.DoesNotExist:
            return Response({'message':"company not found"}, status=status.HTTP_400_BAD_REQUEST)
        data['company_name'] = company.pk
        
        serializer = CustomUserSerializer(data=data)
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
            


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def company_view(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            try:
                company = Company.objects.get(pk=pk)
                serializer = CompanySerializer(company)
                return Response(serializer.data)
            except Company.DoesNotExist:
                return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'new company created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)