from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    """
    Validates that the phone number starts with '09' (11 digits) or '9' (10 digits).
    """
    if value.startswith('09') and len(value) != 11:
        raise ValidationError(
            _('Phone number starting with "09" must be exactly 11 digits.'),
            params={'value': value},
        )
    elif value.startswith('9') and not value.startswith('09') and len(value) != 10:
        raise ValidationError(
            _('Phone number starting with "9" must be exactly 10 digits.'),
            params={'value': value},
        )
    elif not value.startswith('09') and not value.startswith('9'):
        raise ValidationError(
            _('Phone number must start with "09" or "9".'),
            params={'value': value},
        )