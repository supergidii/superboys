from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here


class Profile(AbstractUser):
    phone_number=PhoneNumberField(max_length=13, unique=True,blank=False)

