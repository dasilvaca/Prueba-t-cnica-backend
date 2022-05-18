from django.shortcuts import render
from rest_framework import generics
from ecosystem.serializers import TeacherSerializer
from ecosystem.models import Teacher


class TeacherCreateListView(generics.ListCreateAPIView):
    # queryset = Teacher().objects.all()
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            # return render(request, 'ecosystem/task_create_list_view.html', {'serializer': serializer})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return self.create(request, *args, **kwargs)
