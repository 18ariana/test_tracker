from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

class Activity(models.Model):

    start_time = models.DateTimeField(verbose_name="Дата и время начала активности")
    finish_time = models.DateTimeField(verbose_name="Дата и время окончания активности")
    ACTIVITY_TYPE_CHOICES = {
        ("1", "Бег"),
        ("2", "Ходьба"),
        ("3", "Велосипед")
    }
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPE_CHOICES, verbose_name="Тип активности")
    distance = models.FloatField(verbose_name="Расстояние")
    calories_amount = models.IntegerField(verbose_name="Количество калорий")
    user = models.ForeignKey('FitnessUser', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.start_time.date(), self.get_activity_type_display())
    
    class Meta():
        verbose_name = "Активность"
        verbose_name_plural = "Активность"

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None):

        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):

        if not email:
            raise ValueError("User must have an email")

        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None):

        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user

class FitnessUser(AbstractBaseUser):
    ADMIN = 'admin'
    STAFF = 'staff'
    STATUS = [
        (ADMIN, 'Admin User'),
        (STAFF, 'Staff User'),
    ]
    email = models.EmailField('email address', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    def __str__(self):
        return "{}".format(self.email)