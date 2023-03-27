from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GUEST = 'guest'
    OWNER = 'owner'
    ADMIN = 'admin'
    USER_TYPES = [
        (GUEST, 'guest'),
        (OWNER, 'owner'),
        (ADMIN, 'admin'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default=GUEST)

    def __str__(self):
        return self.username

class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.hotel.name} - {self.user.username}"
