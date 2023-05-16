from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
#test cooment

# another change