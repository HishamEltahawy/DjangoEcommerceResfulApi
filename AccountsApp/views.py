from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SzSignup, SzUsers
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from datetime import datetime, timedelta
from .models import Profile


# SignUp
@api_view(['POST'])
def register(request):
    data = request.data
    serializer = SzSignup(data=data)
    if serializer.is_valid():
        if not User.objects.filter(email=data['email']).exists():
            user = User.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=make_password(data['password']),  # Use make_password library to encrypt password
            )
            # Ensure a profile is created for the user
            user.profile = Profile.objects.create(user=user)
            return Response({'details': 'Add User Successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'details': 'This Account Is Exist'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = SzUsers(request.user)
    usernameget = serializer.data
    usernameget = usernameget['username']
    
    return Response({'details':serializer.data})

# Update user details
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['username']
    user.email = data['email']

    if data['password'] != "":
        user.password = make_password(data['password'])
    
    user.save()
    serializer = SzUsers(user, many=False)
    return Response(serializer.data)


def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return '{protocol}://{host}/'.format(protocol=protocol, host = host)

# Forget password
@api_view(['POST'])
def forget_password(request):
    data = request.data
    user = get_object_or_404(User, email=data['email']) # all fields about this user (id, username, password, ...)
    
    generate_token = get_random_string(40)
    token_ex_date = datetime.now() + timedelta(minutes=30)
    user.profile.new_token = generate_token
    user.profile.ex_date = token_ex_date
    user.profile.save()
    
    link = 'http://127.0.0.1:8000/api/accounts/reset_password/{generate_token}'.format(generate_token=generate_token)
    body = 'Your password-reset link is {link}'.format(link=link)
    
    send_mail(
        'Password reset from hisham',
        body,
        'hishameltahawy555@gmail.com',
        [data['email']]
    )
    return Response({'details': 'Password reset link sent to email: {email}'.format(email=data['email'])})


# Reset password
@api_view(['POST'])
def reset_password(request, token):
    data = request.data
    user = get_object_or_404(User, profile__new_token=token)  # all fields about this user (id, username, password, ...)
    
    if user.profile.ex_date is None or user.profile.ex_date.replace(tzinfo=None) < datetime.now():
        return Response({'error': 'Token is expired'}, status=status.HTTP_400_BAD_REQUEST)
    
    if data['password'] != data['confirmPassword']:
        return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

    # Make token and its expire date empty to never user or anyone use this api again without call forget password 
    user.password = make_password(data['password'])
    user.profile.new_token = ""
    user.profile.ex_date = None
    
    user.profile.save()
    user.save()
    return Response({'result': 'Password changed successfully.'}, status=status.HTTP_200_OK)
  
