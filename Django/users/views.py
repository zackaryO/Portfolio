from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You are logged in')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # Redirect to the desired page if already logged in
        return redirect('/portfolio/resumes/')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  # Or your custom login form with request.POST
        if form.is_valid():
            # Authenticate and login the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the desired page after successful login
                return redirect('/portfolio/resumes/')
    else:
        form = AuthenticationForm()  # Or initialize your custom login form here

    return render(request, 'users/login.html', {'form': form})


@login_required
def profilepage(request):
    return render(request, 'users/profile.html')


from django.shortcuts import render

# Create your views here.
