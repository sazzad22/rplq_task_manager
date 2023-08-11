from rest_framework import serializers
from .models import Assignments

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        fields = '__all__'