from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from todo.models import ToDoListItem
from todo.serializers import UserSerializer, ToDoItemSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoListItem.objects.all()
    serializer_class = ToDoItemSerializer