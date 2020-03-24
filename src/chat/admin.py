from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Chat


# Register your models here.


'''class AccountAdmin(UserAdmin):
    list_display = ('room_name', 'email')
    search_fields = ('email', 'room_name',)'''


admin.site.register(Chat)
