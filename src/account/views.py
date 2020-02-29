from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
import requests
# Create your views here.
from .forms import AccountAuthenticationForm, RegistrationForm, UserForm, ProfileForm
from blog.models import BlogPost


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form

    return render(request, "account/login.html", context)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect("home")
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def update_profile(request):
    context = {}
    if request.POST:
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "first_name": request.POST['first_name'],
                "last_name": request.POST['last_name'],
            }
            form.save()
            context['success_message'] = 'Updated'
            return redirect("edit")

    else:
        form = UserForm(initial={
            "first_name": request.user.first_name, "email": request.user.email, "last_name": request.user.last_name})

    context['user_form'] = form
    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    return render(request, "account/edit.html", context)


def must_authenticate(request):
    return render(request, 'account/must_authenticate.html', {})
