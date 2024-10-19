from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from list.serializers import TaskSerializer
from list.models import Task
from rest_framework import status
from rest_framework.response import Response


class TaskAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        completed = serializer.validated_data.get('completed')


        task = Task.objects.create(title=title,
                                   description=description,
                                   completed=completed,
                                   )

        return Response(data={'task_id': task.id},
                        status=status.HTTP_201_CREATED)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        task = Task.objects.filter(id=kwargs['id']).first()
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task.title = serializer.validated_data.get('title')
        task.description = serializer.validated_data.get('description')
        task.completed = serializer.validated_data.get('completed')
        task.save()

        return Response(data=TaskSerializer(task).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        task = Task.objects.get(id=kwargs['id'])
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
