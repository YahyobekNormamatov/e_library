from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import UserModel
from .serializer import UserSerializer

class UserView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
