from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog

# Create your views here.
from account.models import Account

from .models import BlogPost


def create_blog(request):
    title = 'Create Blog'
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlog(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        return redirect('home')

    context['blog_form'] = form
    context['title'] = title
    return render(request, "blog/create.html", context)


def detail_blog_view(request, slug):
    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)

def edit_blog(request, slug):
    title = 'Update Blog'
    context = {}
    user = request.user
    blog_post = get_object_or_404(BlogPost, slug=slug)
    form = CreateBlog(request.POST or None, request.FILES or None, instance=blog_post)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        return redirect('home')

    context['blog_form'] = form
    context['blog_post'] = blog_post
    context['title'] = title
    return render(request, "blog/create.html", context)
