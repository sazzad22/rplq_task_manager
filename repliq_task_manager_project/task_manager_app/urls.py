from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserRegistrationView,UserLoginView,company_view,employee_view

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('companies/', company_view, name='company-list'),
    path('companies/<int:pk>/', company_view, name='company-detail'),
    path('employees/', employee_view),
    path('employees/<int:pk>/', employee_view),
]