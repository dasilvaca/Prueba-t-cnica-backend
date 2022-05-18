from rest_framework import serializers
from ecosystem.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'# ('id', 'name', 'description', 'created_at', 'updated_at', 'deadline', 'course')