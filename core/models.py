from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *

# Create your models here.


class MyUser(AbstractUser):
    name = models.TextField(max_length=50)
    dob = models.DateField()
    gender = models.TextField()
    email = models.EmailField(unique=True)
    password = models.TextField()
    no = models.IntegerField(unique=True)
    address = models.TextField()
    state = models.TextField()
    education = models.TextField()
    username = models.TextField(unique=False)
    image = models.ImageField(upload_to="user_img/")
    resume = models.FileField(upload_to="user_resume/", null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "dob", "no"]


class Jobs(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.TextField()
    skill = models.TextField()
    duration = models.TextField()
    salary = models.IntegerField()
    deadline = models.DateField()
    vacancy = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
