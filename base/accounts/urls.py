from django.urls import path, include
from .views import UserRegistration

urlpatterns = [
    path('', UserRegistration.as_view(), name='user_register')
]
