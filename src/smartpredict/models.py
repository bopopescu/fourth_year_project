import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class UserDetails(models.Model):
    #userid = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    forex_api = models.CharField(max_length=300)
    date_added = models.DateTimeField('Date person was added')
    def __str__(self):
        stri = str(self.first_name)
        return stri
    def was_added_recently(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)

class Currency(models.Model):
    EURO = 'EUR'
    DOLLAR = 'USD'
    POUND = 'GBP'
    CURRENCY_CHOICES = (
        (EURO, 'Euro'),
        (DOLLAR, 'US Dollar'),
        (POUND, 'GB Pound'),
    )
    currency = models.CharField(
        max_length=10,
        choices=CURRENCY_CHOICES,
        default=EURO,
    )
    def choice(self):
        #Currency.save(force_insert=False, force_update=False, using=DEFAULT_DB_ALIAS, update_fields=None)
        return self.currency