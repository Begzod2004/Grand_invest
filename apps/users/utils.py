# utils.py
import requests
from django.conf import settings

def send_otp_via_eskiz(phone_number, otp):
    url = "https://notify.eskiz.uz/api/message/sms/send"
    headers = {"Authorization": f"Bearer {settings.ESKIZ_API_TOKEN}"}
    data = {
        "mobile_phone": phone_number,
        "message": f"Your verification code is {otp}",
        "from": "4546",
        "callback_url": "http://your-callback-url.com",
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except requests.RequestException as e:
        print("Failed to send OTP:", e)
        return None
