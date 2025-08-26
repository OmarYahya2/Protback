from django.shortcuts import render
from .models import UserProfile
from rest_framework import generics
from .serializers import UserProfileSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def contact(request):
    """
    Minimal DRF endpoint for contact form submissions.
    Upserts by email to avoid unique constraint failures.
    """
    name = (request.data.get('name') or '').strip()
    email = (request.data.get('email') or '').strip().lower()
    message = (request.data.get('message') or '').strip()

    if not name or not email or not message:
        return Response({
            'success': False,
            'message': 'name, email, and message are required.'
        }, status=status.HTTP_400_BAD_REQUEST)

    # Upsert based on unique email
    user_profile, created = UserProfile.objects.get_or_create(
        email=email,
        defaults={'name': name, 'message': message}
    )

    if not created:
        # Update existing record
        if name:
            user_profile.name = name
        user_profile.message = message
        user_profile.save()

    return Response({
        'success': True,
        'message': 'Message saved successfully.' if created else 'Message updated successfully.'
    }, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

