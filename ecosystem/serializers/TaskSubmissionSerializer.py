from rest_framework import serializers
from ecosystem.models import TaskSubmission

class TaskSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSubmission
        fields = '__all__'