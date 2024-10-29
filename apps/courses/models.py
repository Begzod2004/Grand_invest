# models.py
from django.db import models
from django.core.validators import FileExtensionValidator

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in hours")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])])
    duration = models.IntegerField(help_text="Duration in minutes")
    order = models.PositiveIntegerField(help_text="Order of the video in the course")

    def __str__(self):
        return f"{self.title} ({self.course.title})"
