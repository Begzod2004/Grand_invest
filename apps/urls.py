from django.urls import include, path

urlpatterns = [
    path("", include("apps.users.urls")),
    path("Courses", include("apps.courses.urls")),
    # path("about/", include("apps.about.urls")),
    # path("users/", include("apps.users.urls")),
]









