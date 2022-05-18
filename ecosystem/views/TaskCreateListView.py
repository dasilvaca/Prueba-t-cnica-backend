from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import TaskSerializer
from ecosystem.models import Task


class TaskCreateListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
