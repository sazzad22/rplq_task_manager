from django.urls import path
from .views import assignments

urlpatterns = [
    path('assignments/', assignments),
    path('assignments/<int:pk>/', assignments),
    # Other URL patterns for your app
]