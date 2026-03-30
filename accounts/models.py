from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_SELLER = 'seller'
    ROLE_BUYER = 'buyer'

    ROLE_CHOICES = [
        (ROLE_SELLER, 'Seller'),
        (ROLE_BUYER, 'Buyer'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_BUYER)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def is_seller(self):
        return self.role == self.ROLE_SELLER

    def is_buyer(self):
        return self.role == self.ROLE_BUYER

    def __str__(self):
        return f"{self.username} ({self.role})"
