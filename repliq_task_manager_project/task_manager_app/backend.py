from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        
        try:
            user = CustomUser.objects.get(email=email)
            print(user)
            if user.check_password(password):
                return user
            return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        

        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
