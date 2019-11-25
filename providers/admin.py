from django.contrib import admin
from .models import Providers

# Register your models here.
admin.site.register(Providers)

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('registered')