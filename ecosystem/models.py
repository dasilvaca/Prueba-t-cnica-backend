from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True, primary_key=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.dni

class Course(models.Model):
    CourseID = models.CharField(max_length=10, unique=True, primary_key=True, default='')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.teacher.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.dni

class CourseMembers(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    inscription_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.name + ' - ' + self.student.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(default=None, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class TaskSubmission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submission_file = models.FileField(upload_to='submissions')
    grade = models.IntegerField(default=0)
    # grade_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task.name + " - " + self.student.name