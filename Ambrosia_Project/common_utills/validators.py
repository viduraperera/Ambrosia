from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def nic_validator(value):
    if len(value) < 10:
        raise ValidationError(
            _('%(value)s should have more than 10 characters.'),
            params={'value': value},
        )
