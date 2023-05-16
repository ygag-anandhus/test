import django.urls
from .views import UserRegistration

urlpatterns = [
    django.urls.path('', UserRegistration.as_view(), name='user_register')
]
