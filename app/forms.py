from flask_wtf import FlaskForm
from flask_login import LoginManager, current_user, login_user
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, NumberRange, Email, EqualTo
from app.models import User

# Form to create a support ticket
class TicketCreate(FlaskForm):
	cx_id = StringField('Customer ID', validators=[DataRequired()])
	contact_name = StringField('Contact Name', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	version = IntegerField('Version', validators=[NumberRange(min=2000,max=2020)])
	priority =  StringField('Priority')
	status =StringField('Status')
	o365 = BooleanField('Office 365')
	assigned_to = StringField('Assigned to', validators=[DataRequired()])

# Login form for index.html
class MyForm(FlaskForm):
    log_in_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# Search fields for support tickets
class TicketSearch(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	address = TextAreaField('Address', validators=[DataRequired()])
	cx_id = IntegerField('Customer ID', validators=[NumberRange(min=4000000000,max=4009999999)])
	order_num = IntegerField('Order Number', validators=[NumberRange(min=1000000000,max=1009999999)])

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')