from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Biometry
from django.contrib.auth.models import User
# Register your models here.

# Have custom fields added on an existing model
class BiometryInline(admin.StackedInline):
    model = Biometry
    can_delete = False

class CustomizedUserAdmin (UserAdmin):
    inlines = (BiometryInline, )

# Re-register the admin panel
admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

# creates a separate entry
admin.site.register(Biometry)