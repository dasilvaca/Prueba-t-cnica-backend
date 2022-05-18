from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import CourseMembersSerializer
from ecosystem.models import CourseMembers


class InscribeStudentIntoCourse(generics.ListCreateAPIView):
    queryset = CourseMembers.objects.all()
    serializer_class = CourseMembersSerializer