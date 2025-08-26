from django.shortcuts import render
from .models import UserProfile
from rest_framework import generics
from .serializers import UserProfileSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def contact(request):
    name = (request.data.get('name') or '').strip()
    email = (request.data.get('email') or '').strip().lower()
    message = (request.data.get('message') or '').strip()

    if not name or not email or not message:
        return Response({
            'success': False,
            'message': 'name, email, and message are required.'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Upsert في قاعدة البيانات
    user_profile, created = UserProfile.objects.get_or_create(
        email=email,
        defaults={'name': name, 'message': message}
    )

    if not created:
        user_profile.name = name
        user_profile.message = message
        user_profile.save()

    # إرسال الإيميل على Gmail
    try:
        full_message = f"From: {name} <{email}>\n\n{message}"
        send_mail(
            subject=f"New message from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
    except Exception as e:
        return Response({
            'success': False,
            'message': f"Message saved but failed to send email: {str(e)}"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({
        'success': True,
        'message': 'Message saved and email sent successfully.' if created else 'Message updated and email sent successfully.'
    }, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
