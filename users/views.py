from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.schemas.coreapi import is_custom_action
from .serializers import UserCreateSerializer, UserAuthSerializers, UserConfirmSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    # username = serializer.validated_data['username']
    # password = serializer.validated_data['password']
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ =Token.objects.get_or_create(user=user)
        # try:
        #     token = Token.objects.get(user=user)
        # except:
        #     token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'ОШИБКА'})




@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # username = serializer.validated_data['username']
    # password = serializer.validated_data['password']
    user = User.objects.create_user(**serializer.validated_data, is_active=False)
    return Response(data = {'user_id': user.id}, status=201)


@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    if serializer.is_valid():
        return Response({"message": "User confirmed successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)