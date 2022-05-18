from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import StudentSerializer
from ecosystem.models import Student


class StudentCreateListView(generics.ListCreateAPIView):
    # queryset = Teacher().objects.all()
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    #         # return render(request, 'ecosystem/task_create_list_view.html', {'serializer': serializer})
    #     return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # return self.create(request, *args, **kwargs)

