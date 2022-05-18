from rest_framework import serializers
from ecosystem.models import CourseMembers

class CourseMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMembers
        fields = '__all__'