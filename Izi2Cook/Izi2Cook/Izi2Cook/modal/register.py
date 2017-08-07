from flask_wtf import Form
from wtforms import *
from wtforms.fields.html5 import EmailField

class RegistrationForm(Form):
    Firstname = StringField('Firstname', [validators.Length(min=4, max=20)])
    LastName = StringField('Lastname ', [validators.Length(min=4, max=20)])
    Username = StringField('Username', [validators.Length(min=4, max=20)])
    Email = StringField('Email', [validators.Length(min=6, max=50)])
    Pwd = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])
