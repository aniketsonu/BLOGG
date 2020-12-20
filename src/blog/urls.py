from . views import create_blog, detail_blog_view, edit_blog
from django.urls import path
app_name = 'blog'

urlpatterns = [
    path('create/', create_blog, name='create'),
    path('<slug>/', detail_blog_view, name='detail'),
    path('<slug>/edit/', edit_blog, name='edit')
]
