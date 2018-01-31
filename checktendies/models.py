from django.db import models
from django.core.validators import RegexValidator

# source: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
class PhoneModel(models.Model):
    ...
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list