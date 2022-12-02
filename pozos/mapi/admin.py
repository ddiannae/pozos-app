from django.contrib import admin
from .models import Pozo

class PozoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pozo._meta.get_fields()]

admin.site.register(Pozo, PozoAdmin)
