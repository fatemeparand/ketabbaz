from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=False, null=True, unique=True, verbose_name=_('phone number',))
