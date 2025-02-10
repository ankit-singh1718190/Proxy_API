from django.conf import settings 
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields if necessary
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

class ResidentialIP(models.Model):
    ip_address = models.GenericIPAddressField(protocol='both', unique=True)  # Supports IPv4 & IPv6
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address

class ProxyUsage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use dynamic user model
    ip_address = models.ForeignKey(ResidentialIP, on_delete=models.CASCADE)
    usage_start = models.DateTimeField(auto_now_add=True)
    usage_end = models.DateTimeField(null=True, blank=True)
    data_transferred = models.FloatField(default=0)  # in MB

    def __str__(self):
        return f"{self.user} - {self.ip_address}"
