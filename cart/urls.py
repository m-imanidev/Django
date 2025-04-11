from django.urls import path
from .views import (cart_detail, cart_add, cart_remove)

urlpatterns = [
    path('', cart_detail, name="cart"),
    path("cart/add/", cart_add, name="cart_add"),
    path("cart/remove/", cart_remove, name="cart_remove"),
]
