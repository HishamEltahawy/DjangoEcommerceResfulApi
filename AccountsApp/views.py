from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SzSignup
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def register(request):
    data = request.data
    serializer = SzSignup(data = data)
    if serializer.is_valid():
        if not User.objects.filter(email=data['email']).exists():
            serializer = User.objects.create(
                username = data['username'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = make_password(data['password']), # Use make_password library to encrypt password
                )
            return Response({'details':'Add User Successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'details':'This Account Is Exist'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = SzSignup(request.user)
    usernameget = serializer.data
    usernameget = usernameget['username']
    
    return Response({'details':f'Hello {usernameget} your are already Conncted'})