from django.contrib import admin
from .models import Django_Table

# Register your models here.
@admin.register(Django_Table)
class DjangoAdmin(admin.ModelAdmin):
    display_list = ['name','age','salary']

