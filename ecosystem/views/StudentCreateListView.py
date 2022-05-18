from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import StudentSerializer
from ecosystem.models import Student


class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

 
