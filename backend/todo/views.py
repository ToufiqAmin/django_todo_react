# The viewsets base class provides the implementation 
# for CRUD operations by default. This code specifies the serializer_class and the queryset.

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()