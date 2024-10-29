# serializers.py
from rest_framework import serializers
from .models import Course, Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_file', 'duration', 'order']

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)  # Kurs ichidagi videolar

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'duration', 'videos', 'created_at', 'updated_at']
