import re

from django.core.exceptions import ValidationError

VALIDATE_USERNAME_VALIDATION_ERROR = "Ensure this value contains only letters, numbers, and underscore."


def validate_username_chars(value):
    pattern = "^[A-Za-z0-9_]*$"
    state = bool(re.match(pattern, value))
    if not state:
        raise ValidationError(VALIDATE_USERNAME_VALIDATION_ERROR)
