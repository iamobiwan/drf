from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email for user must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True)
    phone = models.CharField(max_length=64, verbose_name='Телефон', blank=True)
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="email является логином пользователя")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()