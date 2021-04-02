from django.core.exceptions import ValidationError
import re


def validate_email(value):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not (re.search(regex, value)):
        raise ValidationError('Wrong email')


def validate_text(value):
    regex = '^.{1,100}$'
    if not (re.search(regex, value)):
        raise ValidationError('Message must contain between 1 and 100 characters')
