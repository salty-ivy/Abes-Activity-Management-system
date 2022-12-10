from django.forms import ModelForm
from django import forms
from django.forms import ValidationError

from user.models import CustomUser
from activity.models import *

def email_abes_check(value):
	if not value.endswith("@abes.ac.in"):
		raise ValidationError("This email domain doesn't belongs to ABES")

class SignupForm(forms.Form):
	email = forms.EmailField(required=True,validators=[email_abes_check],widget=forms.TextInput(attrs={'class':'input','placeholder':'example@abes.ac.in'}))
	username = forms.CharField(max_length=100,required=True)
	password = forms.CharField(max_length=200,widget=forms.PasswordInput,required=True)
	confirm_password = forms.CharField(max_length=255,label="Confirm Password",widget=forms.PasswordInput)

	email.widget.attrs.update({'class':'input','placeholder':'example@abes.ac.in'})
	username.widget.attrs.update({'class':'input','placeholder':'username'})
	password.widget.attrs.update({'class':'input','placeholder':'*****'})
	confirm_password.widget.attrs.update({'class':'input','placeholder':'*****'})

	def clean_email(self):
		email = self.cleaned_data['email']
		if CustomUser.objects.filter(email=email).exists():
			raise ValidationError("Email already used")
		else:
			return email

	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password)<=5:
			raise ValidationError("Length must be more then 5 characters")
		else:
			return password


class SigninForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True,widget=forms.PasswordInput)

	email.widget.attrs.update({'class':'input','id':'email','placeholder':'name.admission@abes.ac.in'})
	password.widget.attrs.update({'class':'input','placeholder':'********'})