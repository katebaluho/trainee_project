from copy import deepcopy

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, password, name=name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return f'CustomUser {self.name} {self.email}'

    @property
    def desctription(self):
        instance_info = deepcopy(self.__dict__)
        delete_key = ('password', '_state')
        [instance_info.pop(key) for key in delete_key]
        return [elem for elem in instance_info.values()]


