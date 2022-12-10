from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from user.models import CustomUser

from . forms import *


def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
    	form = SignupForm(request.POST)
    	if form.is_valid():
    		# print(form.cleaned_data)
    		if form.cleaned_data.get('password')==form.cleaned_data.get('confirm_password'):
    			user = CustomUser.objects.create_user(email=form.cleaned_data.get('email'),username=form.cleaned_data.get('username'),password=form.cleaned_data.get('password'))
    			user.save()
    			messages.success(request,"Sign Up successful")
    			return redirect('login-view')
    		else:
    			messages.warning(request,"Password mismatched")
    			return redirect('signup-view')
    context = {
    	'form':form
    }
    return render(request,'signup.html',context)

def login_view(request):
    form = SigninForm()
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username=email,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,f"Login successful, wlecome {user.username}")
                return redirect("timeline-view")
            else:
                messages.warning(request,f'Incorrect credentials')
                # storage = get_messages(request)
                # for message in storage:
                #     print(message.tags)
                #     print(message.level)
                return redirect('login-view')
    context = {
        'form':form,
    }
    return render (request,'login.html',context)


def logout_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout(request)
            return redirect('login-view')

@login_required(login_url="signup-view")
def timeline_view(request):
	return render(request,"timeline.html")