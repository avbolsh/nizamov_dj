from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    snils = models.CharField(max_length=14, unique=True, verbose_name="СНИЛС", blank=False)
    birthday = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    inn = models.CharField(max_length=12, verbose_name="ИНН", blank=True)
