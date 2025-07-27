from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined' )
    list_display_links = ('email', 'first_name', 'last_name', 'username', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-id',)
    fieldsets = ()
admin.site.register(Account,AccountAdmin)

# Register your models here.
