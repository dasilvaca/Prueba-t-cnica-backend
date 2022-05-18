"""PruebaTécnicaBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from ecosystem.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerTeacher',TeacherCreateListView.as_view()),
    path('registerStudent',StudentCreateListView.as_view()),
    path('createCourse',CourseCreateListView.as_view()),
    path('inscribeStudent',InscribeStudentIntoCourse.as_view()),
    path('createTask',TaskCreateListView.as_view()),
    path('submitTask',SubmitTaskView.as_view()),
    path('editTask/<int:id>',TaskRetrieveUpdateDestroyView.as_view()),
    path('gradeTask/<int:pk>',GradeTaskView.as_view()),
    path('editSubmission/<int:pk>',EditSubmission.as_view()),
    path('showSubmission/<int:pk>',ShowSubmissionView.as_view()),
]