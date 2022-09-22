from django.contrib import admin
from login.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# admin.site.register(Account)

class AccountInline(admin.StackedInline):
    model = Account
    can_delete=False
    verbose_name_plural="Accounts"

class CustomizedUserAdmin (UserAdmin):
    inlines=(AccountInline,)


admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(Account)