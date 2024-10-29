from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
# from .views import SendOTPView, VerifyOTPView


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    # path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    # path("about/", include("apps.about.urls")),
    # path("users/", include("apps.users.urls")),
]
# ]



