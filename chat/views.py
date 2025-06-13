from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Chat
from django.contrib.auth.hashers import make_password, check_password
import secrets

@api_view(['POST'])
def register(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password required'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        hashed_password = make_password(password)
        user = User.objects.create(username=username, password=hashed_password)
        return Response({'message': 'User registered successfully'}, status=201)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def login_view(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        if not check_password(password, user.password):
            return Response({'error': 'Invalid credentials'}, status=401)
        token = secrets.token_hex(16)
        user.auth_token = token
        user.save()
        return Response({'token': token})
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def chat(request):
    try:
        token = request.headers.get('Authorization', '').replace('Token ', '')
        user = User.objects.get(auth_token=token)
        message = request.data.get('message')
        if not message:
            return Response({'error': 'Message is required'}, status=400)
        if user.tokens < 100:
            return Response({'error': 'Insufficient tokens'}, status=402)

        response_text = f"AI Response to: {message}"
        Chat.objects.create(user=user, message=message, response=response_text)
        user.tokens -= 100
        user.save()
        return Response({'message': message, 'response': response_text})
    except User.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=401)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def get_tokens(request):
    try:
        token = request.headers.get('Authorization', '').replace('Token ', '')
        user = User.objects.get(auth_token=token)
        return Response({'tokens': user.tokens})
    except User.DoesNotExist:
        return Response({'error': 'Invalid token'}, status=401)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
