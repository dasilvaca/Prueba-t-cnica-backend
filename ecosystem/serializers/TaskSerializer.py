from rest_framework import serializers
from ecosystem.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        def create(self, validated_data):
            return Task.objects.create(**validated_data)