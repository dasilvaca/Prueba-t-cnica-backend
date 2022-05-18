from rest_framework import serializers
from ecosystem.models import TaskSubmission

class GradeSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSubmission
        fields = ['grade']
        read_only_fields = ['task', 'student', 'submission_date', 'submission_file', 'submission']