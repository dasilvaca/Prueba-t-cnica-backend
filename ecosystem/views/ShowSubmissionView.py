from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import GradeSubmissionSerializer
from ecosystem.models import TaskSubmission
from rest_framework.response import Response
from rest_framework import status
# import FileWrapper
from django.http import FileResponse
from django.http import HttpResponse

class ShowSubmissionView(generics.GenericAPIView):
    # queryset = Teacher().objects.all()
    queryset = TaskSubmission.objects.all()
    serializer_class = GradeSubmissionSerializer

    def get(self, request, *args, **kwargs):
        files = TaskSubmission.objects.get(pk=kwargs['pk']).submission_file  
        response = FileResponse(files)
        return response
