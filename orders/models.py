from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'))

    is_paid = models.BooleanField(default=True)

    first_name = models.CharField(max_length=100, verbose_name=_('name'))
    last_name = models.CharField(max_length=100, verbose_name=_('family'))
    phone_number = models.CharField(max_length=11, verbose_name=_('phone number'))
    address = models.CharField(max_length=700, verbose_name=_('address'))
    order_notes = models.CharField(max_length=700, verbose_name=_('note'))

    datetime_created = models.DateTimeField(auto_now=True, verbose_name=_('time create'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('time modified'))

    def __str__(self):
        return f' order{self.id}'
