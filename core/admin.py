from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile


# Register your models here

class AccountAdmin(UserAdmin):
    list_display = ["email", "date_joined", "last_login"]
    readonly_fields = ["last_login", "date_joined"]

    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()


admin.site.register(Profile, AccountAdmin)