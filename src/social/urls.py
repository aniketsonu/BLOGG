from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from app1.views import home_page

from account.views import (
    login_view,
    registration_view,
    logout_view,
    update_profile,
    must_authenticate
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('must_authenticate/', must_authenticate, name="must_authenticate"),
    path('', home_page, name="home"),
    path('login/', login_view, name="login"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/edit/', update_profile, name="edit"),
    path('login/password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
         name='password_change'),
    path('login/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
         name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
