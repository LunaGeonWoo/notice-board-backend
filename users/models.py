from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, name, password=None):
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password=None):
        user = self.create_user(
            username,
            name=name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()

    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="User Name",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="이름",
    )
    email = models.EmailField(
        blank=True,
        verbose_name="이메일",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name
