from django.urls import path

from .views import (RegisterView, GetTokenView , login_view, 
                    logout_view, register_view, profile_view,
                    )



urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),



    path('registers/', RegisterView.as_view()),
    path('get_token/', GetTokenView.as_view()),
]
