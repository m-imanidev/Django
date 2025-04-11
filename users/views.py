import random
import uuid

from django.core.cache import cache
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User, Device
from utils.validators import validate_phone_number

@permission_classes([AllowAny])
class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response(status=400)
        
        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({'detail': 'User already registered!'}, status=400)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)

        # user, created = User.objects.get_or_create(phone_number=phone_number)
            
        
        device = Device.objects.create(user=user)

        code = random.randint(10000, 99999)


        #cache
        cache.set(str(phone_number), code, 2 * 60)

        return Response({'code': code})


@permission_classes([AllowAny])
class GetTokenView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))

        if code != cached_code:
            return Response({'status': 'code is invalid'},status=403)
        
        token = str(uuid.uuid4())

        return Response({'token': token})
    

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
            # return render(request, 'login/login.html')

    return render(request, 'login/login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        phone_number= request.POST['phonenumber']


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')


        try:
            is_user = User.objects.get_by_phone_number(phone_number)
            if is_user:
                messages.error(request, 'User already exists')
                return redirect('login')
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, phone_number=phone_number, password=password)
            messages.success(request, 'User registered successfully')
            return redirect('login')

    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    user = request.user
    condition = None
    message = None
    

    if request.method == "POST":
        #Account Information
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()


        #Change password
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        
        if password is not None:
            if user.check_password(password):
                if new_password:
                    user.set_password(new_password)
                    message = 'Password updated successfully!'
                    condition = "success"
                else:
                    message = "New password cannot be empty."
                    condition = "warning"
            
            else:
                condition = 'danger'
                message = 'password is incorrect'

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # return redirect('profile')


    username = user.username
    phone_number = user.phone_number
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    
    return render(request, "my-account.html", {'username_placeholder': username, 'phone_number_placeholder': phone_number,
                                                'firstname_placeholder': first_name, 'lastname_placeholder': last_name,
                                                'email_placeholder': email, 'status': condition , 'message': message,
                                                'alert_message': condition is not None,
                                                })

def login_phone_number(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        password = request.POST.get('password')
        phone_number = request.POST.get('phonenumber')
        if phone_number is not None:
            try:
                print(phone_number)
                validate_phone_number(phone_number)
            except:
                messages.error(request, 'Invalid input')
                return render(request, 'login/login-phone-number.html')

        try:
            user = User.objects.get_by_phone_number(phone_number)
            print(user)
            if password is not None:
                is_user = authenticate(request, username = user.username, password = password)
                if is_user is not None:
                    login(request, is_user)
                    return redirect('home')
                else:
                    messages.error(request, 'password is incorrect')
                    return render(request, 'login/login-password.html')
            return render(request, 'login/login-password.html')
        #register
        except User.DoesNotExist:
            messages.success(request, 'Mobile number not used')
            return render(request, 'login/login-phone-number.html')

    return render(request, 'login/login-phone-number.html')