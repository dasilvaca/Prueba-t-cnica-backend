from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import CourseSerializer
from ecosystem.models import Course


class CourseCreateListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer