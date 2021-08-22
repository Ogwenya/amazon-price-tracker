from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import SignUpForm

# Create your views here.
# signup view
def user_signup(request):
	form = None
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('dashboard')
	else:
		form = SignUpForm()

	context = {
		'form': form
	}
	return render(request, 'accounts/signup.html', context)

# login view
def user_login(request):
	form = None
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('dashboard')
	else:
		form = AuthenticationForm()

	context = {
		'form': form
	}
	return render(request, 'accounts/login.html', context)

# logout
def user_logout(request):
	if request.method == 'POST':
		logout(request)

		return redirect('home')