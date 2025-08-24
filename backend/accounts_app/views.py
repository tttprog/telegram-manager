from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status, response

from django.contrib.auth.hashers import make_password

from django.contrib.auth import get_user_model
from accounts_app.serializers import UserRegisterationSerializer

# Create your views here.


@api_view(["POST"])
def user_registration_api_view(request):
    data = request.data
    serializer = UserRegisterationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return response.Response(
            data={"message": "User Registered Successfully."},
            status=status.HTTP_201_CREATED,
        )
    else:
        return response.Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
