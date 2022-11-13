from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from import_export.admin import ImportExportModelAdmin

from store.models import StoreClothes, StoreAccessories


class StoreClothesRequestAdmin(ImportExportModelAdmin):
    pass


admin.site.register(StoreClothes, StoreClothesRequestAdmin)


class StoreAccessoriesRequestAdmin(ImportExportModelAdmin):
    pass


admin.site.register(StoreAccessories, StoreAccessoriesRequestAdmin)


# pot adauga/modifica iteme din baza de date direct din interfata de admin



