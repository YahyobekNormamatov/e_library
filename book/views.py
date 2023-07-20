from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404
from .models import BookModel,AuthorModel
from rest_framework.response import Response
from rest_framework import generics
from .serializer import BookSerializer, AuthorSerializer
# Create your views here.



class RUDBookrView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = BookSerializer


class AllCreateBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer