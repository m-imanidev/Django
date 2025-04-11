from django.db import models

from users.models import User
from cart.models import Cart

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    shipping_method = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    discount_code = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.cart.items.all())

    def __str__(self):
        return f"Order {self.id} - {self.full_name}"
