from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import ToDoListItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class ToDoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDoListItem
        fields = ('text', 'completed', 'date', 'userid')