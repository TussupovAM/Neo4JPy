from django.contrib.auth import login
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer
from .models import User

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response(UserSerializer(user).data)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
