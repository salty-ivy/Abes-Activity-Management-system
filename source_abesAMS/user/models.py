from django.db import models

# Create your models here.
from django.contrib.auth.models import (

			AbstractBaseUser,
			PermissionsMixin,
			BaseUserManager,
	)
import uuid
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_email_domain(email: str):
	end_str = "@abes.ac.in"
	if not email.endswith(end_str):
		raise ValidationError("Invalid email domain, this domain is not allowed")

class CustomUserManager(BaseUserManager):

	def create_user(self,email,username,password=None):
		if password is None:
			raise ValidationError("Password is missing")
		elif username is None:
			raise ValidationError("Username is missing")
		elif email is None:
			raise ValidationError("Email is missing")

		else:
			user = self.model(email=email,username=username)
			user.set_password(password)
			user.save(using=self._db)
			return user

	def create_superuser(self,email,username,password):
		user = self.create_user(email,username,password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
	uid = models.CharField(max_length=255,unique=True,default=uuid.uuid4,db_index=True)
	email = models.EmailField(max_length=200,unique=True,db_index=True,validators=[validate_email_domain])
	username = models.CharField(max_length=255,null=False,blank=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	last_login = models.DateTimeField(null=True)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']