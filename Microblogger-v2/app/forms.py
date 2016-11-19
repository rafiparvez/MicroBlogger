from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

#LoginForm class gets derived from Form Class
class LoginForm(FlaskForm):
	openid = StringField('openid', validators=[DataRequired(message='Please enter your user id')])
	remember_me=BooleanField('remember_me', default=False)