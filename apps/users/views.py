from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
# from .utils import generate_otp, send_otp_via_eskiz


# @method_decorator(cache_page(60*15), name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

# views.py
from rest_framework import status
# from .utils import send_otp_via_eskiz, generate_otp
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# class SendOTPView(APIView):
#     def post(self, request):
#         phone_number = request.data.get("phone_number")
#         otp = generate_otp()
#         result = send_otp_via_eskiz(phone_number, otp)
#         if result and result.get("status") == "success":
#             r.setex(f"otp:{phone_number}", 300, otp)  # OTP’ni 5 daqiqa saqlash
#             return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)
#         return Response({"message": "Failed to send OTP"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# views.py davomida
class VerifyOTPView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        otp = request.data.get("otp")
        stored_otp = r.get(f"otp:{phone_number}")

        if stored_otp and int(stored_otp) == int(otp):
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

