from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField #, StringField, PasswordField, BooleanField\
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload')
