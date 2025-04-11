from django.urls import path

from .views import (RegisterView, GetTokenView , login_view, 
                    logout_view, register_view, profile_view,
                    login_phone_number
                    )



urlpatterns = [
    path('login/', login_view, name='login'),
    path('login2/', login_phone_number, name='phonenumber'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),



    path('registers/', RegisterView.as_view()),
    path('get_token/', GetTokenView.as_view()),
]
