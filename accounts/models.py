from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_user = models.BooleanField(default=True)
    is_editor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'