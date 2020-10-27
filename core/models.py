from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext as _
import uuid
import os


class UserManager(BaseUserManager):
    """
        Manager for UserProfiles
    """

    def create_user(self, email, password=None, **extrac_fields):
        """Create and save a new user"""

        if not email:
            raise ValueError("User must have email")

        email = self.normalize_email(email)

        user = self.model(email=email, **extrac_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extrac_fields):
        """ Create and save a new superuser"""

        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Model for users in the system that use email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user"""
        return self.name

    def __str__(self):
        """ String representation"""

        return self.email


class Account(models.Model):

    CUC = 'CUC'
    CUP = 'CUP'
    USD = 'USD'

    TIPOS = [
        (CUC, 'CUC'),
        (CUP, 'CUP'),
        (USD, 'USD'),
        (None, _('Seleccione tipo de moneda'))
    ]

    type = models.TextField(choices=TIPOS, unique=True)
    balance = models.PositiveIntegerField()

    def __str__(self):

        return self.type


class Action(models.Model):

    ING = 1
    RET = 0

    ACTIONS = [
        (ING, _('Ingresar')),
        (RET, _('Retirar')),
        (None, _('Seleccione acción'))
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    account = models.ForeignKey(Account, on_delete=CASCADE)
    amount = models.PositiveIntegerField()
    act = models.TextField(choices=ACTIONS)
    reason = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):

        if bool(self.act):
            return 'Ingresado una cantidad de ' + str(self.amount)
        return 'Retirado una cantidad de ' + str(self.amount)
