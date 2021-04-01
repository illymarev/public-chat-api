from django.core.exceptions import ValidationError


def validate_email(self, value):
    if value != '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$':
        return ValidationError('wrong email')

    # def clean(self):
    #     if self.text == '^(?![\s\S])':
    #         raise ValidationError
    #     elif self.text != '^[A-Z]{1,100}$':
    #         raise ValidationError
    #     elif self.email != '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$':
    #         raise ValidationError
