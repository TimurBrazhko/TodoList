from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    completed = serializers.BooleanField()
