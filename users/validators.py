import re
from django.core.exceptions import ValidationError

def validate_names(value):
    """Validator to ensure names contain only letters"""
    if not value.isalpha():
        raise ValidationError(f'Name should contain only letters')
