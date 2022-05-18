from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import TeacherSerializer
from ecosystem.models import Teacher


class TeacherCreateListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
