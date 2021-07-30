from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import allowListEmailValidator

class Account(models.Model):
  username = models.CharField(unique=True, max_length=12)
  password = models.CharField(max_length=255)
  email = models.EmailField(max_length=30, validators=[allowListEmailValidator(allowlist=['gmail.com'])])

  def __str__(self):
    return self.username

  class Meta:
    verbose_name_plural = "User Accounts"
    verbose_name = "User Account"


class Person(models.Model):

  class AvailableCountry(models.TextChoices):
    KAZ = "KAZ", _("Kazakhstan")
    RUS = "RUS", _("Russia")

  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="people", related_query_name="person")
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  country = models.CharField(choices=AvailableCountry.choices, default=AvailableCountry.KAZ)
  city = models.CharField(max_length=15)
  address = models.CharField(max_length=40)

  def __str__(self):
    return self.first_name

  @property
  def full_name(self):
    return '%s %s' % (self.first_name, self.last_name)


#class SmartPlug(models.Model):


#class GSource(models.Model):
