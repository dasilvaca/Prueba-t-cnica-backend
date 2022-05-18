from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import TaskSerializer
from ecosystem.models import Task

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    # def get_object(self):
    #     return Task.objects.get(id=self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        return self.update(request, *args, **kwargs)

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs['id'])