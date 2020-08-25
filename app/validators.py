from wtforms.validators import ValidationError
from email_validator import validate_email, EmailNotValidError

def Email():
    def _email(FlaskForm, Field):
        try:
            validate_email(Field.data)
        except EmailNotValidError:
            raise ValidationError("Please, use a valid email address.")
    
    return _email