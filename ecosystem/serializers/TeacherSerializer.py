from rest_framework import serializers
from ecosystem.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        def create(self, validated_data):
            return Task.objects.create(**validated_data)