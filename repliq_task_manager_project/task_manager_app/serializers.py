from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser, Company


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'company_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        company_name = validated_data.pop('company_name')
        
        
        user = CustomUser.objects.create(**validated_data)
        return user
    

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name', 'location', 'contact_info']
        read_only_fields = ['id']