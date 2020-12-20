from django.shortcuts import render, redirect

from django.contrib.auth.models import auth, User

from account.models import Account, MyAccountManager

from blog.models import BlogPost


def home_page(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    blog_posts = BlogPost.objects.all
    context['blog_posts'] = blog_posts
    return render(request, 'home.html', context)
