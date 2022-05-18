from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import GradeSubmissionSerializer
from ecosystem.models import TaskSubmission


class GradeTaskView(generics.RetrieveUpdateAPIView):
    queryset = TaskSubmission.objects.all()
    serializer_class = GradeSubmissionSerializer