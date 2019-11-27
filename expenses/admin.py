from django.contrib import admin

from .models import Expenses

class ExpensesAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_payment_register')


# Register your models here.
admin.site.register(Expenses)
