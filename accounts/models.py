from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None, is_active=True, is_staff=False,
                    is_admin=False, is_client=False):
        if not email:
            raise ValueError('Users must have a email address')
        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user_obj.set_password(password)
        user_obj.client = is_client
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.is_superuser = True
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, first_name=None, last_name=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_client=True,
        )
        return user

    def create_superuser(self, email, first_name=None, last_name=None, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_admin=True,
            is_client=False,
        )
        user.is_superuser = True
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, default='')
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False, null=True)
    admin = models.BooleanField(default=False)
    client = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, default=None,
                              related_name='group')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    # if all user can be access in all modules without permission
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
