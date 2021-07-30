from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

@deconstructible
class allowListEmailValidator(EmailValidator):

  def validate_domain_part(self, domain_part):
    return False

  def __eq__(self, other):
    return isinstance(other, allowListEmailValidator) and super().__eq__(other)