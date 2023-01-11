from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'last_name')
    list_filter = ('email', 'username', 'is_active', 'is_superuser')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'is_active', 'is_superuser')
    readonly_fields = ['date_joined', 'last_login']


fieldsets = (
    (None, {'fields': ('email', 'username', )}),
    ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    ('Personal', {'fields': ('about', 'last_name', 'first_name')}),
)

admin.site.register(Account, UserAdminConfig)
