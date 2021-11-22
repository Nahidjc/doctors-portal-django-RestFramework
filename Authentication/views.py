from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from Authentication.models import Account
from .serializers import RegistrationSerializer
# Create your views here.


@api_view(['POST', ])
@permission_classes((permissions.AllowAny,))
def registration_view(request):

    if request.method == "POST":
        print('request')
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            print("Valid")
            account = serializer.save()
            print(account)
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data['error'] = serializer.errors
        return Response(data)
