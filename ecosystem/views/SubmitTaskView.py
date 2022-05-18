from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import TaskSubmissionSerializer
from ecosystem.models import TaskSubmission


class SubmitTaskView(generics.ListCreateAPIView):
    queryset = TaskSubmission.objects.all()
    serializer_class = TaskSubmissionSerializer