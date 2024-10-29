# urls.py
from django.urls import path
from .views import CourseListCreateAPIView, CourseDetailAPIView, VideoListCreateAPIView

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('courses/<int:course_pk>/videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    # path('upload/', FileUploadView.as_view(), name='file-upload'),

]
