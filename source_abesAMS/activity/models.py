from django.db import models

# Create your models here.

from django.utils import timezone
from django.core.exceptions import ValidationError
from user.models import  CustomUser


class Activity(models.Model):
	opened_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	edit_permissions = models.ManyToManyField(CustomUser,related_name="permitted_users")
	activity_name = models.CharField(max_length=255)
	frequency = models.IntegerField(blank=True,null=True)
	start_date = models.DateTimeField(default=None)
	end_date = models.DateTimeField(default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f"{self.activity_name}--{self.frequency}--{self.start_date}--{self.end_date}"

class SubActivity(models.Model):
	belongs_to = models.ForeignKey(Activity,on_delete=models.CASCADE)
	name = models.CharField(max_length=255,)
	description = models.TextField(blank=True)
	document = models.FileField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.name}"