from rest_framework import serializers
from ecosystem.models import TaskSubmission

class TaskSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSubmission
        fields = ['task', 'student', 'submission_date', 'submission_file']