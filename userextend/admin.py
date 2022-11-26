from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission, User
from import_export.admin import ImportExportModelAdmin

from userextend.models import UserExtend


class UserExtendRequestAdmin(ImportExportModelAdmin):
    pass


admin.site.register(UserExtend, UserExtendRequestAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(Permission)
