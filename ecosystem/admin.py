from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Task)
admin.site.register(CourseMembers)
admin.site.register(TaskSubmission)
