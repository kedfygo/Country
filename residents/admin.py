from django.contrib import admin

from .models import Residents

# Register your models here.
class ResidentsAdmin(admin.ModelAdmin):
    list_display = ['name', 
                    'lastname', 
                    'address', 
                    'phone_number', 
                    'email', 
                    'type_of_property', 
                    'owner_name', 
                    'owner_phone_number']
    list_filter = ['name']

admin.site.register(Residents, ResidentsAdmin)