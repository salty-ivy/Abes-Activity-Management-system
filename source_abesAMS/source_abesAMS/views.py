from django.shortcuts import render
from user.models import CustomUser
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout


def login_view(request):
	return render(request,"login.html")


def logout_view(request):
	pass