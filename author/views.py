from django.shortcuts import render
from rest_framework import generics
from .models import AuthorModel
from .serializer import AuthorSerializers

# Create your views here.

class AllCreateAuthorView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers

class RUDAuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers